import operator
global priority_reference


priority_reference = {
    "tire": 2,
    "brake light": 5,
    "clutch": 7,
    "transmission": 11,
    "crankshaft": 12,
    "brake": 10,
    "brakes": 10,
    "oil": 4,
    "oil change": 4,
    "shock": 6,
    "shocks": 6,
                    }


def prioritize(issue_list):
    urgency = []
    p = {}
    issues = issue_list
    for issue in issues:
        issue.lower()
        priority_level = 0
        for key in priority_reference:
            if key in issue:
                value = priority_reference.get(key, 0)
                priority_level = priority_level + value
                p[issue] = priority_level
                urgency.append(priority_level)
        p[issue] = priority_level  # put an issue into the list even if it doesn't have a key in it

    urgency.sort()
    sorted_priorities = sorted(p.items(), key=operator.itemgetter(1))
    return sorted_priorities
