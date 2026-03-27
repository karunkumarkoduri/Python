import tkinter as tk

root = tk.Tk()
root.title("Menu & Menubutton Demo")
root.geometry("350x200")

def update_status(msg):
    status_label.config(text=msg)

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: update_status("New file"))
file_menu.add_command(label="Exit", command=root.quit)

options_btn = tk.Menubutton(root, text="-who are you- \n (select one)",bg="black",fg="white",relief="groove")
options_btn.pack(pady=50)

options_menu = tk.Menu(options_btn, tearoff=0)
options_btn["menu"] = options_menu
options_menu.add_command(label="A", command=lambda: update_status("superman"))
options_menu.add_command(label="B", command=lambda: update_status("Hulk"))
options_menu.add_command(label="C", command=lambda: update_status("Thor"))

status_label = tk.Label(root, text="Ready", relief="sunken", anchor="w")
status_label.pack(side="bottom", fill="x")

root.mainloop()