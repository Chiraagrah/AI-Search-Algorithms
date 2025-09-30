from fringe_algorithms import best_fs
from draw import wait_for_close
from node import Node

class Problem:
    def __init__(self,puzzle):
        self.puzzle=[list(x) for x in puzzle.split("\n")]
        self.row=len(self.puzzle)
        self.col=len(self.puzzle[0])
        self.startState=self.find("S")
        self.goalState=self.find("G")
        self.actions=[(0,1),(1,0),(0,-1),(-1,0)]

    def GoalTest(self,state):
        return state==self.goalState

    def find(self,element):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j]==element:
                    return (i,j)
        return None


if __name__=="__main__":
    puzzle="""S  ############################
   #     #        #  #     #  #
#  #  #  #######  #  #  ####  #
#     #              #     #  #
################  ####  ####  #
#        #  #                 #
####  ####  #  #  #  ##########
#              #  #     #  #  #
#  #  #  ####  ##########  #  #
#  #  #     #        #     #  #
#  ##########  #  ####  ####  #
#     #  #     #  #  #        #
#  #  #  ##########  ####  ####
#  #     #           #     #  #
#  #######  #######  ####  #  #
#  #        #  #  #  #        #
#  #  #######  #  #  #######  #
#     #  #  #                 #
#  #  #  #  ##########  #  #  #
#  #     #              #  #   
############################  G"""
    puzzle=Problem(puzzle)
    best_fs(puzzle)
    wait_for_close()




