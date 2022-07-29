from importlib.resources import path
from random import gauss
import sys
from turtle import home
from PyQt5.QtWidgets import QFileDialog, QDialog
import PySide2
from PySide2.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import *
from PySide2.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.mainwindow import MainWindow
from views.VentanaGauss import VentanaGauss
import re, os
from PySide2.QtWidgets import QApplication
import numpy as np
from numpy.linalg import inv
from fractions import Fraction


class GaussWindow(QWidget, VentanaGauss):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowFlag(Qt.Window)
        self.boton_home.clicked.connect(self.home)
        self.boton_MGauss.clicked.connect(self.boton_gauss)
        self.boton_inversa.clicked.connect(self.inversa)
        self.boton_determinante.clicked.connect(self.determinante)

        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        #print(path)


###############################################################################################
#       Leer el archivo 
        errorCode = 0
        f = open(path,"r") #hace falta poner la apertura desde el explorador de archivos 
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
        matriz_reserva = []
        for i in range(filas):
            matriz.append([0]*columnas)
            matrizAux.append([0]*columnas)
            matriz_reserva.append([0]*columnas)
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
            x = [i+1 for i in x]
            y = [i+1 for i in y]
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
                        matriz_reserva[m][n] = division
                        matriz[m][n] = division
                    if (not bool(re.search(r'[/]',matrizAux[i][j]))):
                            matriz_reserva[m][n] = float(matrizAux[i][j])
                            matriz[m][n]=float(matrizAux[i][j])
                    n+=1
                n=0
                m+=1
            #print(matriz, filas, columnas)
        #print(errorCode)
        
        self.path = path
        self.matriz = matriz
        self.filas = filas
        self.columnas = columnas


        matriz = map(str, matriz)
        matriz = "\n".join(matriz)

        if errorCode == 0:
            self.TEXT_matriz.setText(matriz)
            self.TEXT_matriz.setStyleSheet("color: rgb(255, 255, 255);")

        elif errorCode == 1:
            from controllers.error_1 import error1
            window = error1(self)
            window.show()
            home()

        
        elif errorCode == 2:
            coordenadas = []
            for a in x:
                coordenadas.append(a)
                for b in y:
                    coordenadas.append(b)

            coordenadas = map(str, coordenadas)
            coordenadas = ", ".join(coordenadas)

            from PySide2.QtWidgets import QWidget
            from views.error2 import Form_error2


            class error2(QWidget, Form_error2):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.setWindowFlag(Qt.Window)
                    self.textBrowser_error2.setText(coordenadas)
                    self.textBrowser_error2.setStyleSheet("color: rgb(255, 255, 255);")

            
            window_error2 = error2(self)
            window_error2.show()

        ############################################
        



    def home(self):
        from controllers.mainwindow import MainWindow
        window = MainWindow(self)
        self.close()
        window.show()


    def determinante(self):
        from controllers.procesar_matriz import procesarMatriz

        matriz_determinante = procesarMatriz(self.path)
        print(matriz_determinante)
        filas = self.filas
        columnas = self.columnas
        copia_matriz = []

        if (filas == columnas):
            for i in range (filas):
                copia_matriz.append([0]*(columnas))
            for i in range(filas):
                for j in range(columnas):
                     copia_matriz[i][j]=matriz_determinante[i][j]
        
        else:
            from views.error_filas import Form_error1
            from PySide2.QtWidgets import QWidget

            class errorFilas(QWidget, Form_error1):
                def __init__ (self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.setWindowFlag(Qt.Window)
            
            window_error_fila = errorFilas(self)
            window_error_fila.show()

        a = np.array(copia_matriz)
        determinante = np.linalg.det(a)

        determinante = str(Fraction(determinante).limit_denominator())
        determinante = str(determinante)

        self.TEXT_resultado.setText(determinante)
        self.TEXT_resultado.setStyleSheet("color: rgb(255, 255, 255);")
        


    def inversa(self):
        from controllers.procesar_matriz import procesarMatriz
        from controllers.inversa import inversaDeUnaMatriz

        matriz_inversa = procesarMatriz(self.path)
        filas = self.filas
        columnas = self.columnas

        if (filas == columnas):
            matriz_inversa, determinante = inversaDeUnaMatriz(matriz_inversa)
        
        else:
            from views.error_filas import Form_error1
            from PySide2.QtWidgets import QWidget

            class errorFilas(QWidget, Form_error1):
                def __init__ (self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.setWindowFlag(Qt.Window)
            
            window_error_fila = errorFilas(self)
            window_error_fila.show()
            

        #print(a)
        
        '''except:
            from PySide2.QtWidgets import QWidget
            from views.error_inversa import Form_error_inversa


            class error_inversa(QWidget, Form_error_inversa):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.setWindowFlag(Qt.Window)
            
            window_inversa = error_inversa(self)
            window_inversa.show()
            home(self)'''
        
        for i in range(len(matriz_inversa)):
            for j in range(len(matriz_inversa[i])):
                matriz_inversa[i][j] = str(Fraction(matriz_inversa[i][j]).limit_denominator())
                #print(Minversa[i][j], end="\t")

        if columnas == filas and determinante !=0:
            matriz_inversa = map(str, matriz_inversa)
            matriz_inversa = "\n".join(matriz_inversa)

            self.TEXT_resultado.setText(matriz_inversa)
            self.TEXT_resultado.setStyleSheet("color: rgb(255, 255, 255);")
        
        else:
            from PySide2.QtWidgets import QWidget
            from views.error_inversa import Form_error_inversa


            class error_inversa(QWidget, Form_error_inversa):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.setWindowFlag(Qt.Window)
            
            window_inversa = error_inversa(self)
            window_inversa.show()
            

    def boton_gauss(self):
        def intercFilas (matriz, j, i, columnas,filas):
            aux=0

            if (j>=filas-1):
                return()
            while (matriz[i][j]==0 and j<filas):
                j += 1
            for x in range(columnas):
                aux = matriz[i][x]
                matriz[i][x]=matriz[j][x]
                matriz[j][x]=aux
        
            

        def imprimeMatriz(matriz):
            print()

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    matriz[i][j] = Fraction(matriz[i][j]).limit_denominator()
                    print(matriz[i][j], end="\t")
                print()
            
            print()

        def pivoteo(filas,columnas,matrizA,vecotorPivote,vectorPivoteAux,j):
            pivoteAux = 0
            matrizTemporal = matrizA.copy()
            sumi = 0

            for i in range(filas):
                if(j==i):
                    if(matriz[i][j]==0):
                        intercFilas(matriz,j,i,columnas,filas)

                    pivoteAux = matrizTemporal[i][j]

                    for l in range(columnas):
                        if(pivoteAux==0):
                            if(matrizTemporal[i][columnas-1]!=0):
                                from views.errorInconsistente import Form_errorInconsistente
                                from PySide2.QtWidgets import QWidget

                                class error3(QWidget, Form_errorInconsistente):
                                    def __init__ (self, parent=None):
                                        super().__init__(parent)
                                        self.setupUi(self)
                                        self.setWindowFlag(Qt.Window)
                            
                                window_inconsistente = error3(self)
                                window_inconsistente.show()
                                
                            else:
                                print('La matriz tiene solucciones infinitas')   
                            for i in range(len(matriz)):
                                for j in range(len(matriz[i])):
                                    matriz[i][j] = str(Fraction(matriz[i][j]).limit_denominator())
                                    #print(matriz[i][j], end="\t")
                            matriz_error = matrizTemporal
                            matriz_error = map(str, matriz_error)
                            matriz_error = "\n".join(matriz_error)
                            self.TEXT_resultado.setText(matriz_error)
                            self.TEXT_resultado.setStyleSheet("color: rgb(255, 255, 255);")
        

                        matrizTemporal[i][l] = matrizTemporal[i][l]/pivoteAux 
                        vectorPivote[l] = matrizTemporal[i][l]
                        vectorPivoteAux[l] = matrizTemporal[i][l]

            return matrizTemporal


        #inicio de la funcion principal
        #matriz = creaMatriz1()
        #imprimeMatriz(matriz)
        from controllers.procesar_matriz import procesarMatriz

        matriz = procesarMatriz(self.path)
        filas = self.filas
        columnas = self.columnas
        pivoteAux = 0
        vectorPivote = []
        vectorPivoteAux = []
        n = 0

        print(matriz)

        for z in range(columnas):
            vectorPivote.append(None)
            vectorPivoteAux.append(None)

        #Inicio metodo Gauus-Jordan 
        for j in range(columnas-1):

            matriz = pivoteo(filas,columnas,matriz,vectorPivote,vectorPivoteAux,j)

            for i in range(filas):
                if (i != j) and (j<columnas-1):
                    n = matriz[i][j]

                #Ciclo para hacer ceron el elemento
                for k in range(columnas):
                    matriz[i][k] = (-1*n*vectorPivote[k] + matriz[i][k])

                if i == j:
                    for l in range(columnas):
                        matriz[i][l] = vectorPivoteAux[l]

                        if (matriz[i][l] == 0):
                            matriz[i][l] = 0
                    
                imprimeMatriz(matriz)

            for h in range(columnas):
                vectorPivote[h] = 0


        ####################################
        
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = str(Fraction(matriz[i][j]).limit_denominator())
                #print(matriz[i][j], end="\t")

        matriz = map(str, matriz)
        matriz = "\n".join(matriz)

        self.TEXT_resultado.setText(matriz)
        self.TEXT_resultado.setStyleSheet("color: rgb(255, 255, 255);")
        

        


