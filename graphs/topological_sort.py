from collections import defaultdict

# DAG
# Create a stack to store the nodes.
# Initialize visited array of size N to keep the record of visited nodes.
# Run a loop from 0 till N
#     if the node is not marked True in visited array
#         Call the recursive function for topological sort and perform the following steps.
#             Mark the current node as True in the visited array.
#             Run a loop on all the nodes which has a directed edge to the current node
#                 if the node is not marked True in the visited array:
#                     Recursively call the topological sort function on the node
#             Push the current node in the stack.
# Print all the elements in the stack.


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.v
        stack = []

        for i in range(self.v):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        print(stack[::-1])


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Following is a Topological Sort of the given graph")

    g.topological_sort()
