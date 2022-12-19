

import multiprocessing
import time
from color_test import ConsoleColor

class CLI_Spinner:
    def __init__(self, message="", speed=0.1) -> None:
        self.message = message
        self.speed = speed
        self.process = multiprocessing.Process(
            target=self.spin,
            args=(),
            name="CLI Spinner",
        )

    
    def spin(self):

        spinner = ['-', '\\', '|', '/', '0']
        n = 0
        while True:
            print(f"\r{self.message}{spinner[n]}", end="")
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)   


    def start(self):
        self.process.start()


    def stop(self):
        if not self.process.is_alive():
            print("Warning: CLI Spinner process is not running.")
        else:
            self.process.terminate()
            print()
        

if __name__ == "__main__":
    spinner = CLI_Spinner(message="Running App - ")
    spinner.start()
    i = 0
    while i < 10:
        time.sleep(.3)
        i += 1
    spinner.stop()
    print(i)