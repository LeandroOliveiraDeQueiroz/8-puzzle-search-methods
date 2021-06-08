from queue import PriorityQueue
from puzzle import Puzzle


def Astar_search(initial_state):
    count=0
    explored=[]
    start_node=Puzzle(initial_state,None,None,0,True)
    # Ordena pela evaluation_function(g' + h') na insercao
    q = PriorityQueue() 
    q.put((start_node.evaluation_function,count,start_node))

    while not q.empty():
        node=q.get()
        node=node[2]
        explored.append(node.state)
        if node.goal_test():
            return node

        # Gera os filho as partir das acoes validas. Checar puzzle.generate_child e puzzle.find_legal_actions
        children=node.generate_child()
        for child in children:
            # Checa e coloca na fila somente os filhos não visitados
            if child.state not in explored:
                count += 1
                q.put((child.evaluation_function,count,child))
    return

