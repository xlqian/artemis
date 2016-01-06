from flask.ext.restful import fields
from artemis.utils import Checker, WhiteListMask

"""
The default behaviour for journeys is to check only a subset journey

the mask create a new dict filtering only the wanted elt
"""


section = {
    "duration": fields.Raw,
    "departure_date_time": fields.Raw,
    "arrival_date_time": fields.Raw,
    'from': fields.Raw(attribute='from.name'),
    'to': fields.Raw(attribute='to.name'),
    'type': fields.Raw,
}

journey = {
    'duration': fields.Raw,
    'nb_transfers': fields.Raw,
    'departure_date_time': fields.Raw,
    'arrival_date_time': fields.Raw,
    'sections': fields.List(fields.Nested(section)),
    'type': fields.Raw,
}

default_journey_checker = Checker(filter=WhiteListMask(mask={
    "journeys": fields.List(fields.Nested(journey))
}))

