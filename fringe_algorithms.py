from node import Node
from collections import deque
from draw import Draw
import heapq


def bfs(puzzle):
    start=puzzle.startState
    goal=puzzle.goalState
    fringe=deque([Node(start,puzzle)])
    explored=set()
    steps=0
    while fringe:
        current=fringe.popleft()
        steps+=1
        if current.state==goal:
            path= current.path()
            Draw(puzzle,start,goal,fringe,explored,path,steps=steps)
            return None
        explored.add(current.state)
        for child in current.expand():
            if child.state not in explored and all(n.state != child.state for n in fringe):
                fringe.append(child)
        Draw(puzzle,start,goal,fringe,explored,steps=steps)
    return None

def dfs(puzzle):
    start=puzzle.startState
    goal=puzzle.goalState
    fringe=deque([Node(start,puzzle)])
    explored=set()
    steps=0
    while fringe:
        current=fringe.pop()
        steps+=1
        if current.state==goal:
            path= current.path()
            Draw(puzzle,start,goal,fringe,explored,path,steps=steps)
            return None
        explored.add(current.state)
        for child in current.expand():
            if child.state not in explored and all(n.state != child.state for n in fringe):
                fringe.append(child)
        Draw(puzzle,start,goal,fringe,explored,steps=steps)
    return None

def best_fs(puzzle):
    start=Node(puzzle.startState,puzzle)
    goal=puzzle.goalState
    fringe=[]
    heapq.heappush(fringe, (start.heuristic,id(start), start))
    explored=set()
    steps=0
    while fringe:
        current=heapq.heappop(fringe)[-1]
        steps+=1
        if current.state==goal:
            path= current.path()
            Draw(puzzle,start,goal,fringe,explored,path,steps=steps,show_heuristics=True)
            return None
        explored.add(current.state)
        for child in current.expand():
            if child.state not in explored and all(n[-1].state != child.state for n in fringe):
                heapq.heappush(fringe, (child.heuristic,id(child) ,child))
        Draw(puzzle,start,goal,fringe,explored,steps=steps,show_heuristics=True)
    return None

