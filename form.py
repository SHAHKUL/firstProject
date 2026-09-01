import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x650")
root.configure(bg="#f2f4f7")
root.resizable(False, False)


# ---------------- COLORS ----------------
BG_COLOR = "#f2f4f7"
CARD_COLOR = "white"
PRIMARY = "#4f46e5"
TEXT_COLOR = "#1f2937"
SECONDARY_TEXT = "#6b7280"


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="Student Registration",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Enter your details below",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg=SECONDARY_TEXT
)
subtitle.pack(pady=(0, 20))


# ---------------- MAIN CARD ----------------
card = tk.Frame(
    root,
    bg=CARD_COLOR,
    padx=30,
    pady=25
)
card.pack(padx=30, fill="both")


# ---------------- NAME ----------------
tk.Label(
    card,
    text="Full Name",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w")

name_entry = tk.Entry(
    card,
    font=("Arial", 12),
    width=35,
    bd=1,
    relief="solid"
)
name_entry.pack(fill="x", pady=(5, 15), ipady=7)


# ---------------- AGE ----------------
tk.Label(
    card,
    text="Age",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w")

age_entry = tk.Entry(
    card,
    font=("Arial", 12),
    bd=1,
    relief="solid"
)
age_entry.pack(fill="x", pady=(5, 15), ipady=7)


# ---------------- GENDER ----------------
tk.Label(
    card,
    text="Gender",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w")

gender = tk.StringVar(value="Male")

gender_frame = tk.Frame(card, bg=CARD_COLOR)
gender_frame.pack(anchor="w", pady=(5, 15))

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender,
    value="Male",
    bg=CARD_COLOR,
    font=("Arial", 11),
    activebackground=CARD_COLOR
).pack(side="left", padx=(0, 20))

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender,
    value="Female",
    bg=CARD_COLOR,
    font=("Arial", 11),
    activebackground=CARD_COLOR
).pack(side="left")


# ---------------- SKILLS ----------------
tk.Label(
    card,
    text="Skills",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w")

python_var = tk.IntVar()
java_var = tk.IntVar()
js_var = tk.IntVar()

skills_frame = tk.Frame(card, bg=CARD_COLOR)
skills_frame.pack(anchor="w", pady=(5, 15))

tk.Checkbutton(
    skills_frame,
    text="Python",
    variable=python_var,
    bg=CARD_COLOR,
    font=("Arial", 11),
    activebackground=CARD_COLOR
).pack(side="left", padx=(0, 15))

tk.Checkbutton(
    skills_frame,
    text="Java",
    variable=java_var,
    bg=CARD_COLOR,
    font=("Arial", 11),
    activebackground=CARD_COLOR
).pack(side="left", padx=(0, 15))

tk.Checkbutton(
    skills_frame,
    text="JavaScript",
    variable=js_var,
    bg=CARD_COLOR,
    font=("Arial", 11),
    activebackground=CARD_COLOR
).pack(side="left")


# ---------------- CITY DROPDOWN ----------------
tk.Label(
    card,
    text="City",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
).pack(anchor="w")

city = tk.StringVar(value="Select City")

city_dropdown = tk.OptionMenu(
    card,
    city,
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Bangalore",
    "Hyderabad"
)

city_dropdown.config(
    font=("Arial", 11),
    bg="white",
    width=25,
    bd=1,
    relief="solid"
)

city_dropdown.pack(anchor="w", pady=(5, 20))


# ---------------- SUBMIT FUNCTION ----------------
def submit():

    name = name_entry.get()
    age = age_entry.get()
    selected_gender = gender.get()
    selected_city = city.get()

    skills = []

    if python_var.get():
        skills.append("Python")

    if java_var.get():
        skills.append("Java")

    if js_var.get():
        skills.append("JavaScript")

    # Validation
    if name == "":
        messagebox.showwarning("Warning", "Please enter your name")
        return

    if age == "":
        messagebox.showwarning("Warning", "Please enter your age")
        return

    if selected_city == "Select City":
        messagebox.showwarning("Warning", "Please select your city")
        return

    if len(skills) == 0:
        skills_text = "No skills selected"
    else:
        skills_text = ", ".join(skills)

    result = f"""
Name   : {name}
Age    : {age}
Gender : {selected_gender}
Skills : {skills_text}
City   : {selected_city}
"""

    messagebox.showinfo("Registration Successful", result)


# ---------------- BUTTON ----------------
submit_button = tk.Button(
    card,
    text="Register Student",
    command=submit,
    font=("Arial", 12, "bold"),
    bg=PRIMARY,
    fg="white",
    activebackground="#3730a3",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    padx=20,
    pady=10
)

submit_button.pack(fill="x", pady=(5, 5))


# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="Student Registration System",
    font=("Arial", 9),
    bg=BG_COLOR,
    fg=SECONDARY_TEXT
)

footer.pack(pady=15)


# ---------------- RUN ----------------
root.mainloop()
