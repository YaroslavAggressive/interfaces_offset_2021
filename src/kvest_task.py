from typing import List


class DiGraph:

    """Class with implementation of directed graph as adjacency list"""

    def __init__(self, nodes: List[int], edges: List[List[int]]):
        self.adj_list = {node: [] for node in nodes}
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])


def read_graph(nodes_num: int, edges_lst: List[List[int]]) -> DiGraph:

    """
    Method for building a graph based on incoming data

    Parameters:
    ----------
    nodes_num: int
        Number of nodes in input graph data
    edges_lst: List[List[int]]
        List of edges connecting vertices (maybe not all)

    Returns:
    -------
        Graph-object for input conditions of the problem
    """

    nodes = [i for i in range(nodes_num)]
    graph = DiGraph(nodes, edges_lst)
    # print(graph.adj_list)  # debug output
    return graph


def check_keys(keys_num: int, links: List[List[int]], links_for_check: List[List[int]]) -> List[bool]:

    """
    Kvest problem solution method

    Parameters:
    ----------
    keys_num: int
        Number of keys
    links: List[List[int]]
        Links between keys in kvest
    links_for_check: List[List[int]]
        Connections whose existence needs to be verified

    Returns:
    -------
        List of answers to the question whether the i-th relationship between keys really exists
    """

    result = []
    graph = read_graph(keys_num, links)

    for link in links_for_check:

        if link[0] == link[1]:
            result.append(True)

        visited = set()
        stack = [link[0]]
        appended = False  # flag for addition result of checking path between two nodes

        # finding path by using bfs on each iteration
        while stack:

            curr_node = stack.pop(0)
            if curr_node == link[1] and stack:
                appended = True
                result.append(True)
                break
            if curr_node not in visited:
                visited.add(curr_node)
            for node in graph.adj_list[curr_node]:
                if node not in visited:
                    stack.append(node)

        # checked all nodes and didn't find any pathes from link[0] to link[1]
        if not appended:
            result.append(False)

    return result


print(check_keys(4, [[1, 2], [1, 0], [2, 0], [2, 3]], [[1, 0], [1, 2], [3, 2]]))
