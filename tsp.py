import math
from collections import defaultdict


def travel(from_, to, graph_data):
    where = defaultdict(list)

    for start, end, type_ in graph_data:
        where[start].append((end, type_))
        where[end].append((start, type_))

    options = _find_all(from_, to, where)

    if not options:
        raise Exception('did not find any paths :(')

    path_by_flights = defaultdict(list)
    min_flights = math.inf
    for opt in options:
        for num_flights, path in _all_paths_with_flights(_flatten(opt)):
            path_by_flights[num_flights].append(path)

            if num_flights < min_flights:
                min_flights = num_flights

    return list(reversed(min(path_by_flights[min_flights], key=len)))


def _find_all(from_, to, where, visited=None):
    visited = visited or [to]
    path = [to]
    connections = where[to]

    options = []
    for conn in connections:
        if conn[0] in visited:
            continue

        if conn[0] == from_:
            options.append(path + [conn])
            continue  # if it's where we're going from then we've found a full path

        ps = _find_all(from_, conn[0], where, visited + [conn[0]])
        if ps:
            for i, _ in enumerate(ps):
                ps[i][0] = conn

            options.append(path + ps)

    return options


def _flatten(l):
    ret = l

    if isinstance(l, list):
        ret = []
        for i in l:
            ret.append(i)

    return ret


def _all_paths_with_flights(options):
    path = []
    num_flights = 0
    has_returned_subpaths = False

    for node in options:
        if isinstance(node, tuple):
            if node[1] == 'f':
                num_flights += 1
            path.append(node[0])
        elif isinstance(node, list):
            for num, pp in _all_paths_with_flights(node):
                yield num_flights + num, path + pp
                has_returned_subpaths = True
        else:
            path.append(node)

    if not has_returned_subpaths:
        yield num_flights, path
