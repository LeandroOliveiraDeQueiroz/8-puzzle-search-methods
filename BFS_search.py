from queue import Queue
from puzzle import Puzzle

# Algoritmo de busca em largura
def breadth_first_search(initial_state):
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        # Gera os filho as partir das acoes validas. Checar puzzle.generate_child e puzzle.find_legal_actions
        children=node.generate_child()
        for child in children:
            # Checa e coloca na fila somente os filhos não visitados
            if child.state not in explored:
                # Testa ao colocar na fila
                if child.goal_test():
                    return child
                q.put(child)
    return
