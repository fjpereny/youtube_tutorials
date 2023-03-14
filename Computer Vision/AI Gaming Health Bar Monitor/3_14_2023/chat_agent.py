

import random
import pyautogui
import time
from typos import Typos


class ChatType:
    say = '/s '
    yell = '/y '
    guild = '/g '
    party = '/p '
    world = '/1 '
    trade = '/2 '


class ChatAgent:
    def __init__(self) -> None:
        self.is_chatting = False
        self.cur_chat_type = None

        self.typo_chance = 1
        self.space_pause_chance = 30


    def chat(self, msg, chat_type=ChatType.say, caps=False, lower=False):
        self.is_chatting = True

        if caps:
            msg = msg.upper()
        if lower:
            msg = msg.lower()

        

        # Initialize chat by the enter key
        pyautogui.press('enter')
        rand_sleep_time = random.random() / 3.0 + 0.1
        time.sleep(rand_sleep_time)

        # Call the correct chat type (say / guild / party)
        if chat_type != self.cur_chat_type:
            rand_type_time = random.random() / 4.0  + 0.1
            pyautogui.typewrite(chat_type, interval=rand_type_time)
            self.cur_chat_type = chat_type
        rand_sleep_time = random.random() / 3.0 + 0.1
        time.sleep(rand_sleep_time)


        # Type our message and send it
        for c in msg:
            if c == ' ':
                pause_chance = random.randint(0, 100)
                if pause_chance <= self.space_pause_chance:
                    pyautogui.typewrite(' ')
                    rand_sleep_time = random.randint(0, 4) / 3.0 + 0.1
                    time.sleep(rand_sleep_time)
                else:
                    pyautogui.typewrite(' ')

            elif c.isalpha():
                typo = random.randint(0, 100)
                if typo <= self.typo_chance:
                    typo_c = Typos.make_typo(c.lower())
                    if c.islower():
                        pyautogui.typewrite(typo_c)
                    else:
                        pyautogui.typewrite(typo_c.upper())
                else:
                    pyautogui.typewrite(c)

            else:
                pyautogui.typewrite(c)

            rand_type_time = random.randint(0, 2000) * 0.0001
            time.sleep(rand_type_time)

        rand_sleep_time = random.random() / 2.0 + 0.1

        pyautogui.press('enter')


        self.is_chatting = False


if __name__ == "__main__":
    chat_agent = ChatAgent()
    chat_agent.chat("What goes around may come around, but it never ends up exactly the same place, you ever notice? Like a record on a turntable, all it takes is one groove's difference and the universe can be on into a whole 'nother song.")





