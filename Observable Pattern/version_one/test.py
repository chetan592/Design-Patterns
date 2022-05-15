from subject import Subject
from observer import ConcreteObserver,ConcreteObserverSecond
from producer import Producer

'''
    Observer desgin pattern to create a system which notifies about changes

    Roles - 
        Subject - Notifies the all subscribers
        Observer - Register to Subject to get notified
        Producer - Something changes here . Producer register Subject class to notify about changes
'''

def test_pattern():
    subject = Subject()
    producer = Producer()
    producer.add_subject(subject)
    observer = ConcreteObserver()
    
    subject.add_observer(observer)

    producer.data_changed('First stream emitted')
    producer.data_changed('Second stream emitted')

    subject.remove_observer(observer)

    observer_second = ConcreteObserverSecond()

    subject.add_observer(observer_second)

    producer.data_changed('Third stream emitted')

    producer.data_changed('Fourth stream emitted')

test_pattern()

