import tkinter as tk
from tkinter import messagebox

# List of words and their first letters
words = [
    {"word": "وردة", "options": ["و", "ب", "ت"], "answer": "و"},
    {"word": "تفاحة", "options": ["ت", "س", "د"], "answer": "ت"},
    {"word": "فيل", "options": ["ف", "م", "ب"], "answer": "ف"},
    {"word": "بيت", "options": ["ب", "ت", "ي"], "answer": "ب"}
]

# Initialize global variables
current_word_index = 0
score = 0

# Function to check the answer
def check_answer(selected_letter):
    global current_word_index, score

    # Get the current word and its correct first letter
    word_data = words[current_word_index]
    correct_answer = word_data['answer']

    if selected_letter == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", f"Correct! The first letter is {correct_answer}.")
    else:
        messagebox.showerror("Incorrect", f"Oops! The correct first letter is {correct_answer}.")

    # Move to the next word or end the game if all words are done
    current_word_index += 1
    if current_word_index < len(words):
        display_word()
    else:
        messagebox.showinfo("Game Over", f"Game over! Your score: {score}/{len(words)}")
        root.quit()

# Function to display the word and options
def display_word():
    global current_word_index
    word_data = words[current_word_index]

    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Display the word
    word_label = tk.Label(root, text=f"What is the first letter of the word: {word_data['word']}?", font=('Arial', 16))
    word_label.pack(pady=20)

    # Display letter options as buttons
    for option in word_data['options']:
        option_button = tk.Button(root, text=option, font=('Arial', 14), width=5, command=lambda opt=option: check_answer(opt))
        option_button.pack(pady=5)

# Initialize the main window
root = tk.Tk()
root.title("Arabic Phonics Game")
root.geometry("400x300")

# Start the game by displaying the first word
display_word()

# Start the Tkinter event loop
root.mainloop()
