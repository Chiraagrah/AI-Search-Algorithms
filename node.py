class Node:
    def __init__(self,state,puzzle,parent=None,steps=0):
        self.state=state
        self.parent=parent
        self.children=[]
        self.puzzle=puzzle
        self.steps=steps
        self.heuristic=ManhattanDistance(self,puzzle.goalState)+steps

    def expand(self):
        for action in self.puzzle.actions:
            newState=(self.state[0]+action[0],self.state[1]+action[1])
            if self.isValid(newState):
                child=Node(newState,self.puzzle,self,self.steps+1)
                self.children.append(child)
        return self.children
    
    def isValid(self,state):
        if 0<=state[0]<self.puzzle.row and 0<=state[1]<self.puzzle.col:
            return self.puzzle.puzzle[state[0]][state[1]]!="#"
        return False
    
    def path(self):
        node=self
        path=[]
        while node:
            path.append(node.state)
            node=node.parent
        return path[::-1]
    
def ManhattanDistance(node,goal):
    return abs(node.state[0]-goal[0])+abs(node.state[1]-goal[1])