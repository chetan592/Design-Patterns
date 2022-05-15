from click import pass_context
import zope.interface

from observer import Observer

class SubjectInterface(zope.interface.Interface):
    def add_observer(self,obs:Observer):
        pass

    def remove_observer(self,obs:Observer):
        pass

    def emit(self,data:str):
        pass

    def __notify_observers(self,data:str):
        pass

@zope.interface.implementer(SubjectInterface)
class ReplaySubject:
    def __init__(self,replay:int) -> None:
        self.replay = replay
        self.__replay_list = []
        self.__observers:list[Observer] = []

    def add_observer(self,obs:Observer):
        self.__observers.append(obs)
        self.__replay_data(obs)

    def remove_observer(self,obs:Observer):
        self.__observers.remove(obs)

    def emit(self,data:str):
        self.__notify_observers(data)
        self.__add_to_replay(data)

    def __add_to_replay(self,data:str):
        if self.replay == 0:
            return

        if len(self.__replay_list) == self.replay:
            self.__replay_list.pop(0)
        
        self.__replay_list.append(data)
        
    def __replay_data(self,obs:Observer):
        for value in self.__replay_list:
            obs.notified(value)

    def __notify_observers(self,data:str):
        for observer in self.__observers:
            observer.notified(data)
