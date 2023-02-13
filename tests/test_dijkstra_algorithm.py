import pytest
import example_function.graph.dijkstra_algorithm_function


class TestDijkstraAlgorithm:

    def test_dijkstra_algorithm(self):
        infinity = float("inf")
        data = {
            "graph": {
                "a": {"fin": 1},
                "b": {"a": 3, "fin": 6},
                "fin": {}

            },
            "costs": {
                "a": 6,
                "b": 2,
                "fin": infinity
            },
            "parents": {
                "a": "start",
                "b": "start",
                "in": None
            }
        }

        result = example_function.graph.dijkstra_algorithm_function.DijkstraAlgorithmFunction.run(self, data=data)
        assert result
        assert False
