
def intercFilas (matriz2, j, i, columnas,filas):
    aux=0

    if (j>=filas-1):
        return()
    while (matriz2[i][j]==0 and j<filas):
        j += 1
    for x in range(columnas):
        aux = matriz2[i][x]
        matriz2[i][x]=matriz2[j][x]
        matriz2[j][x]=aux

    

'''def imprimeMatriz(matriz2):
    print()

    for i in range(len(matriz2)):
        for j in range(len(matriz2[i])):
            print(matriz2[i][j], end="\t")
        print()
    
    print()'''

def pivoteo(filas,columnas,matriz2,vectorPivote,vectorPivoteAux,j):
    pivoteAux = 0
    matrizTemporal = matriz2.copy()
    sumi = 0

    for i in range(filas):
        if(j==i):
            if(matriz2[i][j]==0):
                intercFilas(matriz2,j,i,columnas,filas)

            pivoteAux = matrizTemporal[i][j]

            for l in range(columnas):
                if(pivoteAux==0):
                    print('La matriz no tiene solucion, es incosistente')
                    matrizTemporal = map(str, matrizTemporal)
                    matrizTemporal = "\n".join(matrizTemporal)
                    
                matrizTemporal[i][l] = matrizTemporal[i][l]/pivoteAux 
                vectorPivote[l] = matrizTemporal[i][l]
                vectorPivoteAux[l] = matrizTemporal[i][l]

    return matrizTemporal

def comprobMatriz(matriz2,columnas):
    pass
    cont = 0

    #print()

    for i in range(len(matriz2)):
        aux = matriz2[i][columnas-1]
        for j in range(columnas-1):
            if(matriz2[i][j]==0 and aux!=0):
                cont += 1
        if(cont==columnas-1):
            pass
    #print()
    
def main(matriz2):
    #inicio de la funcion principal
    # imprimeMatriz(matriz)
    filas = len(matriz2)
    columnas = len(matriz2[0])
    pivoteAux = 0
    vectorPivote = []
    vectorPivoteAux = []
    n = 0

    for z in range(columnas):
        vectorPivote.append(None)
        vectorPivoteAux.append(None)

    #Inicio metodo Gauus-Jordan 
    for j in range(columnas-1):

        matriz2 = pivoteo(filas,columnas,matriz2,vectorPivote,vectorPivoteAux,j)

        for i in range(filas):
            if (i != j) and (j<columnas-1):
                n = matriz2[i][j]

            #Ciclo para hacer ceron el elemento
            for k in range(columnas):
                matriz2[i][k] = (-1*n*vectorPivote[k] + matriz2[i][k])

            if i == j:
                for l in range(columnas):
                    matriz2[i][l] = vectorPivoteAux[l]

                    if (matriz2[i][l] == 0):
                        matriz2[i][l] = 0
                
            #imprimeMatriz(matriz2)

        for h in range(columnas):
            vectorPivote[h] = 0
        
        

        
