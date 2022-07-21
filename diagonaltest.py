from numpy import mat

def zigzag(word, numRows):
    matrix = []
    for i in range(numRows):
        matrix.append([])
    magic(matrix, word, 0)

def magic(matrix, word, rowIndex): 
    
    goingUp = False
    
    for letter in word:
        
        if(goingUp == False):
            matrix[rowIndex].append(letter)
            rowIndex += 1
            if(rowIndex == len(matrix)):
                goingUp = True
                rowIndex -= 1
                continue

        if(goingUp == True):
            rowIndex -= 1
            for i in range(len(matrix)):
                if(i == rowIndex):
                    matrix[i].append(letter)
                else:
                    matrix[i].append(" ")
            if(rowIndex == 0):
                goingUp = False




    for row in matrix:
        print("")
        for letter in row:
            print(letter+ " ", end="")

zigzag("ASDASDDDDDDDDDDDWAWEAWDSDASDASDASDA", 7)

    
                                    #rows= 4 (2 1 columns inbetween)
                                              #      3 (1 column inbetween )
                                                     # 2 would have none between 

#[]
#[]
#[]
#[3 - 2]