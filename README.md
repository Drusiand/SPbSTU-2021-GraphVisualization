# Graph visualization

This is a simple student project designed for visualization deep-first search (DFS) and breadth-first search (BFS) algorithms (currently using matploib). Output data is stored in gif-files with corresponding names. Examples are represented in "gif" directory.


## Installation

To make the program work properly, you will have install third-party dependedencies via typing  
```  
code pip install -r requirements.txt  
```  
in terminal.


## Results

### Visualization of BFS algorithm:
![alt-текст](https://github.com/Drusiand/SPbSTU-2021-GraphVisualization/blob/main/gif/graph3_bfs.gif)

### Visualization of dFS algorithm:
![alt-текст](https://github.com/Drusiand/SPbSTU-2021-GraphVisualization/blob/main/gif/graph3_dfs.gif)


## Usage exmples
### graph1.txt
```
3: 4,8
1: 2,4,5,6
5: 6,8
4: 7,8
6: 7,8
7: 8
2: 3

```
Note:  
- 1st node (in that case node with value "3") will be the begining for DFS and BFS algorithms;  
- Source files have to be stored in "graph" directory


### Building a graph
```python
from python.custom_graph import custom_graph
graph = custom_graph("graph1.txt")
```

### Drawing graph
```python
from python.custom_graph import custom_graph
# ...
# building graph...
# ...
graph.draw()
```

### Building gif-files
```python
from python.custom_graph import custom_graph
# ...
# building graph...
# ...
graph.build_gif("bfs", "dfs")  # build gif for both DFS and BFS algorithms
```
