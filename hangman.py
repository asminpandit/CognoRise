import random
import tkinter as tk
from tkinter import messagebox


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        
        self.words = ['python', 'hangman', 'programming', 'computer', 'game', 'code']
        self.word_to_guess = random.choice(self.words)
        self.guesses_left = 6
        self.display_word = ['_'] * len(self.word_to_guess)
        
        self.lbl_word = tk.Label(root, text=' '.join(self.display_word), font=('Arial', 18))
        self.lbl_word.pack(pady=10)
        
        self.lbl_guesses_left = tk.Label(root, text=f'Guesses Left: {self.guesses_left}', font=('Arial', 12))
        self.lbl_guesses_left.pack()
        
        self.entry_guess = tk.Entry(root, font=('Arial', 12))
        self.entry_guess.pack(pady=10)
        self.entry_guess.bind('<Return>', self.make_guess)
        
        self.btn_guess = tk.Button(root, text='Guess', command=self.make_guess)
        self.btn_guess.pack()
        
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()
        
    def draw_hangman(self):
        if self.guesses_left == 5:
            self.canvas.create_line(50, 180, 150, 180)
        elif self.guesses_left == 4:
            self.canvas.create_line(100, 180, 100, 20)
        elif self.guesses_left == 3:
            self.canvas.create_line(100, 20, 150, 20)
        elif self.guesses_left == 2:
            self.canvas.create_line(150, 20, 150, 40)
        elif self.guesses_left == 1:
            self.canvas.create_oval(135, 40, 165, 70)
        elif self.guesses_left == 0:
            self.canvas.create_line(150, 70, 150, 100)
            self.canvas.create_line(150, 100, 130, 130)
            self.canvas.create_line(150, 100, 170, 130)
            self.canvas.create_line(150, 85, 130, 70)
            self.canvas.create_line(150, 85, 170, 70)
            
    def make_guess(self, event=None):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            return
        
        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.display_word[i] = guess
            self.lbl_word.config(text=' '.join(self.display_word))
            if '_' not in self.display_word:
                play_again = messagebox.askyesno("Congratulations", f"You've guessed the word: {self.word_to_guess}!\n\nDo you want to play again?")
                if play_again:
                    self.reset_game()
                else:
                    self.root.quit()
        else:
            self.guesses_left -= 1
            self.lbl_guesses_left.config(text=f'Guesses Left: {self.guesses_left}')
            self.draw_hangman()
            if self.guesses_left == 0:
                play_again = messagebox.askyesno("Game Over", f"The word was: {self.word_to_guess}\n\nDo you want to play again?")
                if play_again:
                    self.reset_game()
                else:
                    self.root.quit()

    def reset_game(self):
        self.word_to_guess = random.choice(self.words)
        self.guesses_left = 6
        self.display_word = ['_'] * len(self.word_to_guess)
        self.lbl_word.config(text=' '.join(self.display_word))
        self.lbl_guesses_left.config(text=f'Guesses Left: {self.guesses_left}')
        self.canvas.delete("all")

root = tk.Tk()
hangman_game = HangmanGame(root)
root.mainloop()
