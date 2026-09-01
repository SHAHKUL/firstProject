import tkinter as tk

root = tk.Tk()
root.title("Pack Example")
root.geometry("400x300")

tk.Label(root, text="Student Registration").pack(anchor='e', pady=10)

tk.Label(root, text="Name").pack()
tk.Entry(root).pack(pady=5)

tk.Label(root, text="Age").pack()
tk.Entry(root).pack(pady=5)

tk.Button(root, text="Submit").pack(pady=10)
root.mainloop()



import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("400x300")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="City").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Submit").grid(
    row=3,
    column=1,
    padx=10,
    pady=10
)

root.mainloop()





import tkinter as tk

root = tk.Tk()
root.geometry("500x300")

label = tk.Label(root, text="Name")
label.place(x=50, y=50)

entry = tk.Entry(root)
entry.place(x=120, y=50)

button = tk.Button(root, text="Submit")
button.place(x=120, y=100)

root.mainloop()










