import threading


class WordCounter:
    def __init__(self):
        self.counter = dict()
        self.lock = threading.Lock()

    def process_text(self, text):
        self.lock.acquire()
        words = text.split(" ")
        for word in words:
            self.counter[word] = self.counter.get(word, 0) + 1
        self.lock.release()

    def get_word_count(self, word):
        return self.counter.get(word, 0)
