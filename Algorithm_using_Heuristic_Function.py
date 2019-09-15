from random import randint
import heapq
from itertools import count

GoalState = [[0, "x", "x"], 
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9]]
#before shuffling
BS = [[0, "x", "x"], 
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9]]
BS1 = [[1, "x", "x"], 
    [0, 2, 3],
    [4, 5, 6],
    [7,8,9]]
BS2 = [[1, "x", "x"], 
    [2, 0, 3],
    [4, 5, 6],
    [7,8,9]]
BS3 = [[1, "x", "x"], 
    [2, 5, 3],
    [4, 0, 6],
    [7,8,9]]
BS4 = [[1, "x", "x"], 
    [2, 5, 3],
    [4, 6, 0],
    [7,8,9]]
BS5 = [[1, "x", "x"], 
    [2, 5, 3],
    [4, 6, 9],
    [7,8,0]]
BSS = [[1, "x", "x"], 
    [2, 5, 0],
    [4, 6, 9],
    [7,8,3]]
BSSD = [[1, "x", "x"], 
    [2, 5, 0],
    [4, 6, 9],
    [7,8,3]]

#print(A[0][1])
## first index row , second index col
def prettyPrint(GoalState):
    for x in range (0,4):
        print(str(GoalState[x][0]) + "  " +str(GoalState[x][1])+ "  " +str(GoalState[x][2]))

def prettyPrintStates(states):
    for c in range (0,len(states)):
        for x in range (0,4):
            print(str(states[c][x][0])+str(states[c][x][0])+str(states[c][x][0]))

movementsArray = ["left","right","up","down"]

## define functions
def second_smallest(numbers):
    temp=numbers
    temp2=temp.index(min(temp))
    temp[temp2] = 100
    return temp.index(min(temp))

def third_smallest(x):
    temp=numbers
    temp2=temp.index(min(temp))
    temp[temp2] = 100
    temp3=temp.index(min(temp))
    temp[temp3] = 100
    return temp.index(min(temp))

def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n-1, n), None)
def get_nth_index(lst, item, n):
    x = 0
    index = 0
    while x != n :
        if lst[index] == item:
            x = x + 1 
        index = index +1    
    return index-1

def left(M,indexRow,indexCol):
    B = M
    if M[indexRow][indexCol-1] == 0:    
            B[indexRow][indexCol-1] =M[indexRow][indexCol]
            M[indexRow][indexCol] = 0
    else:
      print("This can not be done")        
    return B

def right(M,indexRow,indexCol):
    B = M
    if M[indexRow][indexCol+1] == 0:    
            B[indexRow][indexCol+1] = M[indexRow][indexCol]
            M[indexRow][indexCol] = 0
    else:
      print("This can not be done")        
    return B

def up(M,indexRow,indexCol):
    B = M
    if M[indexRow-1][indexCol] == 0:    
            B[indexRow-1][indexCol] = M[indexRow][indexCol]
            M[indexRow][indexCol] = 0
    else:
      print("This can not be done")        
    return B

def down(M,indexRow,indexCol):
    B = M
    if M[indexRow+1][indexCol] == 0:    
            B[indexRow+1][indexCol] = M[indexRow][indexCol]
            M[indexRow][indexCol] = 0
    else:
      print("This can not be done")        
    return B

def whereIsSpace(M):
    a = 0
    b = 0
    for x in range (0,4):
        for i in range (0,3):
            if M[x][i] == 0:
                a = x
                b = i
    return a,b
def CopList(MC):
    C = []
    for x in range (0,4):
        C.append(MC[x][:])             
    return C

def getNeighboursOfSpace(M):
    #prettyPrint(M)
    SR,SC = whereIsSpace(M)
    N1R = SR-1
    N1C = SC
    N1 = "down"
    N2R = SR+1
    N2C = SC
    N2 = "up"
    N3R = SR
    N3C = SC-1
    N3 = "right"
    N4R = SR
    N4C = SC+1
    N4 = "left"
    NCor = [N1R,N1C,N2R,N2C,N3R,N3C,N4R,N4C]
    FalseCor = []
    NewCor = []
    NMovs = [N1,N2,N3,N4]
    FMovs = []
    NewMovs = []
    l = 8
    for x in range (0,l):
        if NCor[x] < 0 and x%2==0:
            FMovs.append(x/2)
            FalseCor.append(x)
            FalseCor.append(x+1)
        elif NCor[x] < 0 and x%2==1:
            FMovs.append((x-1)/2)
            FalseCor.append(x)
            FalseCor.append(x-1)
        elif NCor[x] == 0 and NCor[x+1] == 1 and x%2==0:
            FMovs.append((x)/2)
            FalseCor.append(x)
            FalseCor.append(x+1)
        elif NCor[x] == 0 and NCor[x+1] == 2 and x%2==0:
            FMovs.append((x)/2)
            FalseCor.append(x)
            FalseCor.append(x+1)
        elif NCor[x] > 2 and x%2==1:
            FMovs.append((x-1)/2)
            FalseCor.append(x)
            FalseCor.append(x-1)
        elif NCor[x] > 3 and x%2==0:
            FMovs.append(x/2)
            FalseCor.append(x)
            FalseCor.append(x+1)    

    for x in range (0,8):
        if x in FalseCor:
            pass
        else:
            NewCor.append(NCor[x])

    for x in range (0,4):
        if x in FMovs:
            pass
        else:
            NewMovs.append(NMovs[x])

    return NewMovs,NewCor



def Shuffle(M,n):
    for i in range (0,n):  
          Moves,Coor = getNeighboursOfSpace(M)
          rand = randint(0, len(Moves)-1)
          if "down" == Moves[rand]:
                #print("down")
                down(M,Coor[rand*2],Coor[rand*2+1])            
          if "up" == Moves[rand]:
                up(M,Coor[rand*2],Coor[rand*2+1])
                #print("up")
          if "right" == Moves[rand]:
                right(M,Coor[rand*2],Coor[rand*2+1])
                #print("right")
          if "left" == Moves[rand]:
                left(M,Coor[rand*2],Coor[rand*2+1])

                #print("left")
    #prettyPrint(M) 
    return M



def findMin(A):
    return min(A)

def StateGenerator(M):
    Moves,Coor = getNeighboursOfSpace(M)
    Mstate1 = CopList(M)
    Mstate2 = CopList(M)
    Mstate3 = CopList(M)
    Mstate4 = CopList(M)
    #print("Array which states will be generated")    
    #prettyPrint(M)
    #print(Moves)
    #print(Coor)
    states = []
    for i in range (0,len(Moves)):
        if "down" == Moves[i]:
            #print("down")
            states.append(down(Mstate1,Coor[i*2],Coor[i*2+1]))            
        if "up" == Moves[i]:
            states.append(up(Mstate2,Coor[i*2],Coor[i*2+1]))
            #print("up")
        if "right" == Moves[i]:
            states.append(right(Mstate3,Coor[i*2],Coor[i*2+1]))
            #print("right")
        if "left" == Moves[i]:
            states.append(left(Mstate4,Coor[i*2],Coor[i*2+1]))
            #print("left")
    #print("States From Previous Array")
    #for i in range (0,len(states)):
        #for v in range (0,4):            
            #print(states[i][v])
    return states       
row = 4
def heuristic1Calculator(M):
    b = 0
    if (M[1][0]==1):
        b = b +1
    if (M[2][0]==4):
        b = b +1    
    if (M[3][0]==7):
        b = b +1
    if (M[1][1]==2):
        b = b +1
    if (M[2][1]==5):
        b = b +1
    if (M[3][1]==8):
        b = b +1
    if (M[1][2]==3):
        b = b +1    
    if (M[2][2]==6):
        b = b +1
    if (M[3][2]==9):
        b = b +1
    return 9-b

def heuristicsOfStates(states):
    dis = []
    for i in range (0,len(states)):
        dis.append(heuristic1Calculator(states[i]))
    return dis
def deleteIndexes(my_list,indexes):
    for index in sorted(indexes, reverse=True):
        del my_list[index]

def solveW2(M,GoalState):
    print('Save all states')
    allstates = []
    states = StateGenerator(M)
    totalStates = states
    allstates=allstates+totalStates
    print('Find heuristics - h1 - w=2')
    heuristics = heuristicsOfStates(totalStates)
    print('Find min and second min heur')
    minheur = min(heuristics)
    min1 = heuristics.index(min(heuristics))
    min2 = second_smallest(heuristics)
    print('Generate new states')
    states = StateGenerator(totalStates[min1])
    states2 = StateGenerator(totalStates[min2])
    totalStates = states + states2
    print('Delete repeated states to avoid loops')
    deletestates = []
    for x in range (0,len(allstates)):
        for y in range (0,len(totalStates)):
            if allstates[x]==totalStates[y]:
                deletestates = deletestates + y
    deleteIndexes(totalStates,deletestates)
    allstates=allstates+totalStates
    heuristics = heuristicsOfStates(totalStates)
    minheur = min(heuristics)
    min1 = heuristics.index(min(heuristics))
    min2 = second_smallest(heuristics)
    i=1
    if minheur != []:
        print('Great!')
        while minheur!=0 and heuristics!=[]:
            i=i+1
            states = StateGenerator(totalStates[min1])
            states2 = StateGenerator(totalStates[min2])
            totalStates = states + states2
            deletestates = []
            print('Delete repeated states to avoid loops')
            for x in range (0,len(allstates)):
                for y in range (0,len(totalStates)):
                    if allstates[x]==totalStates[y]:
                        deletestates.append(y)
            deleteIndexes(totalStates,deletestates)
            allstates=allstates+totalStates
            heuristics = heuristicsOfStates(totalStates)
            if heuristics!=[]:
                minheur = min(heuristics)
                min1 = heuristics.index(min(heuristics))
                min2 = second_smallest(heuristics)   
    print('Congratulations!!!!')
    return i

def solveW3(M,GoalState):
    allstates = []
    states = StateGenerator(M)
    totalStates = states
    allstates=allstates+totalStates
    print('Find heuristics - h1 -w=3')
    heuristics = heuristicsOfStates(totalStates)
    minheur = min(heuristics)
    print('Generate new states')
    min1 = heuristics.index(min(heuristics))
    min2 = second_smallest(heuristics)
    min3 = second_smallest(heuristics)
    print('Find min and second min heur')
    states = StateGenerator(totalStates[min1])
    states2 = StateGenerator(totalStates[min2])
    states3 = StateGenerator(totalStates[min3]) 
    totalStates = states + states2 + states3
    deletestates = []
    print('Delete repeated states to avoid loops')
    for x in range (0,len(allstates)):
        for y in range (0,len(totalStates)):
            if allstates[x]==totalStates[y]:
                deletestates = deletestates + y
    deleteIndexes(totalStates,deletestates)
    allstates=allstates+totalStates
    heuristics = heuristicsOfStates(totalStates)
    minheur = min(heuristics)
    min1 = heuristics.index(min(heuristics))
    min2 = second_smallest(heuristics)
    min3 = second_smallest(heuristics)
    i=1
    if minheur != []:
        print('Great!')
        while minheur!=0 and heuristics!=[]:
            i=i+1
            states = StateGenerator(totalStates[min1])
            states2 = StateGenerator(totalStates[min2])
            states3 = StateGenerator(totalStates[min3])
            totalStates = states + states2 + states3
            deletestates = []
            for x in range (0,len(allstates)):
                for y in range (0,len(totalStates)):
                    if allstates[x]==totalStates[y]:
                        deletestates.append(y)
            deleteIndexes(totalStates,deletestates)
            allstates=allstates+totalStates
            heuristics = heuristicsOfStates(totalStates)
            if heuristics!=[]:
                minheur = min(heuristics)
                min1 = heuristics.index(min(heuristics))
                min2 = second_smallest(heuristics)
                min3 = second_smallest(heuristics)
    print('Congratulations!!!!')
    return i


##initial States
B = CopList(BS)
S = Shuffle(B,30)
SC = CopList(S)
#A = [2, 2, 3, 2, 4 ]
#print(get_nth_index(A,2,3))
#print(solveW3(S,GoalState))
#deleteIndexes(A,[0,2])
#print(A)
c=0
allinitials = []
while c<=25:
    try:
        #print("Deneme "+str(c))
        B = CopList(BS)
        S = Shuffle(B,30)
        SC = CopList(S)
        print('Initial State ' + str(c))
        prettyPrint(S)
        #allinitials = allinitials + S
        print("This is our initial state: ")
        prettyPrint(SC)
        print("Solving the puzzle: ")
        iter2 = solveW2(S,GoalState)
        iter3 = solveW3(SC,GoalState)
        print("iteration number for w=2: " + str(iter2))
        print("iteration number for w=3: " + str(iter3))
        #print(iter2)
        #print(iter3)
        c = c+1
    except:
        pass

