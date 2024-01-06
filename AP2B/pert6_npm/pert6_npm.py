from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



def main():
    #configure the app
    global app,window,nama_textbox,npm_textbox,kelas_textbox #definisi variabel global
    app = QApplication([])
    window = QWidget()
    window.setGeometry(400, 600, 400, 100)
    window.setWindowTitle("Pertemuan 6 - 50421583")
    #set the layout
    layout = QVBoxLayout()
    #set label
    label_judul = QLabel("MASUKKAN DATA DIRI ANDA")
    label_nama = QLabel("Nama")
    label_npm = QLabel("NPM")
    label_kelas = QLabel("Kelas")
    #set textbox
    nama_textbox = QLineEdit()
    npm_textbox = QLineEdit()
    kelas_textbox = QLineEdit()
    #set placeholder text
    nama_textbox.setPlaceholderText("Masukkan Nama anda")
    npm_textbox.setPlaceholderText("Masukkan NPM anda")
    kelas_textbox.setPlaceholderText("Masukkan Kelas anda")
    button_input = QPushButton("INPUT DATA")
    button_input.clicked.connect(on_clicked)

    
    #add the widgets
    layout.addWidget(label_judul, alignment=Qt.AlignCenter)
    layout.addWidget(label_nama)
    layout.addWidget(nama_textbox)
    layout.addWidget(label_npm)
    layout.addWidget(npm_textbox)
    layout.addWidget(label_kelas)
    layout.addWidget(kelas_textbox)
    layout.addWidget(button_input)
    
    window.setLayout(layout)
    window.show()
    app.exec_()


def on_clicked():
    message = QMessageBox()
    message.information(window, "Data Diri", "Nama: " + nama_textbox.text() +
                        "\nNPM: " + npm_textbox.text() + "\nKelas: " + kelas_textbox.text())
    nama_textbox.setText("")
    npm_textbox.setText("")
    kelas_textbox.setText("")



if __name__ == "__main__":
    main()
