from abc import ABCMeta, abstractmethod


class Updatable(metaclass=ABCMeta):

    @abstractmethod
    def update_quality(self):
        pass
