import numpy as np

def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            # you need to increment through dataList here, like this:
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)
    return mat

def addkey(mat, key):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = chr(ord(mat[i][j]) + int(key))
    return mat

def leftshifting(mat):
    
    for i in range(4):
       mat[i]=np.roll(mat[i],-1)
    mat=to_list(mat)
    return mat

def to_list(mat):
    lista=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            lista.append(mat[i][j])
    mat=createMatrix(4,4,lista)
    return mat

def to_number(mat):
    for  i in range(4):
        for j in range(4):
            mat[i][j]=ord(mat[i][j])-96
    return mat

def getinput():
    alpha  = [None]*16
    input1=input("Inserisci la stringa: ")
    alpha=input1+" "*(16-len(input1))
    return alpha

def main():
    alpha = getinput()
    mat = createMatrix(4,4,alpha)
    print (mat)
    key=input("Inserisci la chiave: ")
    addkey(mat,key)
    print (mat)
    mat=leftshifting(mat)
    print (mat)
    mat= to_number(mat)
    print (mat)
    
main()