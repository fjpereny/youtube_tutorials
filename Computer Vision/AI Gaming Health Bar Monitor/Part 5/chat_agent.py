
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
        self.msg_queue = []
        self.msg_delay = 3
        self.is_chatting = False
        self.cur_chat_type = None

    def chat(self, msg, chat_type=ChatType.say, caps=False):
        
        self.is_chatting = True

        if caps:
            msg = msg.upper()

        # Initialize chat by pressing the enter key
        pyautogui.press('enter')
        rand_sleep_time = random.random() / 5.0 + 0.1
        time.sleep(rand_sleep_time)

        # Call correct chat type (say / guild / etc)
        if chat_type != self.cur_chat_type:
            rand_type_time = random.randint(1, 5) * 0.005 * len(msg)
            pyautogui.typewrite(chat_type, interval=rand_type_time)
            rand_sleep_time = random.random() / 5.0 + 0.1
            time.sleep(rand_sleep_time)
            self.cur_chat_type = chat_type

        # Type and send message
        words = msg.split(' ')
        for word in words:
            rand_type_time = random.randint(4, 7) * 0.003 * len(word)
            pyautogui.typewrite(word, interval=rand_type_time)
            if word != words[-1]:
                pyautogui.press('space')
        pyautogui.press('enter')

        self.is_chatting = False


if __name__ == '__main__':

    chat_agent = ChatAgent()
    while True:
        chat_agent.chat("Hello, World!")
        chat_agent.chat("This is still a 'say' chat...")
        chat_agent.chat("yo!", chat_type=ChatType.yell, caps=True)
        time.sleep(5)





