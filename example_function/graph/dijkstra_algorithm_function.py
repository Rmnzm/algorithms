class DijkstraAlgorithmFunction:
    processed = []

    def find_lowest_cost_node(self, costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def run(self, data: dict):
        costs = data['costs']
        graph = data['graph']
        parents = data['parents']
        node = self.find_lowest_cost_node(costs)
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node(costs)

