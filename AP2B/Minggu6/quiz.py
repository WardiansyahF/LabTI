import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QButtonGroup, QMessageBox


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Application")
        self.setFixedSize(400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.questions = [
            {"question": "What is the capital of France?", "options": [
                "Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "options": [
                "Earth", "Jupiter", "Mars", "Venus"], "answer": "Jupiter"},
            {"question": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "NaCl", "O2"], "answer": "H2O"},
        ]

        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(self.questions)

        self.question_label = QLabel(self)
        self.layout.addWidget(self.question_label)

        self.button_group = QButtonGroup(self)
        self.option_buttons = []

        for i in range(4):
            radio_button = QRadioButton(self)
            self.layout.addWidget(radio_button)
            self.option_buttons.append(radio_button)
            self.button_group.addButton(radio_button, i)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < self.total_questions:
            question = self.questions[self.current_question_index]
            self.question_label.setText(question["question"])
            options = question["options"]

            for i, option in enumerate(options):
                self.option_buttons[i].setText(option)
                self.option_buttons[i].setChecked(False)
        else:
            self.show_score()

    def check_answer(self):
        selected_button = self.button_group.checkedButton()
        if selected_button:
            answer = selected_button.text()
            correct_answer = self.questions[self.current_question_index]["answer"]

            if answer == correct_answer:
                self.score += 1

            self.current_question_index += 1
            self.next_question()
        else:
            QMessageBox.warning(
                self, "Warning", "Please select an answer before submitting.")

    def show_score(self):
        QMessageBox.information(self, "Quiz Completed", f"You scored {
                                self.score} out of {self.total_questions}.")
        self.close()


def main():
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
