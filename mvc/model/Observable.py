from abc import abstractmethod


class Observable:
    def __init__(self):
        self.observed_by = []

    @abstractmethod
    def update(self):
        for observer in self.observed_by:
            observer.update()

    @abstractmethod
    def add_observer(self, observer):
        self.observed_by.append(observer)

    @abstractmethod
    def remove_observer(self, observer):
        self.observed_by.remove(observer)
