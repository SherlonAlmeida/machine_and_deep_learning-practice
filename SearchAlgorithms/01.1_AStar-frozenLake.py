#Referência: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

import gym
import numpy as np
from config_games import *

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end, possible_actions):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in possible_actions: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

"""Pré-processa o mapa de entrada para o Frozen-lake para que seja no formato de zeros e uns"""
def preprocess_map(my_map):
    for i, rows in enumerate(my_map):
        my_map[i] = list(my_map[i])
        for j, column in enumerate(my_map[i]):
            if column == "H":
                my_map[i][j] = 1
            else:
                my_map[i][j] = 0
    return my_map

"""Dado uma matriz de coordenadas 2D, retorna as posições em 1D"""
def get_path_1D(path_2D, m, n):
    path_1D = []
    for coordinates in path_2D:
        i, j = coordinates
        p = i*n+j
        path_1D.append(p)
    return path_1D

"""Converte o caminho em movimentos ◀️LEFT=0, 🔽DOWN=1, ▶️RIGHT=2, 🔼UP=3"""
def get_moves_from_path(path_2D):
    moves = []
    for idx in range(len(path_2D)-1):
        curr_state_x, curr_state_y = path_2D[idx]
        next_state_x, next_state_y = path_2D[idx+1]
        if (next_state_x > curr_state_x):
            print("Baixo")
            moves.append(1)
        elif (next_state_x < curr_state_x):
            print("Cima")
            moves.append(3)
        elif (next_state_y > curr_state_y):
            print("Direita")
            moves.append(2)
        elif (next_state_y < curr_state_y):
            print("Esquerda")
            moves.append(0)
    return moves
    

maze = frozen_lake_maps["4x4"].copy() #Get the created map from config_games.py
maze = preprocess_map(maze)  #Get the "0's and 1's" map formatted

#Actions:          ◀️LEFT=0, 🔽DOWN=1, ▶️RIGHT=2, 🔼UP=3
possible_actions = [(-1, 0),  (0, -1),    (1, 0),   (0, 1)]
m, n = len(maze), len(maze[0]) # Get the map's dimensionality 
start = (0, 0)
end = (3, 3)

#Caminho em coordenadas (x, y)
path_2D = astar(maze, start, end, possible_actions)
print(path_2D)

#Caminho em coordenadas (i*y+j)
path_1D = get_path_1D(path_2D, m, n)
print(path_1D)

#Movimentos necessários considerando ◀️ LEFT = 0, 🔽 DOWN = 1, ▶️ RIGHT = 2, 🔼 UP = 3
next_moves = get_moves_from_path(path_2D)

#Testa o caminho aprendido com o A*
my_map = frozen_lake_maps["4x4"] #Get the created map from config_games.py
env = gym.make('FrozenLake-v1', desc=my_map, is_slippery=False, render_mode="human") # try for different environments
state, _ = env.reset()

for t, action in enumerate(next_moves):
    observation, reward, done, info, _ = env.step(action)
    print (t, action, observation, reward, done, info)
    
    if done:
        print("Finished after {} timesteps".format(t+1))
        break