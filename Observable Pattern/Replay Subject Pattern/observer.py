import zope.interface

class Observer(zope.interface.Interface):
    def notified(self,data:str):
        pass

@zope.interface.implementer(Observer)
class ConcreteObserver:
    def notified(self,data:str):
        print(f'Stream(ConcreteObserver) ... {data}')

@zope.interface.implementer(Observer)
class ConcreteObserverSecond:
    def notified(self,data:str):
        print(f'Stream(ConcreteObserverSecond) ... {data}')

@zope.interface.implementer(Observer)
class ConcreteObserverThird:
    def notified(self,data:str):
        print(f'Stream(ConcreteObserverThird) ... {data}')

    