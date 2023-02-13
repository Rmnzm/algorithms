from functions.search.dijkstra_algorithm_function import Graph, dijkstra_algorithm, print_result


def test_dijkstra():
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    graph = Graph(nodes, init_graph)

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")

    result = print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")

    assert 'Найден следующий лучший маршрут с ценностью 11.' in result
    assert 'Reykjavik -> Oslo -> Berlin -> Rome -> Athens -> Belgrade' in result
