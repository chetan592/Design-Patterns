
from observable import ConcreteObservable
from observer import ConcreteObserver, ConcreteObserverSecond

'''
    Observer desgin pattern to create a system which notifies about changes

    Roles - 
        Observable - Change occurs here for which observers can subscribe to
        Observer - Wants to get notified when change occurs

'''

def test_pattern():
    observer = ConcreteObserver()

    observable = ConcreteObservable()

    observable.add_observer(observer)

    observable.changed('First stream emitted')

    observer_second = ConcreteObserverSecond()

    observable.add_observer(observer_second)

    observable.changed('Second stream emitted')

    observable.remove_observer(observer)

    observable.changed('Third stream emitted')


test_pattern()