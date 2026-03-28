import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Checkbutton and Radiobutton")
root.geometry("300x300")

tk.Label(root, text="-(Radiobutton)-", font=("Arial", 12)).pack(pady=5)

radio_var = tk.StringVar(value="Not selected")

tk.Radiobutton(root, text="Select-A", variable=radio_var, value="Select-A").pack(padx=20)
tk.Radiobutton(root, text="Select-B", variable=radio_var, value="Select-B").pack(padx=20)
tk.Radiobutton(root, text="Select-C", variable=radio_var, value="Select-c").pack(padx=20)

tk.Label(root, text="-(Checkbotton)-", font=("Arial", 12)).pack(pady=(15, 5))

opt1 = tk.IntVar()
opt2 = tk.IntVar()
opt3 = tk.IntVar()

tk.Checkbutton(root, text="option1", variable=opt1).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="option2", variable=opt2).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="option3", variable=opt3).pack(anchor="w", padx=20)

def show_selection():
    radio_choice = radio_var.get()
    x = []
    if opt1.get():
        x.append("option-1")
    if opt2.get():
        x.append("option-2")
    if opt3.get():
        x.append("option-3")

    msg = "selected in Radiobutton: " + radio_choice + "\nselected in Checkbutton: " + (", ".join(x) if x else "None")
    messagebox.showinfo("Your Order", msg)

tk.Button(root, text="Submit", command=show_selection).pack(pady=20)

root.mainloop()