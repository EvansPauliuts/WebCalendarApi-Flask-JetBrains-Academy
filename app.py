import sys
import datetime

from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')
}

parser.add_argument(
    'event',
    type=str,
    help='The event name is required!',
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True
)


class EventDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        get_id = EventDate.query.filter(EventDate.id == id).first()

        if get_id is None:
            abort(404, 'The event doesn\'t exist!')
        return get_id

    def delete(self, id):
        get_delete = EventDate.query.filter(EventDate.id == id).first()

        if get_delete is None:
            abort(404, 'The event doesn\'t exist!')

        EventDate.query.filter_by(id=id).delete()
        db.session.commit()

        return {'message': 'The event has been deleted!'}


class GetEventToday(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return EventDate.query.filter(EventDate.date == datetime.date.today()).all()


class EventToday(Resource):
    @marshal_with(resource_fields)
    def get(self):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')

        if start_time and end_time:
            events = EventDate.query.filter(EventDate.date >= start_time).filter(EventDate.date <= end_time).all()
            if len(events) < 1:
                abort(404, {'message': 'The event doesn\'t exist!'})
            return events
        return EventDate.query.all()

    def post(self):
        args = parser.parse_args()

        event = args['event']
        date = args['date'].date()
        message = 'The event has been added!'

        new_event = EventDate(event=event, date=date)
        db.session.add(new_event)
        db.session.commit()

        data_event = {
            'message': message,
            'event': event,
            'date': str(date)
        }

        return data_event


api.add_resource(EventToday, '/event')
api.add_resource(GetEventToday, '/event/today')
api.add_resource(EventByID, '/event/<int:id>')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
