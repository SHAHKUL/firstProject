import tkinter as tk


root = tk.Tk()
root.title("Width Change Example")
root.geometry("400x180")


def update_width():
    # Calculate pixel width directly: (value / 100) * total width
    percent = float(spinbox.get())
    pixel_width = int((percent / 100.0) * 300)
    # Update width in pixels directly
    bar.place_configure(width=pixel_width)



# 1. Spinbox (0 to 100)
spinbox = tk.Spinbox(
    root,
    from_=0,
    to=100,
    increment=1,
    command=update_width,
    font=("Arial", 12),
    width=6,
    justify="center"
)
spinbox.pack(pady=20)

# 2. Outer container
track = tk.Frame(root, bg="grey", width=300, height=25)
track.pack(pady=10)

# 3. Inner bar using fixed pixel height and starting with width=0
bar = tk.Frame(track, bg="green")
bar.place(x=0, y=0, width=0, height=25)

root.mainloop()
