from FF import *

def summa1(self):
    self.pushButton.clicked.connect(self.result1)


def result1(self):
    dlin = self.lineEdit.text()
    dlin = int(dlin)
    ch = self.lineEdit_2.text()
    ch = int(ch)
    vis = self.lineEdit_3.text()
    vis = int(vis)

    rez1 = dlin * ch * vis/ 5000
    self.lineEdit_4.setText(str(rez1))


Ui_MainWindow.summa1 = summa1
Ui_MainWindow.result1 = result1


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.summa1()
    MainWindow.show()
    sys.exit(app.exec_())