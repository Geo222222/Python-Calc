from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut
import sys
from logic import evaluate_expression


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Calculator")
        self.setMinimumSize(300, 400)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_line = QLineEdit()
        self.input_line.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_line.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.input_line)

        self.grid = QGridLayout()
        self.buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)
        ]

        for text, row, col, rowspan=1, colspan=1 in self.buttons:
            btn = QPushButton(text)
            btn.setFixedSize(60, 60)
            btn.setStyleSheet("font-size: 18px;")
            self.grid.addWidget(btn, row, col, rowspan, colspan)
            btn.clicked.connect(self.handle_button)

        self.layout.addLayout(self.grid)
        self.setLayout(self.layout)

        # Clipboard shortcuts
        QShortcut(QKeySequence("Ctrl+C"), self, activated=self.copy_to_clipboard)
        QShortcut(QKeySequence("Ctrl+V"), self, activated=self.paste_from_clipboard)

    def handle_button(self):
        sender = self.sender().text()
        if sender == 'C':
            self.input_line.clear()
        elif sender == '=':
            try:
                result = evaluate_expression(self.input_line.text())
                self.input_line.setText(str(result))
            except Exception:
                QMessageBox.critical(self, "Error", "Invalid expression")
        else:
            self.input_line.setText(self.input_line.text() + sender)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.handle_button_by_text('=')
        elif event.key() == Qt.Key.Key_Backspace:
            self.input_line.backspace()
        elif event.key() == Qt.Key.Key_Escape:
            self.input_line.clear()
        else:
            self.input_line.setText(self.input_line.text() + event.text())

    def handle_button_by_text(self, text):
        self.input_line.setText(self.input_line.text() + text)
        self.handle_button()

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.input_line.text())

    def paste_from_clipboard(self):
        pasted = QApplication.clipboard().text()
        if pasted.replace('.', '', 1).isdigit():
            self.input_line.setText(self.input_line.text() + pasted)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
