from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 310)
        MainWindow.setStyleSheet("background-color: rgb(0, 77, 113);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exec_of_the_process = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.exec_of_the_process.setGeometry(QtCore.QRect(20, 15, 350, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exec_of_the_process.setFont(font)
        self.exec_of_the_process.setStyleSheet("border: 2px solid #A4004D;\n"
            "background-color: rgb(0, 77, 113);\n"
            "color: white;")
        self.exec_of_the_process.setPlainText("")
        self.exec_of_the_process.setObjectName("exec_of_the_process")
        self.video_link = QtWidgets.QLineEdit(self.centralwidget)
        self.video_link.setGeometry(QtCore.QRect(20, 185, 350, 30))
        self.video_link.setStyleSheet("border: 2px solid #A4004D;\n"
            "background-color: rgb(0, 77, 113);\n"
            "color: white;")
        self.video_link.setObjectName("video_link")
        self.download_but = QtWidgets.QPushButton(self.centralwidget)
        self.download_but.setGeometry(QtCore.QRect(20, 225, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_but.setFont(font)
        self.download_but.setStyleSheet("QPushButton{\n"
"border: 2px solid #A4004D;\n"
"background-color: rgb(0, 77, 113);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: rgb(0, 64, 94);\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: rgb(0, 64, 94);\n"
"color: white;\n"
"}")
        self.download_but.setObjectName("download_but")
        self.save_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_but.setGeometry(QtCore.QRect(20, 265, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_but.setFont(font)
        self.save_but.setStyleSheet("QPushButton{\n"
"border: 2px solid #A4004D;\n"
"background-color: rgb(0, 77, 113);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"border: 2px solid #A4004D;\n"
"background-color: rgb(0, 64, 94);\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 2px solid white;\n"
"background-color: rgb(0, 64, 94);\n"
"color: white;\n"
"}\n"
"")
        self.save_but.setObjectName("save_but")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.exec_of_the_process.setPlaceholderText(_translate("MainWindow", "Execution process.."))
        self.video_link.setPlaceholderText(_translate("MainWindow", "https://www.youtube.com/VideoID"))
        self.download_but.setText(_translate("MainWindow", "Download video"))
        self.save_but.setText(_translate("MainWindow", "Select a folder to save"))
