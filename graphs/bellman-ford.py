from functools import lru_cache
from itertools import groupby
from math import log

"""
The Bellman-Ford algorithm is commonly used to find the shortest path between a source vertex and
each other vertices. If the graph contains a negative cycle, throw an exception (return True).

Example task: gievn a table of currency exchange rates, determine wheter there is a possible
arbitrage opportunity (find out if there is some sequence, starting with some amount X and ending with amount greater than X).
"""

# Time complexity: O(N^3)
def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False

if __name__ == '__main__':
    graph = {
        "USD": {"GBP": 0.77, "INR": 71.71, "EUR": 0.87},
        "GBP": {"USD": 1.30, "INR": 93.55, "EUR": 1.14},
        "INR": {"USD": 0.014, "GBP": 0.011, "EUR": 0.012},
        "EUR": {"USD": 1.14, "GBP": 0.88, "INR": 81.95}
    }
    result = arbitrage(graph)
    print(result)
