from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 1
    MAX_CHANNEL = 3
    def __init__(self, *args, **kwargs):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_Power.clicked.connect(lambda: self.power())
        self.button_Mute.clicked.connect(lambda: self.mute())
        self.button_ChannelUp.clicked.connect(lambda: self.channel_up())
        self.button_ChannelDown.clicked.connect(lambda: self.channel_down())
        self.button_VolUp.clicked.connect(lambda: self.volume_up())
        self.button_VolDown.clicked.connect(lambda: self.volume_down())

    def power(self):
        self.__status = not self.__status
        if not self.__status:
            self.label.raise_()
            self.slider_Vol.setValue(0)
        else:
            self.ch_1.setHidden(False)
            self.ch_1.raise_()

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.slider_Vol.setValue(0)
                self.button_VolUp.setEnabled(False)
                self.button_VolDown.setEnabled(False)
            else:
                self.slider_Vol.setValue(self.__volume)
                self.button_VolUp.setEnabled(True)
                self.button_VolDown.setEnabled(True)


    def channel_up(self):
        if self.__status:
            if self.__channel != self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
            self.channel_visual(self.__channel)

    def channel_down(self):
        if self.__status:
            if self.__channel != self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
            self.channel_visual(self.__channel)

    def channel_visual(self, ch):
        if ch == 1:
            self.ch_1.setHidden(False)
            self.ch_2.setHidden(True)
            self.ch_3.setHidden(True)
            self.ch_4.setHidden(True)
            self.ch_1.raise_()
        elif ch == 2:
            self.ch_1.setHidden(True)
            self.ch_2.setHidden(False)
            self.ch_3.setHidden(True)
            self.ch_4.setHidden(True)
            self.ch_2.raise_()
        elif ch == 3:
            self.ch_1.setHidden(True)
            self.ch_2.setHidden(True)
            self.ch_3.setHidden(False)
            self.ch_4.setHidden(True)
            self.ch_3.raise_()
        elif ch == 4:
            self.ch_1.setHidden(True)
            self.ch_2.setHidden(True)
            self.ch_3.setHidden(True)
            self.ch_4.setHidden(False)
            self.ch_4.raise_()

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
                self.slider_Vol.setValue(self.__volume)

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
                self.slider_Vol.setValue(self.__volume)
