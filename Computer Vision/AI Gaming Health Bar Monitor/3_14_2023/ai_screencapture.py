
import mss
import pyautogui
import cv2 as cv
import numpy as np
import time
import multiprocessing

import healbot
import map_reader
import nav
import move


SHOW_COMP_VISION_WINDOW = True
SHOW_HEALTH_BAR_WINDOW = False


class ScreenCaptureAgent:
    def __init__(self) -> None:
        self.img = None
        self.img_health = None
        self.img_health_HSV = None
        self.capture_process = None
        self.fps = None
        self.enable_cv_preview = True

        self.zone = None

        self.enable_nav = True
        self.nav_target = cv.imread('target.png')
        self.nav_loc = None
        self.nav_loc_match = None

        self.top_left = (459, 733)
        self.bottom_right = (594, 751)

        self.w, self.h = pyautogui.size()
        print("Screen Resolution: " + "w: " + str(self.w) + " h:" + str(self.h))
        self.monitor = {"top": 0, "left": 0, "width": self.w, "height": self.h}

    def capture_screen(self):

        fps_report_time = time.time()
        fps_report_delay = 5
        n_frames = 1
        with mss.mss() as sct:
            while True:
                self.img = sct.grab(monitor=self.monitor)
                self.img = np.array(self.img)
                self.img = cv.cvtColor(self.img, cv.COLOR_BGRA2BGR)

                self.zone = map_reader.get_cur_zone(self.img)
                self.zone = self.zone.lower().strip()

                self.img_health = self.img[
                    self.top_left[1]:self.bottom_right[1],
                    self.top_left[0]:self.bottom_right[0]
                ]

                self.img_health_HSV = cv.cvtColor(self.img_health, cv.COLOR_BGR2HSV)

                if self.enable_nav:
                    nav_loc = cv.matchTemplate(self.img, self.nav_target, cv.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(nav_loc)
                    self.nav_loc = max_loc
                    self.nav_loc_match = np.round(max_val * 100, 2)
                    if self.nav_loc_match < 85:
                        self.nav_loc = None

                if self.enable_cv_preview:
                    small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5)
                    if self.fps is None:
                        fps_text = ""
                    else:
                        fps_text = f'FPS: {self.fps:.2f}'
                    cv.putText(
                        small, 
                        fps_text, 
                        (25, 50), 
                        cv.FONT_HERSHEY_DUPLEX,
                        1,
                        (255, 0, 255),
                        1,
                        cv.LINE_AA)
                    cv.putText(
                        small, 
                        "Health: " + str(hue_match_pct(self.img_health_HSV, 80, 115)), 
                        (25, 100), 
                        cv.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 0, 255),
                        1,
                        cv.LINE_AA)
                    cv.putText(
                        small, 
                        "Zone: " + self.zone, 
                        (25, 150), 
                        cv.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 255, 255),
                        1,
                        cv.LINE_AA)   
                    
                    if self.enable_nav:
                        cv.putText(
                        small, 
                        "Nav Target: " + str(self.nav_loc) + f" {self.nav_loc_match}%", 
                        (25, 200), 
                        cv.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 255, 0),
                        1,
                        cv.LINE_AA)   
                        if self.nav_loc:
                            turn_angle = np.round(nav.get_nav_turn_angle(self.nav_loc) * 180 / 3.14, 2)
                            pitch_angle = None
                            cv.putText(
                            small, 
                            "Nav Rotate Angle: " + str(turn_angle) + " deg", 
                            (25, 250), 
                            cv.FONT_HERSHEY_DUPLEX,
                            1,
                            (0, 255, 0),
                            1,
                            cv.LINE_AA)
                        
                            if turn_angle > 10:
                                move.bump_left(0.01)
                            elif turn_angle < -10:
                                move.bump_right(0.01)
                            
                            pitch_angle = np.round(nav.get_nav_elevation_ratio(self.nav_loc) * 180 / 3.14, 2)
                            cv.putText(
                            small, 
                            "Nav Pitch Ratio: " + str(pitch_angle) + " deg", 
                            (25, 300), 
                            cv.FONT_HERSHEY_DUPLEX,
                            1,
                            (0, 255, 0),
                            1,
                            cv.LINE_AA)
                        
                            # if pitch_angle > 10:
                            #     move.bump_left(0.01)
                            # elif pitch_angle < -10:
                            #     move.bump_right(0.01)
                    
                    
                    if SHOW_COMP_VISION_WINDOW:
                        cv.imshow("Computer Vision", small)

                    if SHOW_HEALTH_BAR_WINDOW:
                        cv.imshow("Health Bar", self.img_health)


                elapsed_time = time.time() - fps_report_time
                if elapsed_time >= fps_report_delay:
                    self.fps = n_frames / elapsed_time
                    print(f'{bcolors.PINK}FPS: {self.fps:.2f}{bcolors.ENDC}')
                    fps_report_time = time.time()
                    n_frames = 1
                n_frames += 1
                cv.waitKey(1)



class bcolors:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'


def convert_hue(hue):
    ratio = 361 / 180
    return np.round(hue / ratio, 2)


def hue_match_pct(img, hue_low, hue_high):
    match_pixels = 0
    no_match_pixels = 0
    for pixel in img:
        for h, s, v in pixel:
            if convert_hue(hue_low) <= h <= convert_hue(hue_high):
                match_pixels += 1
            else:
                no_match_pixels +=1
    total_pixels = match_pixels + no_match_pixels
    pct_health = np.round(match_pixels / total_pixels, 2) * 100

    if pct_health <= 50:
        healbot.cast_spell('big_heal')
    elif pct_health <= 70:
        healbot.cast_spell('small_heal')

    return pct_health


def print_menu():
    print(f"{bcolors.CYAN}Command Menu{bcolors.ENDC}")
    print(f"\t{bcolors.GREEN}r - run{bcolors.ENDC}\t\t-\tStart screen capture")
    print(f"\t{bcolors.RED}s - stop{bcolors.ENDC}\t-\tStop screen capture")
    print("\tq - quit\t-\tQuit the program")


if __name__ == "__main__":
    screen_agent = ScreenCaptureAgent()

    while True:
        print_menu()
        user_input = input().strip().lower()
        if user_input == 'quit' or user_input == 'q':
            if screen_agent.capture_process is not None:
                screen_agent.capture_process.terminate()
            break
        elif user_input == 'run' or user_input == 'r':
            if screen_agent.capture_process is not None:
                print(f"{bcolors.YELLOW}WARNING:{bcolors.ENDC} A capture process is already running!")
                continue
            screen_agent.capture_process = multiprocessing.Process(
                target=screen_agent.capture_screen, 
                args=(), 
                name="screen capture process")
            screen_agent.capture_process.start()
        elif user_input == 'stop' or user_input == 's':
            if screen_agent.capture_process is None:
                print(f"{bcolors.YELLOW}WARNING:{bcolors.ENDC} A capture process is not running!")
                continue
            screen_agent.capture_process.terminate()
            screen_agent.capture_process = None
        else:
            print(f"{bcolors.RED}ERROR:{bcolors.ENDC} Unknown command.")

print("Done.")


