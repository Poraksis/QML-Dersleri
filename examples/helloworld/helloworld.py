import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui



class Uygulama(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.merhaba=["merhaba onur","merhaba cocuk"]
        self.button= QtWidgets.QPushButton("Tıkla")
        self.text = QtWidgets.QLabel("Selam çocuk adam", alignment = QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.merhaba))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Uygulama()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())