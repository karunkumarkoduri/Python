import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu

root = tk.Tk()
root.title("GUI Widgets Demo")
root.geometry("400x300")

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=lambda: filedialog.askopenfilename())
file_menu.add_command(label="Exit", command=root.quit)

Tab_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="help", menu=Tab_menu)
Tab_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Nothing! Do it by your own"))

mb = tk.Menubutton(root, text="Tools:", direction="below")
mb_menu = tk.Menu(mb, tearoff=0)
mb.config(menu=mb_menu)
mb_menu.add_command(label="Clear List", command=lambda: listbox.delete(0, tk.END))
mb_menu.add_command(label="Show Info", command=lambda: messagebox.showinfo("Info", "List has items: " + str(listbox.size())))
mb.pack(pady=5, anchor="w")

frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

listbox = tk.Listbox(frame, height=8)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

for i in range(1, 21):
    listbox.insert(tk.END, "Item " + str(i))

def show_selected():
    sel = listbox.curselection()
    if sel:
        item = listbox.get(sel[0])
        messagebox.showinfo("Selected Item", "You selected: " + item)
    else:
        messagebox.showwarning("No selection", "Please select an item.")

tk.Button(root, text="Show Selected", command=show_selected).pack(pady=(5, 10))

root.mainloop()