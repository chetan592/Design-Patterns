import  zope.interface

class Observer(zope.interface.Interface):
    def notified():
        pass


@zope.interface.implementer(Observer)
class ConcreteObserver:
    def notified(self,data:str):
        print(f'stream(Observable) ... :{data}')

@zope.interface.implementer(Observer)
class ConcreteObserverSecond:
    def notified(self,data:str):
        print(f'stream(ObservableSecond)... {data}')

