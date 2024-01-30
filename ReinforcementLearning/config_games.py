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