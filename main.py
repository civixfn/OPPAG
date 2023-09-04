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
        "question": "Question 6: What is the most common type of plastic found in the ocean?",
        "answer": "polyethylene"
    },
    {
        "question": "Question 7: What is the term for the gradual breakdown of plastics into smaller particles?",
        "answer": "plastic degradation"
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
  #This makes the multichoice question multi choice
    if "options" in question_data:
        for i, option_button in enumerate(option_buttons):
            option_button.config(text=question_data["options"][i])
            option_button.pack()
        typed_answer_entry.pack_forget()
        typed_answer_button.pack_forget
      #This is what makes the text entry questions text entry
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
      #This adds score and shows a message for correct answers
        if user_answer == correct_answer:
            score += 1
            messagebox.showinfo("Result","Correct")
        #This shows the message for incorrect answers  
        else:
          messagebox.showerror("Result",f"Incorrect the correct answer was {correct_answer}")
            
    elif typed_answer is not None:
        correct_answer = question_data["answer"]
      #This adds score and shows a message for correct answers
        if typed_answer.lower() == correct_answer.lower():
            score += 1
            messagebox.showinfo("Result","Correct")
        #This shows the message for incorrect answers  
        else:
          messagebox.showerror("Result",f"Incorrect the correct answer was {correct_answer}")

  
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
