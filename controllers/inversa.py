import numpy as np
from fractions import Fraction
import re
import numpy as np
from numpy.linalg import inv


#print('Codigo de error:')
#print(errorCode)

def imprimeMatriz(matriz,filas,columnas):
    print()

    for i in range(filas):
        for j in range(columnas):
            print(round(matriz[i][j],2), end="\t")
        print()
    
    print()

def imprimeMatrizConDivision(matriz,filas,columnas,opcion):
    print(matriz)

    if(opcion==0):
        for i in range(filas):
            for j in range(columnas):
                if(j==columnas/2):
                    print(end="|\t")
                matriz[i][j]= matriz[i][j] = Fraction(matriz[i][j]).limit_denominator()
                print(matriz[i][j], end="\t")
            print()
    elif(opcion==1):
        for i in range(filas):
            for j in range(columnas):
                if(j==columnas-1):
                    print(end="|\t")
                matriz[i][j]= matriz[i][j] = Fraction(matriz[i][j]).limit_denominator()
                print(matriz[i][j], end="\t")
            print()
    
    print()

def creaMatrizIdentidad(tam):
    matriz = []
    
    for i in range(tam):
        matriz.append([])
        for j in range(tam):
            matriz[i].append(None)
            if(i==j):
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0

    return matriz               

def eliminaUltimaFila(matriz):
    aux = []

    for i in range(len(matriz)):
        aux.append([])
        for j in range(len(matriz[i])):
            aux[i].append(None)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            aux[i][j] = matriz[i][j]

    for i in range(len(aux)):
        aux[i].pop()

    return aux

def intercFilas (matriz, j, i, columnas):
    aux=0
    while (matriz[i][j]==0):
        j += 1
    for x in range(columnas):
        aux = matriz[i][x]
        matriz[i][x]=matriz[j][x]
        matriz[j][x]=aux
  
def pivoteo(filas,columnas,matrizA,vectorPivote,vectorPivoteAux,j):
    pivoteAux = 0
    matrizTemporal = matrizA.copy()

    for i in range(filas):
        if(j==i):
            if(matrizTemporal[i][j]==0):
                intercFilas(matrizTemporal,j,i,columnas)

            pivoteAux = matrizTemporal[i][j]

            for l in range(columnas):
                matrizTemporal[i][l] = matrizTemporal[i][l]/pivoteAux 
                vectorPivote[l] = matrizTemporal[i][l]
                vectorPivoteAux[l] = matrizTemporal[i][l]

    return matrizTemporal

def comprobMatriz(matriz,columnas):
    cont = 0

    print()

    for i in range(len(matriz)):
        aux = matriz[i][columnas-1]
        for j in range(columnas-1):
            if(matriz[i][j]==0 and aux!=0):
                cont += 1
        if(cont==columnas-1):
            print('Es inconsistente')
    print()

def combinaMatriz(matriz1,matriz2,filas,columnas):
    for i in range(filas):
        for j in range(columnas,(columnas*2),1):
            matriz1[i].append(None)
            matriz1[i][j] = matriz2[i][j-columnas]
            

    

def eliminacionGauss(matriz,filas,columnas,opcion):
    vectorPivote = []
    vectorPivoteAux = []
    n = 0

    for z in range(columnas):
        vectorPivote.append(None)
        vectorPivoteAux.append(None)


    for j in range(columnas-1):

        matriz = pivoteo(filas,columnas,matriz,vectorPivote,vectorPivoteAux,j)

        for i in range(filas):
            if (i != j) and (j<columnas-1):
                n = matriz[i][j]
        
            for k in range(columnas):
                matriz[i][k] = (-1*n*vectorPivote[k] + matriz[i][k])

            if i == j:
                for l in range(columnas):
                    matriz[i][l] = vectorPivoteAux[l]

                    if (matriz[i][l] == 0):
                        matriz[i][l] = 0
                
            imprimeMatrizConDivision(matriz,len(matriz),len(matriz[0]),opcion)

        for h in range(columnas):
            vectorPivote[h] = 0

          
def inversaDeUnaMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    imprimeMatriz(matriz,filas,columnas)

    determinate = np.linalg.det(matriz)

    if(determinate!=0):
        identidad = creaMatrizIdentidad(filas)
        print(identidad)
        combinaMatriz(matriz,identidad,filas,columnas)
        print(matriz)
        columnas = len(matriz[0])
        n = 0

        eliminacionGauss(matriz,filas,columnas,0)

        print("La inversa de la matriz es ")
        columnas = int(columnas/2)
        matriz_aux = []
        for i in range(filas):
            matriz_aux.append([0]*columnas)
        for i in range(filas):
            for j in range(columnas,(columnas*2),1):
                matriz[i][j] = Fraction(matriz[i][j]).limit_denominator()
                matriz_aux[i][int(j-columnas)]=matriz[i][j]
                #print(matriz[i][j], end="\t")
            print()
        return matriz_aux, determinate

    else:
        print("La matriz no es invertible")
    
    #print("La matriz: {}".format(matriz))
    



def main():
    pass

if __name__ == "__main__":
    main()
