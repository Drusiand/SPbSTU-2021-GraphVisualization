import functools

from python.graph_parser import build_graph
from python.graph_drawer import draw_graph, draw_gif

_wrong_descriptor_errmsg = "\nERROR: wrong descriptor"
_invalid_graph_errmsg = "\nERROR: invalid graph"


def handle_errors(logged_method):
    """
    Handle errors in case graph was not instantiated

    Parameters
    ----------
    logged_method:  function
                    custom_graph method that need s to be handled

    Returns
    ----------
    result of correct method (if no error was detected) or None

    """
    @functools.wraps(logged_method)
    def inner(self, *args, **kwargs):
        try:
            assert self._graph is not None
        except AssertionError:
            print(_invalid_graph_errmsg)
            return
        logged_method(self, *args, **kwargs)

    return inner


class custom_graph:
    """

    Custom class for keeping graph

    Attributes
    ----------
    __gif_output_dir:   str
                        directory to output gif-files with algorithm visualization

    __graph_input_dir:  str
                        directory for input txt-files with graph data

    __gif_dfs_ending:   str
                        postfix for gif-files with visualization of DFS algorithm

    __gif_bfs_ending:   str
                        postfix for gif-files with visualization of DFS algorithm

    __draw_success: bool
                    flag of successful graph drawing

    __gif_success:  bool
                    flag of successful gif saving

    _graph: networkx.Graph
            instance of networkx.Graph for keeping graph data

    Methods
    ----------
    draw(show=True)
                    draw graph with matplolib.pyplot

    build_gif(*routes)
                    build gif-files with visualization of algorithms in "routes"

    get_graph()
                    getter for _graph field

    is_drawn_successfully():
                    getter for __draw_success field

    is_gif_built_successfully()
                    getter for __gif_success field

    """
    __gif_output_dir = "../gif/"
    __graph_input_dir = "../graph/"
    __gif_dfs_ending = "_dfs.gif"
    __gif_bfs_ending = "_bfs.gif"
    __draw_success = False
    __gif_success = False
    _graph = None

    def __init__(self, source: str, descriptor="custom_txt"):
        self.__source = source
        if descriptor == "custom_txt":
            self._graph = build_graph(self.__graph_input_dir + source)
            if self._graph is None:
                return
        # elif:
        #   build graph other ways..
        else:
            self._graph = None
            print(_wrong_descriptor_errmsg)
            return
        self.__start = list(self._graph.nodes)[0]
        self.__unit_name = self.__source.split(".")[0]
        self.__gif_dfs_name = self.__gif_output_dir + self.__unit_name + self.__gif_dfs_ending
        self.__gif_bfs_name = self.__gif_output_dir + self.__unit_name + self.__gif_bfs_ending
        print(self.__source)

    @handle_errors
    def draw(self, show=True):
        """

        Drawing graph with matplolib.pyplot

        Parameters
        ----------
        show:   bool, optional, default=True
                flag for showing or not graph plot in figure


        """
        self.__draw_success = draw_graph(self._graph, show=show)
        # return draw_graph(self._graph, show=show)

    @handle_errors
    def build_gif(self, *routes: str):
        """

        Build gif-files with visualization of algorithms in "routes"

        Parameters
        ----------
        routes: array-like of strings
                defines what algorithms are desired to be visualized

        """
        desired_routes = list()
        for route in routes:
            if route in self.__gif_dfs_name:
                desired_routes.append(self.__gif_dfs_name)
            if route in self.__gif_bfs_name:
                desired_routes.append(self.__gif_bfs_name)
        self.__gif_success = draw_gif(self._graph, self.__start, desired_routes)

    def get_graph(self):
        """

        Getter for _graph field

        """
        return self._graph

    def is_drawn_successfully(self):
        """

                Check if graph was successfully drawn

        """
        return self.__draw_success

    def is_gif_built_successfully(self):
        """

                Check if gif was successfully built

        """
        return self.__gif_success
