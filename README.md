# WebCalendarApi-Flask-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/170

## Work on project. Stage 3/4: Relax

### Objectives
Create a model to save events to the database. The table should contain the following columns:

- ```id``` of the ```INTEGER``` type. It should be our ```PRIMARY KEY```.
- ```event``` of the ```VARCHAR``` type. It should be ```NOT NULL```.
- ```date``` of the ```DATE``` type. It should be ```NOT NULL```.

You can use any name for your database.

Now your REST API should have the following features:
- ```POST``` request for the /event endpoint should save the event to your database. 
It should require the same arguments as in the previous stage.
- ```GET``` request for the /event endpoint should return all the events from the database.
- ```GET``` request for the /event/today endpoint should return the list of today's events.

#### Examples

##### Example 1: ```GET``` <em>request for the /event endpoint</em>
Response body:
```json
[
   {
      "id":1,
      "event":"Video conference",
      "date":"2021-03-01"
   },
   {
      "id":2,
      "event":"Today's first event",
      "date":"2021-02-28"
   }
]
```

##### Example 2: ```GET``` <em>request for the /event/today endpoint.</em>
Response body:
```json
[
   {
      "id":2,
      "event":"Today's first event",
      "date":"2021-02-28"
   }
]
```
