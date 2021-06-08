from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from puzzle import Puzzle


state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5],
        
        [0, 1, 2,
        3, 4, 5,
        6, 7, 8],

       [1, 2, 0,
        3, 4, 5,
        6, 7, 8],

        [1, 4, 2,
        3, 5, 8,
        6, 0, 7],
        
        [5, 2, 8,
        4, 1, 7,
        0, 3, 6]]

# Setar objetivo de cada puzzle
goal = [
        [1,2,3,8,0,4,7,6,5],
        [1,2,3,8,0,4,7,6,5],
        [1,2,3,8,0,4,7,6,5],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,5,6,7,8]
]

for i in range(0,7):
    Puzzle.goal_state = goal[i]
    Puzzle.num_of_instances=0
    t0=time()
    breadth_first_search(state[i])
    t1=time()-t0
    print('BFS:')
    print('instancias visitadas:',Puzzle.num_of_instances)
    print('tempo:',t1)
    print()

    Puzzle.num_of_instances = 0
    t0 = time()
    Astar_search(state[i])
    t1 = time() - t0
    print('A*:')
    print('instancias visitadas:', Puzzle.num_of_instances)
    print('tempo:', t1)
    print()
        
    print('------------------------------------------')