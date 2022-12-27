

import random
import pyautogui
import time


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
        words = msg.split(' ')
        for i in range(0, len(words)):
            word = words[i]
            rand_type_time = random.randint(4, 7) * 0.003 * len(word)
            pyautogui.typewrite(word, interval=rand_type_time)
            if i != len(words) - 1:
                time.sleep(0.005)
                pyautogui.press('space')

        rand_sleep_time = random.random() / 2.0 + 0.1

        pyautogui.press('enter')


        self.is_chatting = False


if __name__ == "__main__":
    chat_agent = ChatAgent()
    chat_agent.chat("Hello, world!")
    chat_agent.chat("Testing, 1 2 3!")
    chat_agent.chat("This is a very long string.... let's see how this works!")
    chat_agent.chat("Hello, world!", chat_type=ChatType.party, lower=True)


