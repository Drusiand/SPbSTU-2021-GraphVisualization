import networkx as nx
from python.file_reader import file_reader

__token_delimiter = ","
__node_edges_delimiter = ":"

_wrong_input_errmsg = "ERROR: wrong input file"


def parse_graph(source: str):
    """

    Parsing graph from txt-file

    Parameters
    ----------
    source: str
            name of desired txt-file

    Returns
    ----------
    parsed_graph:   dict
                    graph represented by dictionary {node: edges}

    """
    parsed_graph = dict()
    with file_reader(source) as raw_graph:
        if raw_graph is not None:
            for line in raw_graph.readlines():
                tmp_node_edge_container = line.split(__node_edges_delimiter)
                if len(tmp_node_edge_container) != 2:
                    print(_wrong_input_errmsg)
                    return None
                node, raw_edges = tmp_node_edge_container
                parsed_graph.update({node.strip(): [edge for edge in raw_edges.strip().split(__token_delimiter)]})
        else:
            return None
    return parsed_graph


def build_graph(source: str):
    """

    Build networkx.Graph by txt-file

    Parameters
    ----------
    source: str
            name of desired txt-file

    Returns
    ----------
    graph:  networkx.Graph
            new networkx.Graph instance built from txt-file

    """
    graph_dict = parse_graph(source)
    if graph_dict is None:
        return None
    graph = nx.Graph()
    graph.add_nodes_from(graph_dict.keys())
    graph_edges = list()
    for key in graph_dict.keys():
        for node in graph_dict.get(key):
            graph_edges.append((key, node))
    graph.add_edges_from(graph_edges)

    return graph
