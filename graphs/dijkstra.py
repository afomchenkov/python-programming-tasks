from collections import namedtuple, defaultdict
import heapq
from mimetypes import init

"""
Given a list of edges (a, b, t), where t - time/weight between nodes a and b, determine how long it'll
take for every node to receive a message that begins at node 0.

Dijkstra's algorithm calculates the shortest path between two vertices of a DAG with all positive weights of the edges.
It works by repeatedly travelling to the closest vertex which has not yet been reached.
"""

Edge = namedtuple("Edge", ("start", "end", "time"))


class Graph:
    def __init__(self, N: int, edges: list[Edge]) -> None:
        self.vertices = range(N + 1)
        self.edges = edges
        self.table = self.init_graph()

    def init_graph(self) -> dict:
        graph = {v: [] for v in self.vertices}
        for edge in self.edges:
            graph[edge.start].append((edge.end, edge.time))

        return graph


# Time complexity: O(n^2)
def propagate(graph: dict) -> int:
    times = {node: float('inf') for node in graph}
    times[0] = 0

    q = list(graph)
    while q:
        u = min(q, key=lambda x: times[x])
        q.remove(u)
        for v, time in graph[u]:
            times[v] = min(times[v], times[u] + time)

    # print(times)
    return max(times.values())


# Time complexity: O(E + VlogV)
def propagate_heap(graph: dict) -> int:
    times = {}

    q = [(0, 0)]
    while q:
        u, node = heapq.heappop(q)
        if node not in times:
            times[node] = u
            for neighbour, v in graph[node]:
                if neighbour not in times:
                    heapq.heappush(q, (u + v, neighbour))

    print(times)
    return max(times.values())


if __name__ == '__main__':
    graph_data = [
        Edge(0, 1, 5),
        Edge(0, 2, 3),
        Edge(0, 5, 4),
        Edge(1, 3, 8),
        Edge(2, 3, 1),
        Edge(3, 5, 10),
        Edge(3, 4, 5),
    ]
    graph = Graph(N=5, edges=graph_data)
    # print(graph.table)

    # result = propagate(graph.table)
    result = propagate_heap(graph.table)
    print(result)
    # Resulted path is 9: 0(w3) -> 2(w1)-> 3(w5) -> 4

    pass
