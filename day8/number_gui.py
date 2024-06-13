import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x200")
        
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Guess a number between 1 and 100").pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)
        
        tk.Button(self.root, text="Guess", command=self.check_guess).pack(pady=5)
        tk.Button(self.root, text="Show Answer", command=self.show_answer).pack(pady=5)
        tk.Button(self.root, text="Restart", command=self.restart_game).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1
            if guess < self.target_number:
                self.result_label.config(text="Higher")
            elif guess > self.target_number:
                self.result_label.config(text="Lower")
            else:
                self.result_label.config(text=f"Correct! It took you {self.guess_count} guesses.")
                self.disable_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number")
    
    def show_answer(self):
        messagebox.showinfo("Answer", f"The number was: {self.target_number}")
    
    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.enable_game()
    
    def disable_game(self):
        self.entry.config(state='disabled')
    
    def enable_game(self):
        self.entry.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
