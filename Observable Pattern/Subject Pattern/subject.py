from observer import Observer

class Subject:
    
    def __init__(self) -> None:
        self.observers:list = []

    def add_observer(self,obs:Observer):
        self.observers.append(obs)

    def remove_observer(self,obs:Observer):
        self.observers.remove(obs)

    def emit(self,data:str):
        self.__notify_observers(data)

    def __notify_observers(self,data:str):
        for obs in self.observers:
            obs.notified(data)