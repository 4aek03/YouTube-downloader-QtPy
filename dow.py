from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QLinearGradient, QColor
from pytube import YouTube
from moviepy.editor import *


def download_video(url, output_path="/Applications"):
    try:
        # Создаем объект YouTube с указанной ссылкой на видео
        yt = YouTube(url)

        # Выбираем наилучшее доступное видео-разрешение для скачивания
        video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        # Скачиваем видео
        print({yt.title})
        video.download(output_path)

    except Exception as e:
        print({str(e)})

def download_audio(url, output_path="/Applications"):
    try:
        # Создаем объект YouTube с указанной ссылкой на видео
        yt = YouTube(url)

        # Выбираем наилучшее доступное видео-разрешение для скачивания
        video = yt.streams.filter(only_audio=True).first()

        # Скачиваем видео
        print({yt.title})
        video_file = video.download(output_path, filename="temp")

        # Конвертируем видео в MP3
        audio_path = f"{output_path}/{yt.title}.mp3"
        video_clip = AudioFileClip(video_file)
        video_clip.write_audiofile(audio_path)

        # Удаляем временный видео файл
        video_clip.close()
        os.remove(video_file)

    except Exception as e:
        print({str(e)})


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 300)
        mainWindow.setMinimumSize(QtCore.QSize(800, 300))
        mainWindow.setMaximumSize(QtCore.QSize(800, 300))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(219, 80, 361, 51))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(39)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLineWidth(4)
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(445, 180, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(216, 180, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 641, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color: white;\n""background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit.setFixedSize(650, 25)

        # на будущее статус бар
        # self.line_bar = QtWidgets.QProgressBar(self.centralwidget)
        # self.line_bar.setGeometry(QtCore.QRect(215, 230, 380, 21))
        # self.line_bar.setProperty("value", 24)
        # self.line_bar.setObjectName("line_bar")


        mainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "загрузчик с youtube"))


        self.label.setText(_translate("mainWindow", "загрузчик с youtube"))
        self.label.setStyleSheet("color: white;\n""background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label.setFixedSize(375, 45)


        self.pushButton.setText(_translate("mainWindow", "mp3"))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                    "color: white;\n"
                                    "background-color: rgba(0, 0, 0, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 4px; }\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgba(0, 0, 0, 40);}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color: rgba(0, 0, 0, 40); }")


        self.pushButton1.setText(_translate("mainWindow", "mp4"))
        self.pushButton1.setStyleSheet("QPushButton {\n"
                                    "color: white;\n"
                                    "background-color: rgba(0, 0, 0, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 4px; }\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgba(0, 0, 0, 40);}\n"
                                    "QPushButton:pressed {\n"
                                    "background-color: rgba(0, 0, 0, 40); }")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        # Создаем экземпляр класса Ui_mainWindow
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


        # Привязываем дополнительные действия, если необходимо
        self.ui.pushButton.clicked.connect(self.on_mp3_download_clicked)
        self.ui.pushButton1.clicked.connect(self.on_mp4_download_clicked)


        self.show()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(0, 0, 0))
        gradient.setColorAt(1, QColor(64, 64, 64))
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(65, 105, 225, 300), stop:1 rgba(123, 104, 238, 255));")


    def on_mp3_download_clicked(self):
        # Этот метод вызывается при нажатии на кнопку "mp3"
        # Вы можете определить дополнительные действия здесь
        youtube_url = self.ui.lineEdit.text()
        download_audio(youtube_url)

    def on_mp4_download_clicked(self):
        # Этот метод вызывается при нажатии на кнопку "mp4"
        # Вы можете определить дополнительные действия здесь
        youtube_url = self.ui.lineEdit.text()
        download_video(youtube_url)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())















# from setuptools import setup

# APP = ['dow.py']
# DATA_FILES = []
# OPTIONS = {
#     'packages' : ['PyQt5','pytube','moviepy.editor','PyQt5.QtGui'],
#     'iconfile':'icon.icns',
#     'argv_emulation' : True,
# }

# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )
