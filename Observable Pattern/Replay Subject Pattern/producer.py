from replay_subject import SubjectInterface, ReplaySubject


class Producer:

    def add_subject(self,subject:SubjectInterface):
        self.__subject = subject

    def changed(self,data:str):
        self.__subject.emit(data)