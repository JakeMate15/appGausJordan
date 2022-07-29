from distutils.log import error
import re
import numpy as np
from numpy.linalg import inv
errorCode = 0
f = open("matriz.txt","r") #hace falta poner la apertura desde el explorador de archivos 
content = f.read()
lista_filas = content.splitlines()
filas = len(lista_filas)
#detectar numero de valores por fila inconsistente
a = [0]*filas
for i in range (filas):
    a[i] = len(lista_filas[i].split())
if any (a[0] != a[i] for i in range(filas)):
    errorCode = 1
valores = content.split()
#detectar simbolos invalidos
columnas = int(len(valores)/filas)
matriz = []
matrizAux = []
for i in range(filas):
    matriz.append([0]*columnas)
    matrizAux.append([0]*columnas)
c=0
for i in range (filas):
    for j in range (columnas):
        matrizAux[i][j]=valores[c]
        c=c+1
c=0
#detectar cuando se introduce un valor incompatible
for i in range (filas):
    for j in range (columnas):
        if(len(re.findall(r'[0-9/,-]', matrizAux[i][j]))!=len(matrizAux[i][j])):
            errorCode=2
            c+=1
#obtener las coordenadas del lugar donde se encuentra el valor incompatible
if errorCode == 2:
    x=[0]*c
    y=[0]*c
    c=0
    for i in range (filas):
        for j in range (columnas):
            if (len(re.findall(r'[0-9/,-]', matrizAux[i][j]))!=len(matrizAux[i][j])):
                x[c]=i
                y[c]=j
                c+=1
    print(x,y)
#si no hay errores
if errorCode == 0:
    m=0
    n=0
    for i in range (filas):
        for j in range (columnas):
            if (bool(re.search(r'[/]',matrizAux[i][j]))):
                fract = [0]*2
                fract = (re.split(r'[/]',matrizAux[i][j]))
                division = float(float(fract[0])/float(fract[1]))
                matriz[m][n] = division
            if (not bool(re.search(r'[/]',matrizAux[i][j]))):
                    matriz[m][n]=float(matrizAux[i][j])
            n+=1
        n=0
        m+=1
    print(matriz)
    print(filas,columnas)
print(errorCode)

copia_matriz = []

if(filas != columnas):
    for i in range (filas):
        copia_matriz.append([0]*(columnas-1))
    for i in range(filas):
        for j in range(columnas-1):
            copia_matriz[i][j]=matriz[i][j]
if (filas == columnas):
    for i in range (filas):
        copia_matriz.append([0]*(columnas))
    for i in range(filas):
        for j in range(columnas):
            copia_matriz[i][j]=matriz[i][j]
a = np.array(copia_matriz)
inversa = inv (a)
print(inversa)

if(filas != columnas):
    print("No es determinante.")
    quit()

if(filas==columnas):
    n = filas
    def gauss(n):
        for z in range (n-1):
            for x in range(1, n-z):
                if (matriz[z][z] != 0 ):
                    p = matriz[x+z][z] / matriz[z][z]
                    for y in range (n):
                        matriz[x+z][y] = matriz[x+z][y] - (matriz[z][y]*p)
                        
    def det(n):
        deter=1
        for x in range (n):
            deter=matriz[x][x]*deter
        print ('\nEl determinante de la matriz es = ', deter)


#Programa
n = filas
gauss(n)
det(n)