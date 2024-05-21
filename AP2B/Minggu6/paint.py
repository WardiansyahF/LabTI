import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QColorDialog, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint


class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint Application")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.canvas.clear_canvas)
        toolbar.addWidget(clear_button)

        color_button = QPushButton("Color")
        color_button.clicked.connect(self.canvas.select_color)
        toolbar.addWidget(color_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.canvas.save_canvas)
        toolbar.addWidget(save_button)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.pen_color = Qt.black
        self.pen_width = 3
        self.last_point = QPoint()
        self.drawing = False

        self.image = QPixmap(self.size())
        self.image.fill(Qt.white)

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawPixmap(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            pen = QPen(self.pen_color, self.pen_width,
                       Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def clear_canvas(self):
        self.image.fill(Qt.white)
        self.update()

    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color

    def save_canvas(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG Files (*.png);;All Files (*)")
        if file_path:
            self.image.save(file_path)


def main():
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
