import tkinter as tk

# Function to handle scale value changes
def on_scale_change(value):
    label_value.config(text=f"Value: {value}")

# Create the main application window
root = tk.Tk()
root.title("Scale Widget Example")
root.geometry("400x200")

# Create a frame for the scale widget
frame = tk.Frame(root)

# Create a scale widget
scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_change)
scale.pack()

# Label to display scale value
label_value = tk.Label(root, text="Value: 0")
label_value.pack(pady=10)

# Pack the frame containing the scale widget
frame.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()
