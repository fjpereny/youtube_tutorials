
import multiprocessing
import time

class CLI_Spinner:
    def __init__(self, message="", speed=0.1) -> None:
        self.message = message
        self.speed = speed

        self.process = multiprocessing.Process(
            target=self.spin,
            args=(),
            name="CLI Spinner"
        )


    def spin(self):
        spinner = ['-', '\\', '|', '/']
        n = 0
        while True:
            print(f'\r{self.message}{spinner[n]}', end="")
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)


    def start(self):
        self.process.start()


    def stop(self):
        if not self.process.is_alive():
            print("Warning: CLI spinner is not running.")
        else:
            self.process.terminate()
            print()


if __name__ == "__main__":
    spinner = CLI_Spinner("Hello...", 0.2)
    spinner.start()
    print("Your code here...")
    time.sleep(5)
    spinner.stop()
