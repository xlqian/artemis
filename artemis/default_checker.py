from functools import partial

from flask_restful import fields
from artemis.utils import (
    Checker,
    WhiteListMask,
    BlackListMask,
    SubsetComparator,
    RetrocompatibilityMask,
    StopScheduleIDGenerator,
    PerfectComparator,
)
import re

"""
The default behaviour for journeys is to check only a subset journey

the mask create a new dict filtering only the wanted elt
"""
fare = {
    "total": fields.Raw(attribute="total.value"),
    "currency": fields.Raw(attribute="total.currency"),
}

distances = {
    "bike": fields.Raw,
    "car": fields.Raw,
    "walking": fields.Raw,
    "taxi": fields.Raw,
}

durations = {
    "bike": fields.Raw,
    "car": fields.Raw,
    "total": fields.Raw,
    "walking": fields.Raw,
    "taxi": fields.Raw,
}

section = {
    "duration": fields.Raw,
    "departure_date_time": fields.Raw,
    "arrival_date_time": fields.Raw,
    "from": fields.Raw(attribute="from.name"),
    "to": fields.Raw(attribute="to.name"),
    "type": fields.Raw,
}

journey = {
    "duration": fields.Raw,
    "nb_transfers": fields.Raw,
    "departure_date_time": fields.Raw,
    "arrival_date_time": fields.Raw,
    "distances": fields.Nested(distances),
    "durations": fields.Nested(durations),
    "sections": fields.List(fields.Nested(section)),
    "type": fields.Raw,
    "fare": fields.Nested(fare),
}

error = {"id": fields.Raw, "message": fields.Raw}

cost = {"currency": fields.Raw, "value": fields.Raw}

ticket = {
    "comment": fields.Raw,
    "name": fields.Raw,
    "cost": fields.Nested(cost),
    "found": fields.Raw,
    "source_id": fields.Raw,
}

severity = {"name": fields.Raw, "effect": fields.Raw}

pt_object = {"name": fields.Raw, "embedded_type": fields.Raw}

stop_point = {"name": fields.Raw}

impacted_stop = {
    "arrival_status": fields.Raw,
    "departure_status": fields.Raw,
    "stop_point": fields.Nested(stop_point),
}

impacted_object = {
    "pt_object": fields.Nested(pt_object),
    # Currently no need for impacted_section in the response. Un-comment if needed one day and blame Big M!
    # "impacted_section": fields.Nested(section),
    "impacted_stops": fields.List(fields.Nested(impacted_stop)),
}

disruption = {
    "status": fields.Raw,
    "contributor": fields.Raw,
    "severity": fields.Nested(severity),
    "impacted_objects": fields.List(fields.Nested(impacted_object)),
}

default_journey_checker = Checker(
    filters=[
        WhiteListMask(
            mask={
                "journeys": fields.List(fields.Nested(journey)),
                "error": fields.Nested(error),
                "tickets": fields.List(fields.Nested(ticket)),
                "disruptions": fields.List(fields.Nested(disruption)),
            }
        )
    ]
)


# we don't want full urls in the response, since it will change depending on where the test in run
# so we remove the server address
def replace_hyperlink(text):
    return re.sub(r"http://.+?/v1/(.*?)/?$", r"http://SERVER_ADDR/v1/\1", text)


def nullify_elem(x):
    return None


# Note: two dots between '$' and 'disruptions[*]' will match ALL (even nested) disruptions under root
DEFAULT_BLACKLIST_MASK = (
    ("$..disruptions[*].disruption_uri", nullify_elem),
    ("$..disruptions[*].disruption_id", nullify_elem),
    ("$..disruptions[*].impact_id", nullify_elem),
    ("$..disruptions[*].uri", nullify_elem),
    ("$..disruptions[*].id", nullify_elem),
    ("$..disruptions[*].updated_at", nullify_elem),
    ("$..journeys[*].sections[*].id", nullify_elem),
    ("$..href", replace_hyperlink),
    ("$.context.current_datetime", nullify_elem),
)

JOURNEY_MASK = (
    ("$.links", partial(sorted, key=lambda x: x.get("href"))),
    # we consider that the admins list are not ordered
    ("$..administrative_regions", partial(sorted, key=lambda x: x.get("id"))),
)

default_checker = Checker(
    filters=[RetrocompatibilityMask(), BlackListMask(DEFAULT_BLACKLIST_MASK)],
    comparator=SubsetComparator(),
)

# for journeys we don't want to sort the lists
journeys_retrocompatibility_checker = Checker(
    filters=[BlackListMask(DEFAULT_BLACKLIST_MASK), BlackListMask(JOURNEY_MASK)],
    comparator=PerfectComparator(),
)

stop_schedule_checker = Checker(
    filters=[
        StopScheduleIDGenerator(),
        RetrocompatibilityMask(),
        BlackListMask(DEFAULT_BLACKLIST_MASK),
    ],
    comparator=SubsetComparator(),
)
