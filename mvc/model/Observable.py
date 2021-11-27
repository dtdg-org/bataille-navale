class Observable:
    def __init__(self):
        self.observed_by  = []

    def update(self):
        for observer in self.observed_by:
            observer.update()

    def add_observer(self, observer):
        self.observed_by.append(observer)

    def remove_observer(self, observer):
        self.observed_by.remove(observer)
