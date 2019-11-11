import pydot
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
(graph,) = pydot.graph_from_dot_file('LoginModelFSM.dot')

graph.write_png('LoginModelFSM.png')
