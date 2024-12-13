import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QProgressBar
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, QTimer

class SetupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(200, 200, 300, 100)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Player 1: Choose your symbol")
        self.layout.addWidget(self.label)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.x_button = QPushButton("X")
        self.x_button.clicked.connect(lambda checked, symbol='X': self.symbol_selected(symbol))
        self.button_layout.addWidget(self.x_button)

        self.o_button = QPushButton("O")
        self.o_button.clicked.connect(lambda checked, symbol='O': self.symbol_selected(symbol))
        self.button_layout.addWidget(self.o_button)

        self.selected_symbol = None

    def symbol_selected(self, symbol):
        self.selected_symbol = symbol
        self.close()


class MainWindow(QMainWindow):
    def __init__(self, player1_symbol, player2_symbol):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.outcome_label = QLabel(" ")
        self.outcome_label.setStyleSheet("font-size: 18px; color: grey;")
        self.layout.addWidget(self.outcome_label)

        self.grid_layout = QVBoxLayout()
        self.grid_layout.setSpacing(5)  # Reduce vertical spacing between rows in the grid
        self.layout.addLayout(self.grid_layout)

        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

        self.current_player = 1  # 1 for Player 1, 2 for Player 2
        self.player_symbols = {1: player1_symbol, 2: player2_symbol}
        self.player_colors = {player1_symbol: QColor('lightblue'), player2_symbol: QColor('lightcoral')}
        self.setup_buttons()

        self.restart_button = QPushButton("Restart Game")
        self.restart_button.clicked.connect(self.restart_game)
        self.layout.addWidget(self.restart_button)
        self.restart_button.setVisible(False)  # Initially hidden

        self.game_mode = None  # 'human' for 1 v 1, 'ai' for v AI
        self.ai_symbol = 'O' if player1_symbol == 'X' else 'X'
        self.ai_turn = False  # AI turn indicator

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)
        self.progress_bar.setVisible(False)

    def setup_buttons(self):
        for i in range(3):
            row_layout = QHBoxLayout()
            for j in range(3):
                button = QPushButton('')
                button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)  # Set button size policy
                button.setStyleSheet(f'font-size: 24px; background-color: {self.palette().window().color().name()}; color: {self.player_colors[self.player_symbols[1]].name()};')
                button.clicked.connect(lambda checked, i=i, j=j: self.button_click(i, j))
                row_layout.addWidget(button)
                self.buttons[i][j] = button
            self.grid_layout.addLayout(row_layout)

    def button_click(self, i, j):
        if self.game_mode == 'ai' and self.ai_turn:
            return  # AI's turn, do nothing

        if not self.buttons[i][j].text():
            self.buttons[i][j].setText(self.player_symbols[self.current_player])
            self.buttons[i][j].setEnabled(False)  # Disable button after player's move
            self.buttons[i][j].setStyleSheet(f'background-color: {self.player_colors[self.player_symbols[self.current_player]].name()}; color: white;')

            if self.check_win(self.player_symbols[self.current_player]):
                self.update_outcome_label(f"Player {self.current_player} wins!", 'blue')
                self.highlight_win_line(self.player_symbols[self.current_player])
                self.end_game()
            elif self.check_draw():
                self.update_outcome_label("It's a draw!", 'red')
                self.end_game()
            else:
                self.current_player = 2 if self.current_player == 1 else 1

                if self.game_mode == 'ai':
                    self.ai_turn = True
                    self.progress_bar.setVisible(True)
                    self.progress_bar.setValue(0)  # Reset progress bar
                    self.progress_bar.setFormat("Thinking...")

                    self.ai_move()

    def ai_move(self):
        # Simulating AI move processing time with a timer
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start()

    def update_progress_bar(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)
        else:
            self.timer.stop()
            self.make_ai_move()

    def make_ai_move(self):
        best_move = self.get_best_move()
        if best_move:
            i, j = best_move
            self.progress_bar.setVisible(False)
            self.buttons[i][j].setText(self.ai_symbol)
            self.buttons[i][j].setEnabled(False)  # Disable button after AI's move
            self.buttons[i][j].setStyleSheet(f'background-color: {self.player_colors[self.ai_symbol].name()}; color: white;')

            if self.check_win(self.ai_symbol):
                self.update_outcome_label("AI wins!", 'blue')
                self.highlight_win_line(self.ai_symbol)
                self.end_game()
            elif self.check_draw():
                self.update_outcome_label("It's a draw!", 'red')
                self.end_game()

            self.current_player = 1
            self.ai_turn = False

    def get_best_move(self):
        # Minimax algorithm for AI move
        best_score = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].text() == '':
                    self.buttons[i][j].setText(self.ai_symbol)
                    score = self.minimax(False)
                    self.buttons[i][j].setText('')
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def minimax(self, is_maximizing):
        # Base cases for minimax recursion
        if self.check_win(self.ai_symbol):
            return 1
        elif self.check_win(self.player_symbols[1]):
            return -1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].text() == '':
                        self.buttons[i][j].setText(self.ai_symbol)
                        score = self.minimax(False)
                        self.buttons[i][j].setText('')
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].text() == '':
                        self.buttons[i][j].setText(self.player_symbols[1])
                        score = self.minimax(True)
                        self.buttons[i][j].setText('')
                        best_score = min(score, best_score)
            return best_score

    def check_win(self, player_symbol):
        # Check rows and columns for win
        for i in range(3):
            if all(self.buttons[i][j].text() == player_symbol for j in range(3)):
                return True
            if all(self.buttons[j][i].text() == player_symbol for j in range(3)):
                return True
        # Check diagonals for win
        if all(self.buttons[i][i].text() == player_symbol for i in range(3)):
            return True
        if all(self.buttons[i][2 - i].text() == player_symbol for i in range(3)):
            return True
        return False

    def highlight_win_line(self, symbol):
        # Highlight rows and columns for win
        for i in range(3):
            if all(self.buttons[i][j].text() == symbol for j in range(3)):
                for j in range(3):
                    self.buttons[i][j].setStyleSheet(f'background-color: {self.player_colors[symbol].darker(150).name()}; color: white;')
        for j in range(3):
            if all(self.buttons[i][j].text() == symbol for i in range(3)):
                for i in range(3):
                    self.buttons[i][j].setStyleSheet(f'background-color: {self.player_colors[symbol].darker(150).name()}; color: white;')
        # Highlight diagonals for win
        if all(self.buttons[i][i].text() == symbol for i in range(3)):
            for i in range(3):
                self.buttons[i][i].setStyleSheet(f'background-color: {self.player_colors[symbol].darker(150).name()}; color: white;')
        if all(self.buttons[i][2 - i].text() == symbol for i in range(3)):
            for i in range(3):
                self.buttons[i][2 - i].setStyleSheet(f'background-color: {self.player_colors[symbol].darker(150).name()}; color: white;')

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button.text() == '':
                    return False
        return True

    def end_game(self):
        # End of game actions
        self.restart_button.setVisible(True)
        self.disable_buttons()

    def disable_buttons(self):
        # Disable all buttons at the end of game
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def restart_game(self):
        self.restart_button.setVisible(False)
        self.outcome_label.setText(" ")
        self.current_player = 1
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
                self.buttons[i][j].setEnabled(True)
                self.buttons[i][j].setStyleSheet(f'background-color: {self.palette().window().color().name()}; color: {self.player_colors[self.player_symbols[1]].name()};')

    def update_outcome_label(self, text, color):
        # Update outcome label
        self.outcome_label.setText(text)
        self.outcome_label.setStyleSheet(f"font-size: 18px; color: {color};")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    setup_window = SetupWindow()
    setup_window.show()
    app.exec()

    if setup_window.selected_symbol is not None:
        player1_symbol = setup_window.selected_symbol
        player2_symbol = 'O' if player1_symbol == 'X' else 'X'

        main_window = MainWindow(player1_symbol, player2_symbol)
        main_window.game_mode = 'ai'
        main_window.show()

    sys.exit(app.exec())