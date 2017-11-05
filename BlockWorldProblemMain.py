from BlockWorldProblem import *
from search import *
from utils import *
import sys

def h1(n):
        """mia aplh euretikh ~1200 nodes pernei gurw sta 10-20 sec
        analoga me ton forto tou H/Y ftanei max mexri 5 kuboi meta pernei pollh wra perissotero
        dokimastikh gia swsth leitouyrgeia"""
        return 1

def h2(n):
        """plithos lathasmenwn kibwtiwn elenxei sumfwna me thn telikh katastash an einai sthn swsth seira ane3arthta apo se poia stoiba einai """
        state=n.state
        y=0
        lista=p.goal
        for i in lista:
                if i:
                        counter=0
                        for j in i:
                                counter=counter+1
                                for k in state:
                                        counter2=0
                                        if k:
                                                for l in k:
                                                        counter2=counter2+1
                                                        if counter2!=counter and j==k:
                                                                y=y+1
        return y
                

def h3(n):
        """poso makria einai apo to goal state sugkrinei stoiba stoiba anti gia stoixeio stoixeio
        einai kalh euretikh analoga me to pws mpenoun ta toublakia mporei na ftasei mexri kai 11"""
        state=n.state
        lista=p.goal
        y=0
        l1=[]
        l2=[]
        for i in state:
                l1.append(list(i))
        for i in lista:
                l2.append(list(i))
        for i in l1:
                if i:
                        if i not in l2:
                                y=y+1
        return y


p = BlockWorldProblem()
s = astar_search(p,h3)
sol = s.solution() # The sequence of actions to go from the root to this node
path = s.path() # The nodes that form the path from the root to this node
print "Solution: \n+{0}+\n|Action\t|State\t	\t|Path Cost |\n+{0}+".format('-'*42)
for i in range(len(path)) :
	state = path[i].state
	cost = path[i].path_cost
	action = " "
	if i > 0 : # The initial state has not an action that results to it
		action = sol[i-1]
	print "|{0}\t|{1} \t|{2} \t   |".format(action, state, cost)
print "+{0}+".format('-'*42)
