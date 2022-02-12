# WebCalendarApi-Flask-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/170

## Work on project. Stage 4/4: Back to the future

### Objectives
In this stage, add a resource with the /event/<int:id> URL. It should handle the following requests:

- A ```GET``` request should return the event with the ID in JSON format. If an event doesn't exist, 
return ```404``` with the following message: ```The event doesn't exist!```.
- A ```DELETE``` request should delete the event with the given ID and respond with the following response body:
```json
{
    "message": "The event has been deleted!"
}
```
If the event with the ID doesn't exist, return ```404``` with the message ```The event doesn't exist!```
- A ```GET``` request for the /event endpoint with ```start_time``` and ```end_time``` parameters should 
return a list of events for the given time range. If the arguments are missing,
return the list of all events.
- The URLs from the previous stage should work in the same way.

#### Examples

##### Example 1: ```GET``` <em>request for the /event?start_time=2020-10-10&end_time=2020-10-20 endpoint</em>
Response body:
```json
[
   {
      "id":1,
      "event":"Video conference",
      "date":"2020-10-15"
   },
   {
      "id":2,
      "event":"Today's first event",
      "date":"2020-10-20"
   }
]
```

##### Example 2: ```GET``` <em>request for the /event/1 endpoint</em>
Response body:
```json
{
    "id":1,
    "event":"Video conference",
    "date":"2020-10-15"
}
```

##### Example 3: ```GET``` <em>request for the /event/10 endpoint</em>
Response body:
```json
{
    "message": "The event doesn't exist!"
}
```

##### Example 4: ```DELETE``` <em>request for the /event/1 endpoint</em>
Response body:
```json
{
    "message": "The event has been deleted!"
}
```

##### Example 5: ```DELETE``` <em>request for the /event/10 endpoint</em>
Response body:
```json
{
    "message": "The event doesn't exist!"
}
```
