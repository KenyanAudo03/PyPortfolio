import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from functools import partial
import math

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Auto Calculator')

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

        buttons = [
            'x^2', 'x^3', 'sqrt', 'cbrt',
            '7', '8', '9', 'Del',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '.', '-', '+',
            'C', 'sin',  # Added 'Del' for delete
            'cos', '=', 'tan',  # Added trigonometric functions
        ]

        # Create a grid layout for the buttons
        grid_layout = QGridLayout()

        # Add buttons to the grid layout
        row_val = 0
        col_val = 0

        for button in buttons:
            btn = QPushButton(button, self)
            if button == '=':
                btn.clicked.connect(self.calculate)
            elif button == 'C':
                btn.clicked.connect(self.clear)
            elif button == 'Del':
                btn.clicked.connect(self.delete)
            elif button in ('sin', 'cos', 'tan'):
                btn.clicked.connect(lambda _, op=button: self.on_trig_function_click(op))
            else:
                btn.clicked.connect(partial(self.on_button_click, button))

            grid_layout.addWidget(btn, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)

        self.setLayout(layout)

        self.show()

    def on_button_click(self, value):
        current_text = self.display.text()
        self.display.setText(current_text + value)

    def on_trig_function_click(self, operation):
        current_text = self.display.text()
        try:
            angle_in_degrees = eval(current_text)
            angle_in_radians = math.radians(angle_in_degrees)

            if operation == 'sin':
                result = math.sin(angle_in_radians)
            elif operation == 'cos':
                result = math.cos(angle_in_radians)
            elif operation == 'tan':
                result = math.tan(angle_in_radians)
            else:
                raise ValueError("Invalid trigonometric operation")

            self.display.setText(f'{operation}({angle_in_degrees}°) = {result}')
        except Exception as e:
            self.display.setText('Error')

    def clear(self):
        self.display.clear()

    def delete(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

    def calculate(self):
        try:
            expression = self.display.text()
            expression = expression.replace('sqrt', 'math.sqrt')
            result = eval(expression)
            if isinstance(result, (float, int)):
                self.display.setText(str(result))
            else:
                self.display.setText('Error')
        except Exception as e:
            self.display.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec_())
