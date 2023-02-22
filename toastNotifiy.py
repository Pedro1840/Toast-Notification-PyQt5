import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Toast(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

        if parent:
            main_window_geo = self.parent().frameGeometry()

            # Obter a posição da janela principal da aplicação
            main_window_pos = self.parent().pos()

            # Ajustar as coordenadas do toast em relação à janela principal
            toast_x = main_window_pos.x() + main_window_geo.width() - self.width() - 10
            toast_y = main_window_pos.y() + 50

            # Definir a posição do toast
            self.move(toast_x, toast_y)

        self.initUI()

    def initUI(self):
        self.label = QLabel(self.text)
        self.label.setAlignment(Qt.AlignCenter)
        self.setAutoFillBackground(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.hide)
        
    def show(self):
        self.timer.start()
        super().show()

    def hide(self):
        super().hide()
        self.timer.stop()

    def paintEvent(self, event):
        border_color = "#1c1c1c"
        background_color = "#323232"
        radius = 10
        margin = 10
        width = self.width()
        height = self.height()

        # Estilo
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRoundedRect(QRectF(margin, margin, width - margin * 2, height - margin * 2), radius, radius)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.NoBrush)
        #painter.drawRoundedRect(QRectF(margin, margin, width - margin * 2, height - margin * 2), radius, radius)
        painter.drawRoundedRect(self.rect(), 5, 5)

    def get_position(self):
        # PySide6
        ##desktop = QGuiApplication.primaryScreen().availableGeometry()

        #PyQt5
        desktop = QDesktopWidget().availableGeometry()
        
        return desktop.width() - self.width(), 0


# Para Utilizar o Notification Adicione isto na sua MainWindow 
# Fique a Vontade para Estilizar ela da sua maneira :)

##EXAMPLE##

#self.toast = Toast('My Toast Notification', self)
#self.toast.show()