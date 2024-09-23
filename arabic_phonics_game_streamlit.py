import streamlit as st

# List of words and their first letters
words = [
    {"word": "وردة", "options": ["و", "ب", "ت"], "answer": "و"},
    {"word": "تفاحة", "options": ["ت", "س", "د"], "answer": "ت"},
    {"word": "فيل", "options": ["ف", "م", "ب"], "answer": "ف"},
    {"word": "بيت", "options": ["ب", "ت", "ي"], "answer": "ب"}
]

# Initialize session state to track the word index and score
if 'current_word_index' not in st.session_state:
    st.session_state.current_word_index = 0

if 'score' not in st.session_state:
    st.session_state.score = 0

# Function to check the answer
def check_answer(selected_letter):
    word_data = words[st.session_state.current_word_index]
    correct_answer = word_data['answer']

    if selected_letter == correct_answer:
        st.session_state.score += 1
        st.success(f"Correct! The first letter is {correct_answer}.")
    else:
        st.error(f"Oops! The correct first letter is {correct_answer}.")

    st.session_state.current_word_index += 1

# Function to display the word and options
def display_word():
    if st.session_state.current_word_index < len(words):
        word_data = words[st.session_state.current_word_index]
        
        st.write(f"### What is the first letter of the word: {word_data['word']}?")
        
        for option in word_data['options']:
            if st.button(option):
                check_answer(option)
    else:
        st.write(f"## Game over! Your score: {st.session_state.score}/{len(words)}")
        st.button("Restart", on_click=restart_game)

# Function to restart the game
def restart_game():
    st.session_state.current_word_index = 0
    st.session_state.score = 0

# Display the current word and options
display_word()
