import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("Plastic Pollution Quiz")
app.geometry("300x200")
app.configure(bg="blue")

# Define the quiz questions and multiple-choice options
questions = [
    {
        "question": "Question 1: How long does it take for a plastic bottle to decompose in the ocean?",
        "options": ["50 years", "100 years", "450 years", "1000 years"],
        "correct": "450 years"
    },
    {
        "question": "Question 2: What percentage of marine waste is estimated to be plastic?",
        "options": ["10%", "50%", "80%", "100%"],
        "correct": "80%"
    },
    {
        "question": "Question 3: Which marine animals are particularly at risk due to plastic pollution?",
        "options": ["Fish", "Dolphins", "Sea turtles, seabirds, and marine mammals", "Sharks"],
        "correct": "Sea turtles, seabirds, and marine mammals"
    },
    # Add more questions here
 {
    "question": "Question 4: What is the long-term environmental impact of plastic pollution on marine ecosystems?",
    "options": ["Habitat destruction, harm to marine life", "Global Warming", "World Hunger", "Earthquakes"],
    "correct": "Habitat destruction, harm to marine life"
},
  {
    "question":"What is the primary source of plastic pollution in our oceans?",
    "options":["Industrial Waste", "Natural debris", "Household Garbage", "Space debris"],
    "correct": "Household Garbage"

  }
  

]

# Variables to track current question and score
current_question = 0
score = 0

# Function to display the current question and options
def display_question():
    question_data = questions[current_question]
    question_label.config(text=question_data["question"])
    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(text=option, state=tk.NORMAL)
    score_label.config(text=f"Score: {score}")

# Function to check the answer and move to the next question
def check_answer(selected_option):
    global current_question, score
    question_data = questions[current_question]
    user_answer = question_data["options"][selected_option]
    correct_answer = question_data["correct"]

    if user_answer == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()

# Function to display the final result
def show_result():
    messagebox.showinfo("Quiz Result", f"You got {score} out of {len(questions)} questions correct.")
    app.destroy()

# Create GUI elements
question_label = tk.Label(app, text="", wraplength=500, bg="blue", fg="white", font=("Arial", 16))
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    option_button = tk.Button(app, text="", width=40, command=lambda selected_option=i: check_answer(selected_option))
    option_button.pack(pady=5)
    option_buttons.append(option_button)

score_label = tk.Label(app, text="Score: 0", bg="blue", fg="white", font=("Arial", 12))
score_label.pack(pady=10)

# Start the quiz
display_question()

 
# Run the Tkinter main loop
app.mainloop()
