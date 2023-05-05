from controller import *

def main():
    app = QApplication([])
    MainWindow = Controller()
    MainWindow.show()
    app.exec_()



if __name__ == '__main__':
    main()