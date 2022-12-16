
import mss
import pyautogui
import cv2 as cv
import numpy as np
import time
import multiprocessing


class ScreenCaptureAgent:
    def __init__(self) -> None:
        self.img = None
        self.capture_process = None
        self.fps = None

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
                small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5)
                cv.imshow("Computer Vision", small)

                elapsed_time = time.time() - fps_report_time
                if elapsed_time >= fps_report_delay:
                    print(f'{bcolors.PINK}FPS: {(n_frames / elapsed_time):.2f}{bcolors.ENDC}')
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
                print("{bcolors.YELLOW}WARNING:{bcolors.ENDC} A capture process is already running!")
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