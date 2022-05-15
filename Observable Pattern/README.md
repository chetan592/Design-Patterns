# Observable Patterns
Observables are reactive programming concept. 
There is library called as [rxjs](https://rxjs.dev/) which provides out of the box Observables
implmentation with loads of other type of observables and operators.

## Observable Pattern

Observer desgin pattern to create a system which notifies about changes

### Roles
- **Observable** - Change occurs here for which observers can subscribe to
- **Observer** -   Wants to get notified when change occurs

## Subject Pattern
Observer desgin pattern to create a system which notifies about changes using external Subject class

### Roles
- **Subject** - Notifies the all subscribers
- **Observer** - Register to Subject to get notified
- **Producer** - Something changes here . Producer register Subject class to notify about changes

## Replay Subject Pattern

Replay Subject is special kind of subject.
It replays previously emitted values to new subscriber.
Number of values to replay need to specify while creating ReplaySubject as shown below.

### Roles
- **Replay Subject** - Notifies the all subscribers. Also replay specified number of previously emitted values to new subscribers.
- **Observer** - Register to Subject to get notified.
- **Producer** - Change happens here. Producer uses Subject to notify subscribers about changes.
