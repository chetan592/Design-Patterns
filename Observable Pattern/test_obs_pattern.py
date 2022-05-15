from subject import Subject
from observer import Observer,ObserverSecond
from producer import Producer

'''
    Observer desgin pattern to create a system to notify about changes

    Roles - 
        Subject - Notifies the all subscribers
        Observer - Register to Subject to get notified
        Producer - Something changes here . Producer register Subject class to notify about changes
'''

def test_pattern():
    subject = Subject()
    producer = Producer(subject)
    observable = Observer()
    
    subject.add_observer(observable)


    producer.data_changed('First stream emitted')
    producer.data_changed('Second stream emitted')
    producer.data_changed('Third stream emitted')

    observable_second = ObserverSecond()

    subject.add_observer(observable_second)

    producer.data_changed('Fourth stream emitted')

test_pattern()

