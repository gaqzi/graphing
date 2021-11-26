from collections import defaultdict


def travel(from_, to, graph_data):
    where = defaultdict(list)

    for start, end, type_ in graph_data:
        where[start].append([end, type_])

    path = [to]
    current = to
    while current != from_:
        connection = _connection_for(current, where)
        if connection is None:
            raise f'failed to find a connection to {current}'

        path.append(connection)
        current = connection

    path.reverse()
    return path


def _connection_for(to, where):
    for start, connections in where.items():
        for end, type_ in connections:
            if end == to and type_ != 'f':
                return start

    return None
