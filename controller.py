from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    """
    Class that contains all the button functions and defines the default values
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 1
    MAX_CHANNEL = 3
    def __init__(self, *args, **kwargs):
        """
        Sets initial values and connects all the buttons with their functions.
        """
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

    def power(self) -> None:
        """
        Turns the tv status on and off and resets all values to their default values when the tv is turned off.
        """
        self.__status = not self.__status
        if not self.__status:
            self.label.raise_()
            self.slider_Vol.setValue(self.MIN_VOLUME)
            self.__volume = self.MIN_VOLUME
            self.__channel = self.MIN_CHANNEL
            self.__muted = False
        else:
            self.ch_1.setHidden(False)
            self.ch_1.raise_()

    def mute(self) -> None:
        """
        If the tv is on the status of mute is changed. When mute is on the slider is set to 0
        and the volume buttons are disabled. When mute is off volume buttons are enabled and slider
        returns to the value it was at before it was muted.
        """
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


    def channel_up(self) -> None:
        """
        If the tv is on the channel is increased and the corresponding channel image is displayed.
        """
        if self.__status:
            if self.__channel != self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
            self.channel_visual(self.__channel)

    def channel_down(self) -> None:
        """
        If the tv is on the channel is decreased and the corresponding channel image is displayed.
        """
        if self.__status:
            if self.__channel != self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
            self.channel_visual(self.__channel)

    def channel_visual(self, ch: int) -> None:
        """
        Displays the corresponding channel image and hides the other channels.
        :param ch: Gets the channel that needs to be displayed
        """
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

    def volume_up(self) -> None:
        """
        If the tv is on, increases the volume and adjusts the slider accordingly.
        """
        if self.__status:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
                self.slider_Vol.setValue(self.__volume)

    def volume_down(self) -> None:
        """
        If the tv is on, decreases the volume and adjusts the slider accordingly.
        """
        if self.__status:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
                self.slider_Vol.setValue(self.__volume)
