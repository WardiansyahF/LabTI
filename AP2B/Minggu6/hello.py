from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("Hello World")
    
    layout = QVBoxLayout()
    label = QLabel("Pencet Tombol Dibawah ini")
    button = QPushButton("Tekan Aku!")
    
    button.clicked.connect(on_clicked)
    layout.addWidget(label)
    layout.addWidget(button)
    
    window.setLayout(layout)
    window.show()
    app.exec_()

def on_clicked():
    message = QMessageBox()
    message.setText("Hello World!")
    message.exec_()

if __name__ == "__main__":
    main()