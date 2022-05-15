from producer import Producer
from replay_subject import ReplaySubject
from observer import ConcreteObserver, ConcreteObserverSecond, ConcreteObserverThird


'''
    Replay Subject is special kind of subject. It replays previously emitted values to new subscriber.
    Number of values to replay need to specify while creating ReplaySubject as shown below.

    Roles - 
        ReplaySubject - Notifies the all subscribers. Also replay specified number of previously emitted values to new subscribers.
        Observer - Register to Subject to get notified
        Producer - Something changes here . Producer register Subject class to notify about changes

    This is a part of reactive programming. There is famous library rxjs which provides observable functionality.

'''

def test_pattern():
    producer = Producer()
    subject = ReplaySubject(2)
    producer.add_subject(subject)
    observer = ConcreteObserver()

    subject.add_observer(observer)

    producer.changed('First value emitted')
    producer.changed('Second value emitted')
    producer.changed('Third value emitted')
    

    observer_second = ConcreteObserverSecond()

    subject.add_observer(observer_second)
    
    producer.changed('Fourth value emitted')
    producer.changed('Fifth value emitted')
   
    observer_third = ConcreteObserverThird()

    subject.add_observer(observer_third)

test_pattern()
