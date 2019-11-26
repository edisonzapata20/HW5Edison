import numpy

grid = numpy.random.choice([x for x in range(0,2)],5*5)

#If a set matrix wants to be used comment the grid above and uncomment the one below for testing
#grid = numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

gridA= numpy.asmatrix(grid)
BoardMatrix = numpy.asarray(gridA).reshape(5, 5)

rows = BoardMatrix.shape[0]
columns = BoardMatrix.shape[1]


#Changes adjacent spaces and current position to the position that had a 1 above it
def changeState(a,b):
    position = BoardMatrix
    if b+1 <=4:
        if position[a][b + 1] == 0:
            position[a][b + 1] = 1
        else:
            position[a][b+1] = 0
    if b-1 >= 0:
        if position[a][b - 1] == 0:
            position[a][b - 1] = 1
        else:
            position[a][b-1] = 0
    if a-1 >=0:
        if position[a - 1][b] == 0:
            position[a - 1][b] = 1
        else:
            position[a-1][b] = 0
    if a+1 <=4:
        if position[a + 1][b] == 0:
            position[a + 1][b] = 1
        else:
            position[a+1][b] = 0

    if position[a][b] == 0:
        position[a][b] = 1
    else:
        position[a][b] = 0

# Searches for positions with 1 above it
def searchMatrix():
    for i in range(1, rows):
        for j in range(0, columns):
            if (BoardMatrix[i - 1, j]) == 1:
                changeState(i,j)
    print(BoardMatrix)


def stepstoSolve():
    if(BoardMatrix[4][2] == 1 and BoardMatrix[4][3] == 1 and BoardMatrix[4][4] ==1 and BoardMatrix[4][1]==0 and BoardMatrix[4][0]==0):
        print ("To solve the game press the position [0,3] and use light chasing again")
        changeState(0,3)
        secondstatechange()
        return
    if (BoardMatrix[4][2] == 0 and BoardMatrix[4][3] == 0 and BoardMatrix[4][4] == 0 and BoardMatrix[4][1] == 0 and
            BoardMatrix[4][0] == 0):
        print("Game is solved")
        return
    if (BoardMatrix[4][1] == 1 and BoardMatrix[4][3] == 1 and BoardMatrix[4][2]==0 and BoardMatrix[4][4]==0 and BoardMatrix[4][0]==0):
        print("To solve the game press the positions [0,1] and [0,4] and use light chasing again")
        changeState(0,1)
        changeState(0,4)
        secondstatechange()
        return
    if (BoardMatrix[4][1] == 1 and BoardMatrix[4][2] == 1 and BoardMatrix[4][4] == 1 and BoardMatrix[4][0]==0 and BoardMatrix[4][3]==0):
        print("To solve the game press the position [0,0] and use light chasing again")
        changeState(0,0)
        secondstatechange()
        return
    if (BoardMatrix[4][0] == 1 and  BoardMatrix[4][4] == 1 and BoardMatrix[4][2]==0 and BoardMatrix[4][1]==0 and BoardMatrix[4][3]==0):
        print("To solve the game press the position [0,3] and [0,4] and use light chasing again")
        changeState(0,3)
        changeState(0,4)
        secondstatechange()
        return
    if (BoardMatrix[4][0] == 1 and BoardMatrix[4][2] == 1 and BoardMatrix[4][3] == 1 and BoardMatrix[4][4]==0 and BoardMatrix[4][1]==0):
        print("To solve the game press the position [0,4] and use light chasing again")
        changeState(0,4)
        secondstatechange()
        return
    if (BoardMatrix[4][0] == 1 and BoardMatrix[4][1] == 1 and BoardMatrix[4][3] and BoardMatrix[4][4] == 1 and BoardMatrix[4][2]==0):
        print("To solve the game press the position [0,2] and use light chasing again")
        changeState(0,2)
        secondstatechange()
        return
    if (BoardMatrix[4][0] == 1 and BoardMatrix[4][1] == 1 and BoardMatrix[4][2] == 1 and BoardMatrix[4][3]==0 and BoardMatrix[4][4]==0):
        print("To solve the game press the position [0,1] and use light chasing again")
        changeState(0,1)
        secondstatechange()
        return
    else:
        print ("Game can't be solved since one of the 9 possible cases is not found")
        return


print ("Lights out game to solve if its solvable (run multiple times until a solvable game is found: ")

print(BoardMatrix)

print ("Lights out game matrix gotten after applying light chasing: ")

searchMatrix()

def secondstatechange():

    print("Matrix to apply light chasing again on: ")
    print(BoardMatrix)

    print("After using the given position and light chasing the game is solved: ")
    searchMatrix()

stepstoSolve()