import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(QSize(300, 300))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.buttons = {}
        self.current_player = 'X'

        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(self.make_move)
                self.grid_layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

    def make_move(self):
        button = self.sender()
        if button.text() == "":
            button.setText(self.current_player)
            if self.check_winner():
                QMessageBox.information(self, "Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(button.text() != "" for button in self.buttons.values()):
                QMessageBox.information(self, "Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for line in lines:
            if (self.buttons[line[0]].text() == self.buttons[line[1]].text() == self.buttons[line[2]].text()) and self.buttons[line[0]].text() != "":
                return True
        return False

    def reset_board(self):
        for button in self.buttons.values():
            button.setText("")
        self.current_player = 'X'

def main():
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
