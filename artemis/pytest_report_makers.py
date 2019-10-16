import ujson as json
import jsondiff
import os
from artemis.configuration_manager import config
import logging

def journeys_diff(ref_dict, resp_dict):
    log = logging.getLogger(__name__)

    ref_journeys = ref_dict.get('journeys', []) 
    resp_journeys = resp_dict.get('journeys', [])

    if not all((ref_journeys,  resp_journeys)):
        # in case where ref_journey/resp_journey is empty, the diff becomes a list, here we build the diff ourselves
        diff = {jsondiff.symbols.insert
                if not ref_journeys
                else jsondiff.symbols.delete: [[i, j] for i, j in enumerate(resp_journeys)]}
    else:
        diff = jsondiff.diff(ref_journeys, resp_journeys, syntax='symmetric')

    updated_nb = sum(str(k).isdigit() for k in diff.keys())

    message = (
        "* new journeys nb: {}\n"
        "* discarded journeys nb: {}\n"
        "* updated journeys nb: {}\n"
        "<details open><summary>CLICK ME</summary><p>\n"
        "```json\n"
        "{}\n"
        "```\n"
        "</p></details>\n"
    ).format(len(diff.get(jsondiff.symbols.insert, [])),
                len(diff.get(jsondiff.symbols.delete, [])),
                updated_nb,
                json.dumps(diff, indent=2)
                )
    return message

        #"\n\n"

def add_to_report(test_name, test_query, report_message):
    failures_report_path = os.path.join(config['RESPONSE_FILE_PATH'], "failures_report.md")

    reading_mode = "a" if os.path.exists(failures_report_path) else "w"
    with open(failures_report_path, reading_mode) as failures_report:
        failures_report.write("## {}\n".format(test_name))
        failures_report.write("[query]({}) | [open old]({})  |  [open new]({})\n"
                                .format(test_query,
                                        'http://canaltp.github.io/navitia-playground/file.html',
                                        'http://canaltp.github.io/navitia-playground/file.html')
                                )
        failures_report.write("{}\n".format(report_message))

