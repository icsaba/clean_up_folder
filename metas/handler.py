from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, *args, **kwargs):
        res = self._handle(*args, **kwargs)
        if not res:
            self.successor.handle(*args, **kwargs)

    @abstractmethod
    def _handle(self, *args, **kwargs):
        raise NotImplementedError()
