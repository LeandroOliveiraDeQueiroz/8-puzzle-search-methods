# O modelo do Puzzle funciona tanto para o A* quanto para o BSF

class Puzzle:
    goal_state=[]
    heuristic=None
    evaluation_function=None
    needs_hueristic=False
    num_of_instances=0
    def __init__(self,state,parent,action,path_cost,needs_hueristic=False):
        self.parent=parent
        self.state=state
        self.action=action
        if parent:
            self.path_cost = parent.path_cost + path_cost # gerando g'
        else:
            self.path_cost = path_cost # gerando g'
        if needs_hueristic:
            self.needs_hueristic=True
            self.generate_heuristic() # gerando h'
            self.evaluation_function=self.heuristic+self.path_cost # h' + g'
        

    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    # Distância de Manhantan do tabuleiro
    def generate_heuristic(self):
        self.heuristic=0
        for num in range(1,9):
            distance=abs(self.state.index(num) - self.goal_state.index(num))
            i=int(distance/3)
            j=int(distance%3)
            self.heuristic=self.heuristic+i+j

    # Testando para verificar se o puzzle atingiu objetivo
    def goal_test(self):
        Puzzle.num_of_instances+=1 # Aumenta o contador de instancias visistadas
        if self.state == self.goal_state:
            return True
        return False

    # Identifica movimentos permitidos
    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['C', 'B', 'E', 'D']
        if i == 0:
            legal_action.remove('C')
        elif i == 2:
            legal_action.remove('B')
        if j == 0:
            legal_action.remove('E')
        elif j == 2:
            legal_action.remove('D')
        return legal_action


    # Para cada ação permitida naquela posição, gera um novo tabuleiro
    def generate_child(self):
        children=[]
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions=self.find_legal_actions(i,j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action == 'C':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action == 'B':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action == 'E':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action == 'D':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            children.append(Puzzle(new_state,self,action,1,self.needs_hueristic))
        return children
