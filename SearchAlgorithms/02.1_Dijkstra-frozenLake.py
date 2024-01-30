#Referência: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

import numpy as np
from config_games import *

#Referência: https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/?ref=lbp

import sys

NO_PARENT = -1
def dijkstra(adjacency_matrix, start_vertex, DEBUG=True):
	n_vertices = len(adjacency_matrix[0])

	# shortest_distances[i] will hold the shortest distance from start_vertex to i
	shortest_distances = [sys.maxsize] * n_vertices

	# added[i] will true if vertex i is included in shortest path tree
	# or shortest distance from start_vertex to i is finalized
	added = [False] * n_vertices

	# Initialize all distances as INFINITE and added[] as false
	for vertex_index in range(n_vertices):
		shortest_distances[vertex_index] = sys.maxsize
		added[vertex_index] = False
		
	# Distance of source vertex from itself is always 0
	shortest_distances[start_vertex] = 0

	# Parent array to store shortest path tree
	parents = [-1] * n_vertices

	# The starting vertex does not have a parent
	parents[start_vertex] = NO_PARENT

	# Find shortest path for all vertices
	for i in range(1, n_vertices):
		# Pick the minimum distance vertex from the set of vertices not yet
		# processed. nearest_vertex is always equal to start_vertex in first iteration.
		nearest_vertex = -1
		shortest_distance = sys.maxsize
		for vertex_index in range(n_vertices):
			if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
				nearest_vertex = vertex_index
				shortest_distance = shortest_distances[vertex_index]

		# Mark the picked vertex as processed
		added[nearest_vertex] = True

		# Update dist value of the adjacent vertices of the picked vertex.
		for vertex_index in range(n_vertices):
			edge_distance = adjacency_matrix[nearest_vertex][vertex_index]
			
			if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
				parents[vertex_index] = nearest_vertex
				shortest_distances[vertex_index] = shortest_distance + edge_distance
	if DEBUG:
		print_solution(start_vertex, shortest_distances, parents)
	
	return start_vertex, shortest_distances, parents

# A utility function to print the constructed distances array and shortest paths
def print_solution(start_vertex, distances, parents):
	n_vertices = len(distances)
	print("Vertex\t Distance\tPath")
	
	for vertex_index in range(n_vertices):
		if vertex_index != start_vertex:
			print("\n", start_vertex, "->", vertex_index, "\t\t", distances[vertex_index], "\t\t", end="")
			print_path(vertex_index, parents)

# Function to print shortest path from source to current_vertex using parents array
def print_path(current_vertex, parents):
	# Base case : Source node has been processed
	if current_vertex == NO_PARENT:
		return
	print_path(parents[current_vertex], parents)
	print(current_vertex, end=" ")

#Sherlon: Adapted Function to get the path from source to target
def get_path(current_vertex, parents):
	global path_1D
	if current_vertex == NO_PARENT:
		return
	path_1D.insert(0, current_vertex)
	get_path(parents[current_vertex], parents)

"""Dado uma matriz de coordenadas 2D, retorna as posições em 1D"""
def get_path_1D(path_2D, m, n):
    path_1D = []
    for coordinates in path_2D:
        i, j = coordinates
        p = i*n+j
        path_1D.append(p)
    return path_1D

#Given a maze + the possible actions, return an adjacency matrix.
def get_adj_matrix(maze, possible_actions):
    grid = np.array(maze)
    #Creating nodes
    nodes = {}
    m,n = grid.shape
    for i in range(m):
        for j in range(n):
            idx  = i*n+j
            node = (i, j)
            nodes[idx] = node
    
    #Creating edges based on actions
    adjMat = np.zeros([m*n, m*n])
    edges = []
    for idx in nodes:
        i, j = nodes.get(idx)

        #Checking Holes for Frozen-Lake
        if grid[i, j] == 1:
            continue

        for action in possible_actions:
            x, y = action
            new_x = i + x
            new_y = j + y
            
            #Checking matrix boundaries
            if (new_x < 0) or (new_x > m-1) or (new_y < 0) or (new_y > n-1):
                continue
            #Checking Holes for Frozen-Lake
            if grid[new_x, new_y] == 1:
                #adjMat[i*n+j, new_x*n+new_y] = -1 #Activate this line to see the "Holes"
                continue
            
            #If everything is ok until now the Edge is created between (i,j) and (new_x, new_y)
            adjMat[i*n+j, new_x*n+new_y] = 1 #The number 1 means that there is a connection of length 1 (All weights are the same, since it is a grid)
            edges.append((i*n+j, new_x*n+new_y))
    return nodes, edges, adjMat

def get_path_2D(path, nodes):
    path_2D = []
    for idx in path:
        path_2D.append(nodes[idx])
    return path_2D

#Set the desired matrix (Grid/Maze), where: 0-Frozen, 1-Hole.
maze = frozen_lake_maps[CURR_MAP].copy() #Get the created map from config_games.py
maze = preprocess_map(maze)  #Get the "0's and 1's" map formatted

#Given a Source, the algorithm in this tutorial finds the short distance to all the other nodes.
#Actions:          ◀️LEFT=0, 🔽DOWN=1, ▶️RIGHT=2, 🔼UP=3
#possible_actions = [(-1, 0),  (0, -1),    (1, 0),   (0, 1)] #Considerando o Plano Cartesiano, com origem (0,0) no centro. (Usado no Frozen Lake)
possible_actions  = [(0, -1),   (1, 0),    (0, 1),   (-1, 0)] #Considerando Matrizes, com origem (0,0) em Cima-Esquerda.
nodes, edges, adjacency_matrix = get_adj_matrix(maze, possible_actions)

m, n = len(maze), len(maze[0]) # Get the map's dimensionality 

#Set the Source (start) and target (end)
source, target = get_start_and_goal(frozen_lake_maps[CURR_MAP].copy(), get_1D=True)

#Execute Dijkstra algorithm to find the shortest-path.
start_vertex, shortest_distances, parents = dijkstra(adjacency_matrix, source, DEBUG=False)

#Caminho em coordenadas (i*y+j)
path_1D = []
get_path(target, parents)
print("Path 1D:", path_1D)

#Caminho em coordenadas (x, y)
path_2D = get_path_2D(path_1D, nodes)
print("Path 2D:", path_2D)

#Movimentos necessários considerando ◀️ LEFT = 0, 🔽 DOWN = 1, ▶️ RIGHT = 2, 🔼 UP = 3
next_moves = get_moves_from_path(path_2D)

#Testa o caminho aprendido com o Dijkstra
render_path_found(next_moves)