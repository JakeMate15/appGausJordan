from PySide2.QtWidgets import QApplication
from controllers.mainwindow import MainWindow


          

if __name__ == "__main__":
    app = QApplication()    
    window = MainWindow()
    window.show()
    app.exec_()

##j