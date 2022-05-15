import  zope.interface

class Observers(zope.interface.Interface):
    def notified():
        pass


@zope.interface.implementer(Observers)
class Observer:
    def notified(self,data:str):
        print(f'stream(Observable) ... :{data}')

@zope.interface.implementer(Observers)
class ObserverSecond:
    def notified(self,data:str):
        print(f'stream(ObservableSecond)... {data}')

