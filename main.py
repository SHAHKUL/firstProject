
import tkinter as tk

root = tk.Tk()
root.title("Student Register")
root.geometry("600x600")
root.configure(bg="#f2f2f2")


# Heading
title_label = tk.Label(
    root,
    text="Student Registration",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="#333333"
)
title_label.pack(pady=30)


# Name Label
name_label = tk.Label(
    root,
    text="Enter Your Name",
    font=("Arial", 14),
    bg="#f2f2f2",
    fg="#333333"
)
name_label.pack(anchor="w", padx=80, pady=(10, 5))


# Name Entry
name_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=35
)
name_entry.pack(
    padx=80,
    pady=(0, 20),
    ipady=8
)


# Submit Function
def submited():
    name = name_entry.get()

    result_label.config(
        text="Student Name is: " + name
    )


# Submit Button
submit_button = tk.Button(
    root,
    text="Register Student",
    command=submited,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10
)
submit_button.pack(pady=10)
# Result Label
result_label = tk.Label(
    root,
    text="Student Name is",
    bg="#f2f2f2",
    fg="#333333",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=30)

root.mainloop()
