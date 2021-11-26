import pytest

import tsp


def test_integration():
    graph_data = [('A', 'C', 't'), ('A', 'D', 't'), ('D', 'I', 'f'), ('E', 'F', 't'), ('B', 'E', 't'),
                  ('B', 'F', 't'), ('E', 'H', 'f'), ('G', 'H', 't'), ('H', 'I', 't')]

    assert tsp.travel('A', 'B', graph_data) == ['A', 'D', 'I', 'H', 'E', 'B']


def test_simple_train_graph():
    assert (
            tsp.travel('A', 'B', [('A', 'B', 't')]) == ['A', 'B']
    ), 'expected to have picked the only possible destination in ascending order'


def test_three_node_graph():
    assert (
            tsp.travel('A', 'C', [('A', 'B', 't'), ('B', 'C', 't')]) == ['A', 'B', 'C']
    ), 'expected to have traveled to C through B'


def test_no_path():
    with pytest.raises(Exception, match='did not find any paths'):
        tsp.travel('A', 'C', [('A', 'B', 't'), ('D', 'C', 't')])


def test_three_node_graph_eschewing_flight_for_train():
    assert (
            tsp.travel('A', 'C', [('A', 'C', 'f'), ('A', 'B', 't'), ('B', 'C', 't')]) == ['A', 'B', 'C']
    ), 'expected to have traveled to C through B because there is a train only path'


def test_three_node_graph_where_flight_required():
    assert (
            tsp.travel('A', 'C', [('A', 'B', 't'), ('B', 'C', 'f')]) == ['A', 'B', 'C']
    ), 'expected to have traveled to C through B with a flight'


def test_four_node_graph_where_flight_required_from_one():
    assert (
            tsp.travel(
                from_='H',
                to='B',
                graph_data=[
                    ('E', 'F', 't'), ('B', 'E', 't'),
                    ('B', 'F', 't'), ('E', 'H', 'f')
                ]
            ) == ['H', 'E', 'B']
    ), 'expected to have traveled to D through B since it is the only one with a connection'
