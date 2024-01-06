from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



def main():
    #configure the app
    global app,window,textbox1,textbox2,textbox3
    app = QApplication([])
    window = QWidget()
    window.setGeometry(400, 200, 400, 100)
    window.setWindowTitle("Pertemuan 6 - 51421514")
    #set the layout
    layout = QVBoxLayout()
    #set label
    label_judul = QLabel("MASUKKAN DATA DIRI ANDA")
    label_nama = QLabel("Nama")
    label_npm = QLabel("NPM")
    label_kelas = QLabel("Kelas")
    #set textbox
    textbox1 = QLineEdit()
    textbox2 = QLineEdit()
    textbox3 = QLineEdit()
    #set placeholder text
    textbox1.setPlaceholderText("Masukkan Nama anda")
    textbox2.setPlaceholderText("Masukkan NPM anda")
    textbox3.setPlaceholderText("Masukkan Kelas anda")
    #set button
    button_input = QPushButton("INPUT DATA")
    button_input.clicked.connect(on_clicked)

    
    #add the widgets
    layout.addWidget(label_judul, alignment=Qt.AlignCenter)
    layout.addWidget(label_nama)
    layout.addWidget(textbox1)
    layout.addWidget(label_npm)
    layout.addWidget(textbox2)
    layout.addWidget(label_kelas)
    layout.addWidget(textbox3)
    layout.addWidget(button_input)
    
    window.setLayout(layout)
    window.show()
    app.exec_()

#fungsi button ketika di klik
def on_clicked():
    message = QMessageBox()
    message.information(window, "Data Diri", "Nama: " + textbox1.text() +
                        "\nNPM: " + textbox2.text() + "\nKelas: " + textbox3.text())
    textbox1.setText("")
    textbox2.setText("")
    textbox3.setText("")


#pengkondisian
if __name__ == "__main__":
    main()
