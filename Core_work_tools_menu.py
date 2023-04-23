import pyperclip
from PyQt5 import QtWidgets
from PyQt5.QtGui import *


class ClssHowDoIt(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssHowDoIt, self).__init__(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("vL")
        self.tex = QtWidgets.QTextBrowser(self)
        self.tex.setText(
            '1. Зайдите на видео-хостинг "YouTube" и скопируете ссылку на видео/плэйлист.\n2. Вставьте ссылку '
            'в поле под названием "link", нажав на кнопку "paste".\n3. Вы можете выбрать путь куда будет '
            'скачиваться файл/лы, нажав на кнопку "...".\n4. Выберите одну из двух кнопок - "V", "P"("V" - '
            'видео, "P" - плэйлист) и\nвыберите качество изображения из перечня.\n5. Нажмите на кнопку скачать. '
            'Во время скачивания кнопка будет недоступна.\nПосле скачивания она разблокируется.')
        font = QFont()
        font.setFamily("Bold")
        font.setPointSize(10)
        self.tex.setFont(font)
        self.verticalLayout.addWidget(self.tex)
        self.setWindowTitle("How do it")

    def how_do_it(self):
        dialog = ClssHowDoIt(self)
        dialog.exec_()


class ClssFunctionalList(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssFunctionalList, self).__init__(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("vL")
        self.tex = QtWidgets.QTextBrowser(self)
        self.tex.setText(
            '1. Возможность загружать видео с видео-хостина "YouTube".\n2. Возможность загружать плэйлист с '
            'видео-хостина "YouTube".\n3. Возможность выбирать качество загружаемых видео - в форматах: .mp3,'
            ' .mp4 в низком качестве, .mp4 в высоком(720p) качестве.\n4. Возможность выбирать путь загрузки '
            'файла/файлов.')
        font = QFont()
        font.setFamily("Bold")
        font.setPointSize(10)
        self.tex.setFont(font)
        self.verticalLayout.addWidget(self.tex)
        self.setWindowTitle("Functional list")

    def functional_list(self):
        dialog = ClssFunctionalList(self)
        dialog.exec_()


class ClssListErrorTemporary(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssListErrorTemporary, self).__init__(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("vL")
        self.tex = QtWidgets.QTextBrowser(self)
        with open('error_list_temporary', 'r') as f:
            self.tex.setText('\n'.join(f.readlines()))
        font = QFont()
        font.setFamily("Bold")
        font.setPointSize(10)
        self.tex.setFont(font)
        self.verticalLayout.addWidget(self.tex)
        self.setWindowTitle("Temporary list error")

    def open_error_list_temporary(self):
        dialog = ClssListErrorTemporary(self)
        dialog.exec_()

    @staticmethod
    def clear_temporary_error_log():
        open('error_list_temporary', 'w').close()

    @staticmethod
    def copy_error_list_temporary():
        with open('error_list_temporary', 'r') as file:
            pyperclip.copy('\n'.join(file.readlines()))

    @staticmethod
    def replace_temporary_error_log():
        with open('error_list_temporary', 'w') as file:
            file.write(pyperclip.paste())


class ClssListErrorPermanent(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssListErrorPermanent, self).__init__(parent)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("vL")
        self.tex = QtWidgets.QTextBrowser(self)
        with open('error_list_permanent', 'r') as f:
            self.tex.setText('\n'.join(f.readlines()))
        font = QFont()
        font.setFamily("Bold")
        font.setPointSize(10)
        self.tex.setFont(font)
        self.verticalLayout.addWidget(self.tex)
        self.setWindowTitle("Permanent list error")

    def open_error_list_permanent(self):
        dialog = ClssListErrorPermanent(self)
        dialog.exec_()

    @staticmethod
    def clear_permanent_error_log():
        open('error_list_permanent', 'w').close()

    @staticmethod
    def copy_error_list_permanent():
        with open('error_list_permanent', 'r') as file:
            pyperclip.copy('\n'.join(file.readlines()))

    @staticmethod
    def replace_permanent_error_log():
        with open('error_list_permanent', 'w') as file:
            file.write(pyperclip.paste())


def clear_all_error_logs():
    ClssListErrorTemporary.clear_temporary_error_log()
    ClssListErrorPermanent.clear_permanent_error_log()


def replace_all_error_logs():
    ClssListErrorTemporary.replace_temporary_error_log()
    ClssListErrorPermanent.replace_permanent_error_log()
