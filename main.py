import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("Plastic Pollution Quiz")
# This is the size of the window that the game is played on
app.geometry("400x300")
# This is the background colour of the game
app.configure(bg="blue")

# Define the quiz questions and multiple-choice options
questions = [
    {
        "question": "Question 1: What is the most common type of plastic found in the ocean?",
        "options": ["polyethylene", "microplastics", "polypropylene", "polycarbonate"],
        "correct": "polyethylene"
    },
    {
        "question": "Question 2: What is the term for the gradual breakdown of plastics into smaller particles?",
        "options": ["plastic degradation", "plastic combustion", "plastic breakdown", "plastic destruction"],
        "correct": "plastic degradation"
    },
    {
        "question": "Question 3: Which marine animals are particularly at risk due to plastic pollution?",
        "options": ["Fish", "Dolphins", "Sea turtles, seabirds, and marine mammals", "Sharks"],
        "correct": "Sea turtles, seabirds, and marine mammals"
    },
    {
        "question": "Question 4: What is the long-term environmental impact of plastic pollution on marine ecosystems?",
        "options": ["Habitat destruction, harm to marine life", "Global Warming", "World Hunger", "Earthquakes"],
        "correct": "Habitat destruction, harm to marine life"
    },
    {
        "question": "Question 5: What is the primary source of plastic pollution in our oceans?",
        "options": ["Industrial Waste", "Natural debris", "Household Garbage", "Space debris"],
        "correct": "Household Garbage"
    }
]

# Additional easy questions about plastic pollution in the ocean that answers will be typed
questions += [
    {
        "question": "Question 6: How many years does it take for a plastic bottle to decompose in the ocean?",
        "answer": 450
    },
    {
        "question": "Question 7: What percentage of marine waste is estimated to be plastic?",
        "answer": 80
    }
]

# Variables to track current question and score
current_question = 0
score = 0

# Function to display the current question and options
def display_question():
    question_data = questions[current_question]
    question_label.config(text=question_data["question"])

    # Hide or show widgets based on question type
    if "options" in question_data:
        for i, option_button in enumerate(option_buttons):
            option_button.config(text=question_data["options"][i])
            option_button.pack()
        typed_answer_entry.pack_forget()
        typed_answer_button.pack_forget()
    elif "answer" in question_data:
        for option_button in option_buttons:
            option_button.pack_forget()
        typed_answer_entry.pack()
        typed_answer_button.pack()

    # Update the score label
    score_label.config(text=f"Score: {score}")

# Function to check the answer and move to the next question

def check_answer(selected_option=None, typed_answer=None):
    global current_question, score
    question_data = questions[current_question]

    if selected_option is not None:
        user_answer = question_data["options"][selected_option]
        correct_answer = question_data["correct"]
        if user_answer == correct_answer:
            score += 1
            messagebox.showinfo("Correct","You got the correct answer")
        else:
            messagebox.showerror("Incorrect", f"Incorrect answer the correct answer was: {correct_answer}")
    elif typed_answer is not None:
        try:
          # This turns the string into a numeric value
            typed_answer = int(typed_answer)
          # This creates a boundary
            if typed_answer >= 0:
                correct_answer = question_data["answer"]
                if typed_answer == correct_answer:
                    score += 1
                    messagebox.showinfo("Correct","You got the correct answer")
                else:
                    messagebox.showerror("Incorrect", f"Incorrect answer the correct answer was: {correct_answer}")
            else:
                messagebox.showerror("Invalid", "Please enter a positive number next time.")
        except ValueError:
            messagebox.showerror("Invalid", "Please enter a valid positive number next time.")

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
    option_buttons.append(option_button)

typed_answer_entry = tk.Entry(app, width=40)

typed_answer_button = tk.Button(app, text="Submit Typed Answer", width=40,
                                command=lambda: check_answer(typed_answer=typed_answer_entry.get()))

score_label = tk.Label(app, text="Score: 0", bg="blue", fg="white", font=("Arial", 12))
score_label.pack(pady=10)

# Start the quiz
display_question()

# Run the Tkinter main loop
app.mainloop()