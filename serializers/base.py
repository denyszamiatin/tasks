import os


class BaseSerializer:
    DATA_DIR = 'data'

    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)

    def __init__(self, filename=None):
        if filename is None:
            filename = self.FILENAME
        self.filename = os.path.join(self.DATA_DIR, filename)

    def load(self):
        try:
            return self._load()
        except FileNotFoundError:
            return {}

    def _load(self):
        pass