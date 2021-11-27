from mvc.model.Observable import Observable


class Observer:
    def update(self):
        pass

    def observe(self, observable: Observable):
        observable.add_observer(self)

    def stop_observing(self, observable: Observable):
        observable.remove_observer(self)
