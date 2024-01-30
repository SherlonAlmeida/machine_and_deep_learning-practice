import gym

#FROZEN LAKE CONFIG: https://www.gymlibrary.dev/environments/toy_text/frozen_lake/
# Set the input map desired: S=Start, G=Goal, H=Hole, F=Frozen
frozen_lake_maps = {"4x4": ["SFFF",
                            "FHFH",
                            "FFFH",
                            "HFFG"],
                    "3x6": ["HFFFHS",
                            "GFHFHF",
                            "FFHFFF"],
                    "2x8": ["SFFFHHHH",
                            "HHHFFFFG"],
                    "2x3": ["SFF",
                            "FFG"]
                    }
#The global variable that defines the map to be explored
CURR_MAP = "4x4"

"""Dado o mapa no formato de string, identifica as coordenadas do S=start e G=Goal"""
def get_start_and_goal(my_map, get_1D=False):
    m, n = len(my_map[0]), len(my_map[1])
    start = None
    end   = None
    for i, row in enumerate(my_map):
        for j, col in enumerate(my_map[i]):
            if col == "S":
                start = (i, j)
            if col == "G":
                end = (i, j)
    if get_1D:
        Ai, Aj = start
        Bi, Bj = end
        return (Ai*n+Aj, Bi*n+Bj) #Return the Start and End in 1D
    else:
        return start, end  #Return the Start and End in 2D

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


def render_path_found(next_moves):
    my_map = frozen_lake_maps[CURR_MAP] #Get the created map from config_games.py
    env = gym.make('FrozenLake-v1', desc=my_map, is_slippery=False, render_mode="human") # try for different environments
    state, _ = env.reset()

    for t, action in enumerate(next_moves):
        observation, reward, done, info, _ = env.step(action)
        print (t, action, observation, reward, done, info)
        
        if done:
            print("Finished after {} timesteps".format(t+1))
            break