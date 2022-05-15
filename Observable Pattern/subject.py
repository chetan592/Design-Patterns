from observer import Observers

class Subject:
    
    def __init__(self) -> None:
        self.obervables:list = []

    def add_observer(self,obs:Observers):
        self.obervables.append(obs)

    def emit(self,data:str):
        self.__notify(data)

    def __notify(self,data:str):
        for obs in self.obervables:
            obs.notified(data)