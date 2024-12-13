import tkinter as tk
from tkinter import messagebox
import json
import random

class QuizGameGUI:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Game")

        # Calculate window size as half of the screen size
        window_width = int(master.winfo_screenwidth() / 2)
        window_height = int(master.winfo_screenheight() / 2)
        self.master.geometry(f"{window_width}x{window_height}+{int((master.winfo_screenwidth() - window_width) / 2)}+{int((master.winfo_screenheight() - window_height) / 2)}")

        self.questions = questions
        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(master, text="", font=("consolas", 26))
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value=i + 1, font=("consolas", 24))
            radio_button.pack(anchor='w', pady=5)
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Helvetica", 14))
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])

            for i, option in enumerate(question_data['options']):
                self.radio_buttons[i].config(text=option)

        else:
            self.show_final_score()

    def next_question(self):
        if self.radio_var.get():
            selected_option = int(self.radio_var.get())
            question_data = self.questions[self.current_question_index]

            # Hide the question label and radio buttons
            self.question_label.pack_forget()
            for radio_button in self.radio_buttons:
              radio_button.pack_forget()

            # Check if the selected option is correct
            if question_data['options'][selected_option - 1] == question_data['answer']:
                self.score += 1
                self.flash_background('green')  # Flash green for correct answer
            else:
                self.flash_background('red')  # Flash red for incorrect answer

            # Wait for around 2 seconds (2000 milliseconds) before moving on to the next question
            self.master.after(50, self.restore_background)

        else:
            messagebox.showinfo("Error", "Please select an option.")

    def flash_background(self, color):
        self.master.config(bg=color)

    def restore_background(self):
        self.master.config(bg='SystemButtonFace')  # Replace with the default background color

        # Show the question label and radio buttons for the next question
        self.question_label.pack(pady=20)
        for radio_button in self.radio_buttons:
            radio_button.pack(anchor='w', pady=5)

        self.current_question_index += 1
        self.radio_var.set(None)
        self.load_question()

    def show_final_score(self):
        # messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score >= 7:
            messagebox.showinfo("CONGRADULATION 😊😉",f"Your final score is: {self.score}/{len(self.questions)}")
        elif self.score >= 5:
            messagebox.showinfo("AVERAGE.PUT MORE EFFORT",f"Your final score is: {self.score}/{len(self.questions)}")
        else:
            messagebox.showinfo("YOU NEED TO READ.",f"Your final score is: {self.score}/{len(self.questions)}")
        self.master.destroy()
        

# Read questions from the JSON file and shuffle them
def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    random.shuffle(questions)
    return questions

def load_options_from_json(file_path):
    with open(file_path, 's') as file:
        options = json.load(file)
        random.shuffle(options)
        return options

# Example questions
quiz_questions = load_questions_from_json("questions.json")

# Create and start the Tkinter app
root = tk.Tk()
quiz_app = QuizGameGUI(root, quiz_questions)
root.mainloop()