from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


def main():
    # Configure the app
    global app, window, textbox1, textbox2, textbox3
    app = QApplication([])
    window = QWidget()
    window.setGeometry(400, 200, 400, 200)
    window.setWindowTitle("Pertemuan 6 - 51421514")

    # Set the layout
    layout = QVBoxLayout()
    # Add margin for better appearance
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)  # Add spacing between widgets

    # Set labels
    label_judul = QLabel("MASUKKAN DATA DIRI ANDA")
    label_judul.setAlignment(Qt.AlignCenter)
    label_judul.setStyleSheet(
        "font-size: 16px; font-weight: bold; color: white;")

    label_nama = QLabel("Nama")
    label_nama.setStyleSheet("color: white;")

    label_npm = QLabel("NPM")
    label_npm.setStyleSheet("color: white;")

    label_kelas = QLabel("Kelas")
    label_kelas.setStyleSheet("color: white;")

    # Set textboxes
    textbox1 = QLineEdit()
    textbox2 = QLineEdit()
    textbox3 = QLineEdit()

    # Set placeholder text
    textbox1.setPlaceholderText("Masukkan Nama anda")
    textbox2.setPlaceholderText("Masukkan NPM anda")
    textbox3.setPlaceholderText("Masukkan Kelas anda")

    # Set styles for textboxes
    textbox1.setStyleSheet("background-color: white;")
    textbox2.setStyleSheet("background-color: white;")
    textbox3.setStyleSheet("background-color: white;")

    # Set button
    button_input = QPushButton("INPUT DATA")
    button_input.setStyleSheet(
        "background-color: darkgreen; color: white; font-weight: bold;")
    button_input.clicked.connect(on_clicked)

    # Set background color of the window to a shade of green
    palette = window.palette()
    palette.setColor(QPalette.Window, QColor(
        "#228B22"))  # Forest Green background
    window.setPalette(palette)

    # Add widgets to the layout
    layout.addWidget(label_judul)
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

# Function to handle button click


def on_clicked():
    name = textbox1.text()
    npm = textbox2.text()
    kelas = textbox3.text()

    if not name or not npm or not kelas:
        QMessageBox.warning(window, "Input Error", "Semua kolom harus diisi!")
        return

    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setWindowTitle("Data Diri")
    message.setText(f"Nama: {name}\nNPM: {npm}\nKelas: {kelas}")
    message.setStandardButtons(QMessageBox.Ok)
    message.exec_()

    textbox1.setText("")
    textbox2.setText("")
    textbox3.setText("")


# Conditional to run the main function
if __name__ == "__main__":
    main()
