import threading


class BaseEntropySource(object):
    def __init__(self, buffer):
        self.buffer = buffer
        self.is_running = True
        self.thread = threading.Thread(target=self.collect_entropy)
        self.thread.start()

    def collect_entropy(self):
        pass

    def release(self):
        self.is_running = False
