import pytest

import tsp


def test_integration():
    pytest.skip('Not ready yet')
    graph_data = [('A', 'C', 't'), ('A', 'D', 't'), ('D', 'I', 'f'), ('E', 'F', 't'), ('B', 'E', 't'),
                  ('B', 'F', 't'), ('E', 'H', 'f'), ('G', 'H', 't'), ('H', 'I', 't')]

    assert tsp.travel('A', 'B', graph_data) == ['A', 'D', 'I', 'H', 'E', 'B']


def test_simple_train_graph():
    assert (
            tsp.travel('A', 'B', [('A', 'B', 't')]) == ['A', 'B']
    ), 'expected to have picked the only possible destination in ascending order'
