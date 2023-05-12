import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
import sys, re
from FeistelCipher import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.key = ''

        self.setWindowTitle("Feistel Cipher")
        self.setFixedWidth(700)
        self.setFixedHeight(500)

        # Krijimi i tabave dhe shtimi i tyre ne dritare
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.setStyleSheet("background-color: #fff;")

        # Krijimi i dy tabs
        self.encrypt_tab = QWidget()
        self.decrypt_tab = QWidget()

        # Adding to tab 1
        self.encrypt_tab_elements()

        # Adding to tab 2
        self.decrypt_tab_elements()

        # Shtimi i tabs
        self.tabs.addTab(self.encrypt_tab, "Encrypt")
        self.tabs.addTab(self.decrypt_tab, "Decrypt")

    def encrypt_tab_elements(self):
        self.title_label = QLabel("<h2>You can encrypt here!</h2>")
        self.key_label = QLabel("<h4>Enter your key here: </h4>")
        self.key_text_box = qtw.QLineEdit()

        self.plaintext_label = QLabel("<h4>Enter your plaintext here:</h4>")
        self.plaintext_box = qtw.QTextEdit()
        self.encrypt_button = qtw.QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encryption)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.title_label)
        self.layout1.addWidget(self.key_label)
        self.layout1.addWidget(self.key_text_box)
        self.layout1.addWidget(self.plaintext_label)
        self.layout1.addWidget(self.plaintext_box)
        self.layout1.addWidget(self.encrypt_button, alignment=Qt.AlignCenter)
        self.layout1.addWidget(qtw.QFrame(frameShape=qtw.QFrame.HLine))
        self.layout1.addWidget(QLabel("<h4>Encrypted text:</h4>"))

        self.ciphertext_box = qtw.QTextEdit()
        self.ciphertext_box.setReadOnly(True)
        self.layout1.addWidget(self.ciphertext_box)
        self.encrypt_tab.setLayout(self.layout1)

        # Add some styling to the buttons
        self.encrypt_button.setStyleSheet("background-color: #008CBA; color: #fff; padding: 10px;")

    def decrypt_tab_elements(self):
        self.decrypt_title_label = QLabel("<h2>You can decrypt here!</h2>")
        self.decrypt_key_label = QLabel("<h4>Enter your key here:</h4>")
        self.decrypt_key_textbox = qtw.QLineEdit()
        self.decrypt_ciphertext_label = QLabel("<h4>Enter your ciphertext:</h4>")
        self.decrypt_ciphertext_box = qtw.QTextEdit()
        self.decrypt_button = qtw.QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decryption)

        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.decrypt_title_label)
        self.layout3.addWidget(self.decrypt_key_label)
        self.layout3.addWidget(self.decrypt_key_textbox)
        self.layout3.addWidget(self.decrypt_ciphertext_label)
        self.layout3.addWidget(self.decrypt_ciphertext_box)

        self.layout3.addWidget(self.decrypt_button, alignment=Qt.AlignCenter)
        self.layout3.addWidget(qtw.QFrame(frameShape=qtw.QFrame.HLine))
        self.layout3.addWidget(QLabel("<h4>Plaintext:</h4>"))

        self.decrypt_plaintext_box = qtw.QTextEdit()
        self.decrypt_plaintext_box.setReadOnly(True)
        self.layout3.addWidget(self.decrypt_plaintext_box)
        self.decrypt_tab.setLayout(self.layout3)

        # Add some styling to the button
        self.decrypt_button.setStyleSheet("background-color: #008CBA; color: #fff; padding: 10px;")

    def encryption(self):
        if len(self.key_text_box.text()) != 16:
            MyWindow.alert("The key length must be exactly 16!")
            return None
        if not MyWindow.is_hex(self.key_text_box.text()):
            MyWindow.alert("The key must be in hex values")
            return None
        feistel = FeistelCipher(self.plaintext_box.toPlainText(), self.key_text_box.text())
        ciphertext = feistel.encrypt()
        self.ciphertext_box.setText(ciphertext)


    def decryption(self):
        if len(self.key_text_box.text()) != 16:
            MyWindow.alert("The key length must be exactly 16!")
            return None
        if not MyWindow.is_hex(self.key_text_box.text()):
            MyWindow.alert("The key must be in hex values")
            return None
        feistel = FeistelCipher(self.decrypt_ciphertext_box.toPlainText(), self.decrypt_key_textbox.text())
        plaintext = feistel.decrypt()
        self.decrypt_plaintext_box.setText(plaintext)

    @staticmethod
    def alert(message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Key Error")
        msgBox.addButton(QMessageBox.Ok)
        response = msgBox.exec_()

    @staticmethod
    def is_hex(text):
        pattern = r'^[0-9a-fA-F]+$'
        return bool(re.match(pattern, text))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the window
    window = MyWindow()
    window.show()

    # Run the main Qt loop
    sys.exit(app.exec_())
