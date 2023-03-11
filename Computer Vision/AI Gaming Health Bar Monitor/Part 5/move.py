

import pyautogui
import time


KEY_RUN = 'numlock'
KEY_JUMP = 'space'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'
KEY_FORWARD = 'w'
KEY_BACKWARD = 's'
KEY_STRAFE_LEFT = 'q'
KEY_STRAFE_RIGHT = 'e'
KEY_SHEATHE = 'z'
KEY_SIT = 'x'

def forward_start():
    pyautogui.keyDown(KEY_FORWARD)

def forward_stop():
    pyautogui.keyUp(KEY_FORWARD)

def backward_start():
    pyautogui.keyDown(KEY_BACKWARD)

def backward_stop():
    pyautogui.keyUp(KEY_BACKWARD)

def left_start():
    pyautogui.keyDown(KEY_LEFT)

def left_stop():
    pyautogui.keyUp(KEY_LEFT)

def right_start():
    pyautogui.keyDown(KEY_RIGHT)

def right_stop():
    pyautogui.keyUp(KEY_RIGHT)

def left_strafe_start():
    pyautogui.keyDown(KEY_STRAFE_LEFT)

def left_strafe_stop():
    pyautogui.keyUp(KEY_STRAFE_LEFT)

def right_strafe_start():
    pyautogui.keyDown(KEY_STRAFE_RIGHT)

def right_strafe_stop():
    pyautogui.keyUp(KEY_STRAFE_RIGHT)

def jump():
    pyautogui.press(KEY_JUMP)

def bump_forward(t=0.05):
    pyautogui.keyDown(KEY_FORWARD)
    time.sleep(t)
    pyautogui.keyUp(KEY_FORWARD)

def bump_backward():
    pyautogui.keyDown(KEY_BACKWARD)
    time.sleep(0.05)
    pyautogui.keyUp(KEY_BACKWARD)

def bump_left():
    pyautogui.keyDown(KEY_LEFT)
    time.sleep(0.05)
    pyautogui.keyUp(KEY_LEFT)

def bump_right():
    pyautogui.keyDown(KEY_RIGHT)
    time.sleep(0.05)
    pyautogui.keyUp(KEY_RIGHT)

def bump_strafe_left():
    pyautogui.keyDown(KEY_STRAFE_LEFT)
    time.sleep(0.05)
    pyautogui.keyUp(KEY_STRAFE_LEFT)

def bump_strafe_right():
    pyautogui.keyDown(KEY_STRAFE_RIGHT)
    time.sleep(0.05)
    pyautogui.keyUp(KEY_STRAFE_RIGHT)

def sheathe_toggle():
    pyautogui.press(KEY_SHEATHE)

def sit():
    pyautogui.press(KEY_SIT)


if __name__ == '__main__':
    time.sleep(10)
    while True:
        
        jump()
        time.sleep(1)

        forward_start()
        time.sleep(2)
        left_strafe_start()
        time.sleep(2)
        left_strafe_stop()
        time.sleep(1)

        right_strafe_start()
        time.sleep(2)
        right_strafe_stop()
        time.sleep(1)
        forward_stop()
        time.sleep(1)

        backward_start()
        time.sleep(2)
        backward_stop()
        time.sleep(1)

        left_start()
        time.sleep(2)
        left_stop()
        time.sleep(1)

        right_start()
        time.sleep(2)
        right_stop()
        time.sleep(1)

        sheathe_toggle()
        time.sleep(2)
        sit()
        time.sleep(2)
        jump()
        time.sleep(1)

        bump_forward()
        bump_backward()
        bump_left()
        bump_right()
        bump_strafe_left()
        bump_strafe_right()
        