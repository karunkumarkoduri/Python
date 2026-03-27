import tkinter as kk
root=kk.Tk()
root.title("GUI using Label, Entry and Button widgets")
root.geometry("400x200")
L1=kk.Label(root,text="Hi! I am Label1",font=("Arial",12),bg="Green",fg="Black",padx=10,pady=5)
L1.pack()
i1=kk.Entry(root,width=25,font=("Arial",11),bg="white",fg="Darkblue",bd=2,relief="solid")
i1.pack()
def button():
    l2=kk.Label(root,text="~You are stronger~")
    l2.pack()
cb=kk.Button(root,text=("Kick me!!!\n(only with cursor)"),font=("Arial",12,"bold"),bg="Green",fg="Black",padx=15,pady=5,command=button)
cb.pack()
root.mainloop()