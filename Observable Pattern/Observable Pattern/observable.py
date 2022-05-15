import imp
import zope.interface

from observer import Observer


class Subject(zope.interface.Interface):
    def add_observer(self,obs:Observer):
        pass
    
    def remove_observer(self,osb:Observer):
        pass

    def __notify_observers(self,data:str):
        pass

@zope.interface.implementer(Subject)
class ConcreteObservable:

    def __init__(self) -> None:
        self.obsevers:list[Observer] = []

    def add_observer(self,obs:Observer):
        self.obsevers.append(obs)

    def remove_observer(self,obs:Observer):
        self.obsevers.remove(obs)
    
    def __notify_observers(self,data:str):
        for observer in self.obsevers:
            observer.notified(data)
    
    def changed(self,data:str):
        self.__notify_observers(data)
    

    
    