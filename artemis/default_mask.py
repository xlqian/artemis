from flask.ext.restful import fields

"""
The default behaviour for journeys is to check only a subset

the mask create a new dict filtering only the wanted elt
"""

section = {
    "duration": fields.Raw,
    "departure_date_time": fields.Raw,
    "arrival_date_time": fields.Raw,
}

journey = {
    'duration': fields.Raw,
    'nb_transfers': fields.Raw,
    'departure_date_time': fields.Raw,
    'arrival_date_time': fields.Raw,
    'sections': fields.List(fields.Nested(section)),
    'from': fields.Raw,
    'to': fields.Raw,
    'type': fields.Raw,
    'tags': fields.List(fields.Raw),
}

default_journey_mask = {
    "journeys": fields.List(fields.Nested(journey)),
}

