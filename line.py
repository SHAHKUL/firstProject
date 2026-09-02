import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
canvas.create_rectangle(50, 100, 200, 200, outline="black", fill="yellow", width=2)
canvas.create_oval(50, 250, 200, 350, outline="green", fill="lightgreen", width=2)

root.mainloop()
