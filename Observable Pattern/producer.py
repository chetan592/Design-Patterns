from subject import Subject

class Producer:
    
    def __init__(self,subject:Subject):
        self.subject = subject

    def data_changed(self,data:str):
        self.subject.emit(data)