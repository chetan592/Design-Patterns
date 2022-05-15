Replay Subject is special kind of subject. It replays previously emitted values to new subscriber.<br>
Number of values to replay need to specify while creating ReplaySubject as shown below.

<h5>Roles -</h5> 
    <h6>ReplaySubject</h6> - Notifies the all subscribers. Also replay specified number of previously emitted values to new subscribers.<br>
    <h6>Observer</h6> - Register to Subject to get notified.<br>
    <h6>Producer</h6> - Something changes here . Producer register Subject class to notify about changes<br><br>

This is a part of reactive programming.<br>
There is famous library called as <b>rxjs</b> which provides observable functionality that you can use in projects.
