import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui



class Uygulama(QtWidgets.QWidget):
    """uygulama ekranımızın gelmesi için bir kaç seçenek var bunlardan biri widget ekranı
    o yüzden bu sınıfı genişletip üzerinde özelleştirmeler yapmalıyız.
    """
    def __init__(self) -> None:
        super().__init__()
        """Uyguluma ilk açıldığında üstünde yazı button gibi görsel elemanları oluşturduk."""
        self.merhaba=["merhaba onur","merhaba cocuk"]
        self.button= QtWidgets.QPushButton("Tıkla")
        self.text = QtWidgets.QLabel("Selam çocuk adam", alignment = QtCore.Qt.AlignCenter)
        #Programın yerleşim biçiminibelirleyip oluşan kompanentleri içine yükledik.
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        #Buttonun çalıştıracağı fonksiyonu belirttik.
        self.button.clicked.connect(self.magic)
    
    #Yukarıda tetiklediğimiz fonksiyonun görevini belirttik.
    #text objesinin yazı eğerini random bir yazı ile değiştirecek.
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.merhaba))


#Burada prohramımızı başlatmak için kullanılan kalıp kodlar bulunmakta.
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Uygulama()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())