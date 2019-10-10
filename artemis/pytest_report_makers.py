import ujson as json
import jsondiff


def journeys_diff(ref, output):
    with open(ref) as ref_f, open(output) as output_f:
        ref_json = json.load(ref_f)
        out_json = json.load(output_f)

        ref_journey = ref_json.get('response', {}).get('journeys') or []
        out_journey = out_json.get('response', {}).get('journeys') or []

        if not all((ref_journey,  out_journey)):
            # in case where ref_journey/out_journey is empty, the diff becomes a list, here we build the diff ourselves
            diff = {jsondiff.symbols.insert
                    if not ref_journey
                    else jsondiff.symbols.delete: [[i, j] for i, j in enumerate(out_journey)]}
        else:
            diff = jsondiff.diff(ref_journey, out_journey, syntax='symmetric')

        updated_nb = sum(str(k).isdigit() for k in diff.keys())

        message = (
            "* new journeys nb: {}\n"
            "* discarded journeys nb: {}\n"
            "* updated journeys nb: {}\n"
            "\n<details open><summary>CLICK ME</summary><p>\n"
            "\n```json\n{}\n```\n"
            "\n</p></details>\n"
        ).format(len(diff.get(jsondiff.symbols.insert, [])),
                 len(diff.get(jsondiff.symbols.delete, [])),
                 updated_nb,
                 json.dumps(diff, indent=2))
        return message


def ptref_diff(ref, output):
    return "* ptref diff not yet implemented"


def example_diff(ref, output):
    return "* example diff not yet implemented"
