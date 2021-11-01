import os
import sys
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow


class Downloader(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None

    def run(self):
        self.my_signal.emit('Download process is running!')

        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([self.url])

        self.my_signal.emit('Download process is complete!')
        self.my_signal.emit('finish')

    def init_args(self, url):
        self.url = url


class Gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.download_folder = None
        self.ui.save_but.clicked.connect(self.get_folder)
        self.ui.download_but.clicked.connect(self.start)
        self.my_thread = Downloader()
        self.my_thread.my_signal.connect(self.handler)

    def start(self):
        if len(self.ui.video_link.text()) > 10:
            if self.download_folder != None:
                link = self.ui.video_link.text()
                self.my_thread.init_args(link)
                self.my_thread.start()
                self.locker(True)
            else:
                QtWidgets.QMessageBox.warning(self,
                                              'Error',
                                              'You have not selected a folder!'
                                              )
        else:
            QtWidgets.QMessageBox.warning(self, 'Error',
                                          'Video link not specified!'
                                          )

    def get_folder(self):
        self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Select a folder to save'
        )
        os.chdir(self.download_folder)

    def handler(self, value):
        if value == 'finish':
            self.locker(False)
        else:
            self.ui.exec_of_the_process.appendPlainText(value)

    def locker(self, lock_value):
        base = [self.ui.save_but, self.ui.download_but]

        for item in base:
            item.setDisabled(lock_value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Gui()
    win.show()

    sys.exit(app.exec_())
