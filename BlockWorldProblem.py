from search import *
from utils import *
import sys

class BlockWorldProblem(Problem) :
        def __init__(self) :
                #super(BlockWorldProblem,self).__init__((("c","b","a"),("e","d"),(),(),()),(("a","e"),("b",),("d","c"),(),()))
                #-------#
                #super(BlockWorldProblem,self).__init__((("c","b","a"),("e","d","g"),(),(),(),()),(("a","e"),("b",),("d","c"),("g",),(),()))
                #------#
                #super(BlockWorldProblem,self).__init__((("c","b","a"),("e","d","g"),("h",),(),(),(),()),(("a","e"),("b",),("d","c"),("g",),("h",),()))
                #--------#
                #super(BlockWorldProblem,self).__init__(((3,2,1),(5,4,6),(),(),()),((1,5),(2,),(4,3),(),()))
                #------#
                #super(BlockWorldProblem,self).__init__(((3,2,1),(5,4,6),(),(),(),()),((1,5),(2,),(4,3),(6,),(),()))
                #--------#
                super(BlockWorldProblem,self).__init__(((3,2,1),(5,4,6),(7,),(),(),(),()),((1,5),(2,),(4,3),(6,),(7,),(),()))
                #---------#
                #super(BlockWorldProblem,self).__init__(((3,2,1),(5,4,6),(7,8),(),(),(),(),()),((1,5),(2,),(4,3),(6,8),(7,),(),(),()))
                #--------#
                """apasxoliaste opoia apo tis parapanw 8elete h balte mia dikia sas opws tis bazw
                egw.Wstoso egkyomai oti 8a leitourghsei gia oles tis eisodous
                apla den 8a teleiwsei se grhgoro xrono me autes pou protinw parapanw
                epishs exw afhsei apasxoliasmenh to paradeigma.Gia oles protinw thn h2"""




        """edw proketai gia ta actions to (j,k):
        prokeitai gia to jgia thn stoiba pou 8a paroume
        to stoixeio kai to k gia thn stoiba pou tha baloume to stoixeio"""
        def actions(self,state):
                validaction = []
                validstucks = []
                x=len(state)
                counter=0
                for i in state:
                        counter=counter+1
                        if i:
                                validstucks.append(counter)
                flag=0
                counter2=0
                for i in state:
                        counter2=counter2+1
                        if not i:
                                if flag==0:
                                        validtable=counter2
                                        flag=1
                a=len(validstucks)
                j=1
                while(j<=x):
                        k=1
                        flag=0
                        i=1
                        while(i<=a):
                                if(j==validstucks[i-1]):
                                        flag=1
                                i=i+1
                        if flag==1:
                                while(k<=x):
                                        if (len(state[j-1])==1 and j!=k):
                                                if(len(state[k-1])>=1 and j!=k):
                                                        l=[j,k]
                                                        validaction.append(l)
                                        elif(len(state[j-1])>1 and j!=k):
                                                if(len(state[k-1])>=1):
                                                        l=[j,k]
                                                        validaction.append(l)
                                        k=k+1
                                if(len(state[j-1])>1):
                                        k=validtable
                                        l=[j,k]
                                        validaction.append(l)
                        j=j+1
                return validaction



        """edw exoume ta analoga result twn parapanw:arxika apo poia stoiba bgazoume to stoixeio(action[0])
        kai meta se poia to bazoume(action[1])"""
        def result(self,state,action):
                temp=list(state)
                newstatelist=[]
                for i in temp:
                        newstatelist.append(list(i))
                a=action[0]-1
                b=action[1]-1
                c=newstatelist[a].pop()
                newstatelist[b].append(c)
                flag2=1
                newstatelist = [tuple(l) for l in newstatelist]
                return tuple(newstatelist)

        """edw elenxei to goal state ane3arthtos pou briskontai aneksarthtos diataksis"""
        def goal_test(self, state) :
                n=0
                a=0
                b=0
                lista=self.goal
                l1 = []
                l2 = []
                for i in lista:
                        if i:
                                a=a+1
                for i in state:
                        l1.append(list(i))
                for i in lista:
                        l2.append(list(i))
                for i in l1:
                        if i:
                                if i in l2:
                                        n=n+1
                if n==a:
                        return True
                else:
                        return False
                                        
                        
                        
                        
