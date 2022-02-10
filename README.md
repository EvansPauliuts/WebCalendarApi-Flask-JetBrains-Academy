# WebCalendarApi-Flask-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/170

## Work on project. Stage 2/4: GET vs POST

### Objectives
Create a resource that handles ```POST``` requests for the <em>/event</em>, endpoint. 
It must require the following arguments in the request body:

- An ```event``` argument of the ```str``` type. If this argument is missing, please, 
respond with the following error message: ```The event name is required!```
- A ```date``` argument of the ```inputs.date``` type. If this argument is missing or it has the wrong format, 
please, respond with the following error message: ```The event date with the correct format is required!
The correct format is YYYY-MM-DD!```

If a user sends the correct response, display the following message:
```The event has been added!```, and show the user data:

```json
{
    "message": "The event has been added!",
    "event": "Client event name",
    "date": "Client date"
}
```

#### Examples

##### Example 1: Wrong ```POST``` <em>request for the /event endpoint</em>
Request body:
```json
{
    "date": "2021-02-10"
}
```
Response body:
```json
{
    "message": {
        "event": "The event name is required!"
    }
}
```

##### Example 2: Wrong ```POST``` <em>request for the /event endpoint</em>
Request body:
```json
{
    "event": "Video conference",
}
```
Response body:
```json
{
    "message": {
        "date": "The event date with the correct format is required! The correct format is YYYY-MM-DD!"
    }
}
```

##### Example 3: A correct ```POST``` <em>request for the /event endpoint</em>
Request body:
```json
{
    "event": "Video conference",
    "date": "2020-11-15"
}
```
Response body:
```json
{
    "message": "The event has been added!",
    "event": "Video conference",
    "date": "2020-11-15"
}
```
