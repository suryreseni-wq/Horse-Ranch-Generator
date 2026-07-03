import time


class Logger:

    def __init__(self):

        self.start = time.time()

    def info(self, text):

        print(f"[INFO] {text}")

    def warning(self, text):

        print(f"[WARNING] {text}")

    def error(self, text):

        print(f"[ERROR] {text}")

    def finish(self):

        print(f"Finished in {time.time()-self.start:.2f}s")
