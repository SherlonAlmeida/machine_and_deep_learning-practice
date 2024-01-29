#Reference: https://www.geeksforgeeks.org/how-to-visualize-a-neural-network-in-python-using-graphviz/
from graphviz import Digraph 
  
# instantiating object 
dot = Digraph(comment='A Round Graph') 
  
# Adding nodes 
dot.node('A', 'Alex') 
dot.node('B', 'Rishu') 
dot.node('C', 'Mohe') 
dot.node('D', 'Satyam') 
  
# Adding edges 
dot.edges(['AB', 'AC', 'AD']) 
dot.edge('B', 'C', constraint = 'false') 
dot.edge('C', 'D', constraint = 'false') 
  
# saving source code 
dot.format = 'png'
dot.render('Graph', view = True)  