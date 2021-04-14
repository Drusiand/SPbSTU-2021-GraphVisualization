import matplotlib.pyplot as plt
import networkx as nx
from celluloid import Camera
from python.graph_search import DFS, BFS

__draw_options = {
    "alpha": 0.8,
    "width": 3,
    "node_size": 700,
    "font_size": "15",
    "font_weight": "bold"
}

__graph_layout = nx.planar_layout
__default_node_color = "red"
__step_node_color = "blue"
__animation_delay = 1000
__bfs_descriptor = "bfs"
__dfs_descriptor = "dfs"
__walk_function_errmsg = "\nERROR: wrong walk_function descriptors"


def draw_graph(graph: nx.Graph, color_map_node=None, show: bool = True):
    """

    Drawing graph with matplotlib.pyplot with specified node color map

    Parameters
    ----------
    graph:  networkx.Graph
            a graph to draw

    color_map_node: list, optional, default=None
                    defines a color map for algorithm visualization

    show:   bool, optional, default=True
            flag for showing or not graph plot in figure

    Returns
    ----------
    True in case of successful drawing, false otherwise

    """
    plt.gcf().number = 0
    figures_before_drawing = plt.gcf().number  # get number of already drawn figures BEFORE drawing the graph itself
    nx.draw(graph, node_color=color_map_node, pos=__graph_layout(graph),
            with_labels=True,
            **__draw_options)
    if show:
        plt.show()
    else:
        plt.gcf().number += 1
    figures_after_drawing = plt.gcf().number  # get number of already drawn figures AFTER drawing the graph itself
    return True if figures_after_drawing > figures_before_drawing else False


def build_gif(graph: nx.Graph, color_order: list, gif_name: str):
    """
        Build a single gif-file with visualization of certain route

        Parameters
        ----------
        graph:  networkx.Graph
                a graph to build gif from

        color_order:    list
                        list of colours that defines visualized route

        gif_name:   str
                    name of gif-file

        Returns
        ----------
        True in case of successful gif build, false otherwise

    """
    color_map_node = list()
    for i in range(graph.number_of_nodes()):
        color_map_node.append(__default_node_color)

    fig = plt.figure()
    camera = Camera(fig)
    success_plot_list = list()

    for i in color_order:
        if i != -1:
            color_map_node[i] = __step_node_color
        success_plot_list.append(draw_graph(graph, color_map_node=color_map_node, show=False))
        camera.snap()
    if None or False in success_plot_list:  # check if all frames of gif were successfully drawn
        return False
    animation = camera.animate(interval=__animation_delay)
    animation.save(gif_name)
    return True


def get_color_sequence(graph_nodes: list, route: list):
    """

    Get color sequence that represents a certain route

    Parameters
    ----------
    graph_nodes:    list
                    list of graph nodes

    route:  list
            visualized algorithm route

    Returns
    ----------
    route_color order:  list
                        list of colors that defines visualized route

    """
    route_color_order = list()
    for route_node in route:
        count = 0
        for graph_node in graph_nodes:
            if graph_node == route_node:
                route_color_order.append(count)
                break
            count += 1
    return route_color_order


def draw_gif(graph: nx.Graph, start: str, gif_names: list or str):
    """

    Build gif-files with visualization or desired routes

    Parameters
    ----------
    graph:  networkx.Graph
            a graph to build gifs from

    start:  str
            beginning node of the algorithm

    gif_names:  list or str
                name of gif-files to save; also define desired route algorithms

    Returns
    ----------
    True in case of successful gifs build, false otherwise

    """
    walk_functions = dict()
    for gif_name in gif_names:
        if __bfs_descriptor in gif_name:
            walk_functions.update({BFS: gif_name})
            continue
        elif __dfs_descriptor in gif_name:
            walk_functions.update({DFS: gif_name})
            continue
    try:
        assert walk_functions != {}
    except AssertionError:
        print(__walk_function_errmsg)
        return

    success_gif_list = list()
    for walk_function in walk_functions.keys():
        route_color_order = [-1]  # add -1 to color order for drawing original graph in 1'st frame of gif
        route_color_order.extend(get_color_sequence(list(graph.nodes), walk_function(graph, start)))
        success_gif_list.append(build_gif(graph, route_color_order, walk_functions.get(walk_function)))
    if None or False in success_gif_list:
        return False
    return True
