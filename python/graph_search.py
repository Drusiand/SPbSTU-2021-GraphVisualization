import networkx as nx


def DFS(graph: nx.Graph, start: str, visited: list = None):
    """

    Realization of depth-first search (DFS) algorithm

    Parameters:
    ----------
    graph:  networkx:Graph
            original graph

    start:  str
            beginning node of the algorithm

    visited:    list, optional, default=None
                list of visited nodes

    Returns
    ----------
    visited:    list
                route of DFS

    """
    if visited is None:
        visited = list()
    if start in visited:
        return visited
    visited.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            visited = DFS(graph, neighbor, visited)
    return visited


def BFS(graph: nx.Graph, start: str, visited: list = None, bfs_order: list = None, queue: list = None):
    """

        Realization of breadth-first search (BFS) algorithm

        Parameters:
        ----------
        graph:  networkx:Graph
                original graph

        start:  str
                beginning node of the algorithm

        visited:    list, optional, default=None
                    list of visited nodes

        bfs_order:  list, optional, default=None
                    future route of BFS

        queue:  list, optional, default=None
                queue of temporary nodes

        Returns
        ----------
        bfs_order:  list
                    route of BFS

        """
    if visited is None:
        visited = list()
    if queue is None:
        queue = list()
    if bfs_order is None:
        bfs_order = list()
    if start in visited:
        return bfs_order
    visited.append(start)
    bfs_order.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            queue.append(neighbor)
    while queue:
        BFS(graph, queue.pop(0), visited, bfs_order, queue)
    return bfs_order
