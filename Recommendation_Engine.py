#!/usr/bin/env python3
import tkinter as tk
from collections import defaultdict
import matplotlib.pyplot as plt
from tkinter import ttk

# Dictionary to store the characteristics of each approach
approaches = {
    "Kanban": {
        "Project Lifecycle Model": "Continuous",
        "Flexibility": "High",
        "Customer Involvement": "Moderate",
        "Iterative Development": "No",
        "Time Management": "Flexible",
    },
    "PRINCE2": {
        "Project Lifecycle Model": "Staged",
        "Flexibility": "Low",
        "Customer Involvement": "Moderate",
        "Iterative Development": "No",
        "Time Management": "Fixed",
    },
    "Nexus": {
        "Project Lifecycle Model": "Iterative",
        "Flexibility": "High",
        "Customer Involvement": "High",
        "Iterative Development": "Yes",
        "Time Management": "Fixed",
    },
    "Waterfall": {
        "Project Lifecycle Model": "Linear",
        "Flexibility": "Low",
        "Customer Involvement": "Low",
        "Iterative Development": "No",
        "Time Management": "Fixed",
    },
    "Extreme Programming (XP)": {
        "Project Lifecycle Model": "Iterative",
        "Flexibility": "High",
        "Customer Involvement": "High",
        "Iterative Development": "Yes",
        "Time Management": "Flexible",
    },
    "Dynamic Systems Development Method (DSDM)": {
        "Project Lifecycle Model": "Iterative",
        "Flexibility": "High",
        "Customer Involvement": "High",
        "Iterative Development": "Yes",
        "Time Management": "Flexible",
    },
    "Hybrid Approach": {
        "Project Lifecycle Model": "Adaptive",
        "Flexibility": "High",
        "Customer Involvement": "High",
        "Iterative Development": "Yes",
        "Time Management": "Flexible",
    },
}

# Initialize points for each approach
approach_points = defaultdict(int)

# Function to update points based on user choices
def update_points():
    for approach, characteristics in approaches.items():
        if characteristics["Project Lifecycle Model"] == lifecycle_var.get():
            approach_points[approach] += 1
        if characteristics["Flexibility"] == flexibility_var.get():
            approach_points[approach] += 1
        if characteristics["Customer Involvement"] == customer_var.get():
            approach_points[approach] += 1
        if (
            characteristics["Iterative Development"]
            == iterative_development_var.get()
        ):
            approach_points[approach] += 1
        if characteristics["Time Management"] == time_management_var.get():
            approach_points[approach] += 1

# Function to display results
def show_results():
    update_points()
    # Identify the highest score
    highest_score = max(approach_points.values())
    # Find all approaches with the highest score
    recommended_approaches = [approach for approach, points in approach_points.items() if points == highest_score]

    # Plotting
    plt.figure(figsize=(10, 8))
    approaches_list = list(approach_points.keys())
    points_list = [approach_points[app] for app in approaches_list]
    plt.barh(approaches_list, points_list, color='#2ec4b6')
    plt.xlabel('Points')
    plt.ylabel('Approaches')
    plt.title('Suitability of Project Management Approaches')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest points on top

    # Calculate the maximum width of the bars to position the text above the highest bar
    max_width = max(points_list)
    padding = max_width * 0.05  # Add a little padding above the bars

    # Prepare recommendation text
    if len(recommended_approaches) > 1:
        recommendation_text = "The equally most suitable approaches for your project are: " + ", ".join(
            recommended_approaches)
    else:
        recommendation_text = "The most suitable approach for your project is: " + recommended_approaches[0]

    # Display the recommendation text in the plot
    plt.text(max_width / 2, len(approaches_list) - 0.03, recommendation_text, ha='center', va='top', fontsize=12,
             color='#193C57', bbox=dict(facecolor='white', alpha=0.5))

    plt.tight_layout()
    plt.show()


def next_question(frame, next_frame):
    frame.pack_forget()
    next_frame.pack(fill='both', expand=True)

def previous_question(frame, prev_frame):
    frame.pack_forget()
    prev_frame.pack(fill='both', expand=True)

def submit_and_show_results():
    update_points()
    show_results()

def begin_quiz():
    instructions_frame.pack_forget()
    question_frames[0].pack(fill='both', expand=True)

# Create main window
root = tk.Tk()
root.title("Project Management Approach Selection Quiz")
root.geometry("700x500")

# Apply a theme to the window for better visuals
style = ttk.Style(root)
style.theme_use('clam')
# This sets the background of the progress bar (trough) to a dark color
style.configure("Horizontal.TProgressbar", troughcolor='#ffffff', background='#2ec4b6')

# Logo and Title
logo_image = tk.PhotoImage(file="/Users/steicysingh/PycharmProjects/ENCE607/Images/Logo.png")  # Replace "your_logo_file.png" with the path to your logo image file
resized_logo_image = logo_image.subsample(16, 16)
# Introduction
intro_frame = tk.Frame(root)
intro_frame.pack(side="left", padx=10)

# Logo label
logo_label = tk.Label(intro_frame, image=resized_logo_image)
logo_label.grid(row=0, column=0, padx=(0, 10))  # Add padding to the right

# Text label
intro_label = tk.Label(
    intro_frame, text="Project Management Approach Quiz", font=("Helvetica", 21), pady=20
)
intro_label.grid(row=0, column=1)

# Instructions Frame
instructions_frame = tk.Frame(root, bg='#cbf3f0')  # Baby Pink Background
instructions_frame.pack(fill='both', expand=True)

# Text label for instructions
instructions_text = """
Welcome to the Quiz!

This quiz will help you discover which project management approaches you might want to implement in your next project, company, or initiative.

Please read the instructions carefully before proceeding:

- You will have multiple questions with multiple choices, and you can only choose one option (the most suitable).
- After answering each question, click the "Next" button to move to the next one.
- You can also go back to the previous question by clicking on the "Previous Question" button.
- A progress bar on the screen will indicate how much of the quiz is completed and how much is pending.
- On the screen with the final question, you will find a submit button. Clicking it will show you the recommendation charts.

Click "Begin" to start now!
"""

instructions_label = tk.Label(instructions_frame, text=instructions_text, font=("Helvetica", 14), pady=80, padx=20, bg='#cbf3f0', fg='#323232', justify = 'left')
instructions_label.pack()


# Begin button
begin_button = tk.Button(instructions_frame, text="Begin", command=begin_quiz, bg='#cbf3f0', fg='#323232')  # Pink Button
begin_button.pack()

# Question frames
question_frames = []
for i in range(5):
    frame = tk.Frame(root, bg='#ffffff', bd=1, relief='sunken')
    question_frames.append(frame)

# Variables for each question
lifecycle_var = tk.StringVar()
flexibility_var = tk.StringVar()
customer_var = tk.StringVar()
iterative_development_var = tk.StringVar()
time_management_var = tk.StringVar()

# Create question cards
def create_question_card(question, options, var, frame, next_frame=None, prev_frame=None):
    frame.config(bg='#cbf3f0')  # Set the background color of the frame to blue
    question_label = tk.Label(frame, text=question, font=("Helvetica", 22), bg='#cbf3f0', fg='#323232', wraplength=500)
    question_label.pack(pady=(60, 40))
    for option in options:
        # Adjusted the background color to blue and text color to white for readability
        option_frame = tk.Frame(frame, bg='#cbf3f0')  # Create a frame for each option to add padding
        option_frame.pack(anchor="w")
        tk.Radiobutton(option_frame, text=option[1], variable=var, value=option[0], font=("Helvetica", 14), bg='#cbf3f0', fg='#323232', selectcolor='#0056b3').pack(side='left', padx=(25, 0))

    progress = ttk.Progressbar(frame, orient='horizontal', length=200, mode='determinate')
    progress.pack(pady=110)
    progress['value'] = (question_frames.index(frame) + 1) * 20  # Increment progress bar value

    if prev_frame:
        prev_button = tk.Button(frame, text="Previous", command=lambda: previous_question(frame, prev_frame), bg='white', fg='#323232')
        prev_button.pack(side='left', pady=80, padx=(20, 0))

    if next_frame:
        next_button = tk.Button(frame, text="Next", command=lambda: next_question(frame, next_frame), bg='white', fg='#323232')
        next_button.pack(side='right', pady=80, padx=(0, 20))
    else:
        next_button = tk.Button(frame, text="Submit", command=submit_and_show_results, bg='white', fg='black')
        next_button.pack(side='right', pady=80, padx=(0, 20))


# Create question cards
create_question_card(
    "Q1. Which project lifecycle model best aligns with your organization's approach?",
    [
        ("Linear", "Linear: Divides the project into distinct phases with sequential dependencies."),
        ("Iterative", "Iterative: Allows for repetitive cycles of development and refinement."),
        ("Continuous", "Continuous: Views the project as an ongoing process without distinct start and end points."),
        ("Adaptive", "Adaptive: Accepts changes in project, change-driven model ")
    ],
    lifecycle_var,
    question_frames[0],
    next_frame=question_frames[1]
)

create_question_card(
    "Q2. On a scale of low, medium and high, how would you rate the level of flexibility is required in your project?",
    [
        ("Low", "Low: Limited ability to adapt or change project scope, schedule, or resources."),
        ("Medium", "Medium: Moderate level of adaptability to accommodate changes within predefined constraints."),
        ("High", "High: Significant capacity to adjust project elements based on evolving requirements or feedback.")
    ],
    flexibility_var,
    question_frames[1],
    next_frame=question_frames[2],
    prev_frame=question_frames[0]
)

create_question_card(
    "Q3. What level of client/customer involvement is expected in the project?",
    [
        ("Low", "Low: Limited participation of the customer or end-user in project planning or decision-making."),
        ("Moderate", "Moderate: Some involvement of stakeholders or customers in providing feedback or requirements."),
        ("High", "High: Extensive collaboration with customers throughout the project lifecycle to ensure alignment with their needs.")
    ],
    customer_var,
    question_frames[2],
    next_frame=question_frames[3],
    prev_frame=question_frames[1]
)

create_question_card(
    "Q4. How is your project being developed? Iteratively or linearly?",
    [
        ("Yes", "Iteratively: Involves iterative cycles of planning, executing, and reviewing project deliverables."),
        ("No", "Linearly: Adheres to a linear progression without revisiting or revising completed stages.")
    ],
    iterative_development_var,
    question_frames[3],
    next_frame=question_frames[4],
    prev_frame=question_frames[2]
)

create_question_card(
    "Q5. Is your project constrained by fixed timelines and milestones?",
    [
        ("Fixed", "Fixed: Project schedule is rigid with predefined milestones and deadlines."),
        ("Flexible", "Flexible: Allows for adjustments to project timelines based on changing priorities or constraints.")
    ],
    time_management_var,
    question_frames[4],
    prev_frame=question_frames[3]
)

root.mainloop()
