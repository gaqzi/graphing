import math
from collections import defaultdict


def travel(from_, to, graph_data):
    where = defaultdict(list)

    for start, end, type_ in graph_data:
        where[start].append((end, type_))
        where[end].append((start, type_))

    paths = _find_all_paths(to, from_, where)
    if not paths:
        raise Exception('did not find any paths :(')

    path_by_flights = defaultdict(list)
    min_flights = math.inf
    for path in paths:
        for num_flights, p in _all_paths_with_num_flights(path):
            path_by_flights[num_flights].append(p)
            min_flights = min(num_flights, min_flights)

    return list(min(path_by_flights[min_flights], key=len))


def _find_all_paths(to, from_, where, visited=None):
    visited = visited or [from_]
    path = [from_]
    connections = where[from_]

    options = []
    for conn in connections:
        if conn[0] in visited:
            continue

        if conn[0] == to:
            options.append(path + [conn])
            continue  # if it's where we're going to then we've found a full path

        ps = _find_all_paths(to, conn[0], where, visited + [conn[0]])
        if ps:
            for i, _ in enumerate(ps):
                ps[i][0] = conn  # make sure we store whether flight/train

            options.append(path + ps)

    return options


def _all_paths_with_num_flights(options):
    path = []
    num_flights = 0
    has_returned_subpaths = False

    for node in options:
        if isinstance(node, tuple):
            if node[1] == 'f':
                num_flights += 1
            path.append(node[0])
        elif isinstance(node, list):
            for num, pp in _all_paths_with_num_flights(node):
                yield num_flights + num, path + pp
                has_returned_subpaths = True
        else:
            path.append(node)

    if not has_returned_subpaths:
        yield num_flights, path
