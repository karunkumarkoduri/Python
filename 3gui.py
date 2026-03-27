import tkinter as kk

root=kk.Tk()
root.title(" GUI using a Tkinter geometry methods pack(), grid(), place()")
root.geometry("800x430")

p_top=kk.Label(root,text="This is using pack top ",font=("arial",14,"bold"),bg="red",fg="black",relief="groove")
p_top.pack(side="top",fill="x")

p_bottom=kk.Label(root,text="this is pack bottom padx=10,pady=10",font=("arial",14,"bold"),bg="green",fg="black",relief="ridge")
p_bottom.pack(side="bottom",fill="x",padx=10,pady=10)

p_right=kk.Label(root,text="This is using pack left \n ,padx=20,pady=10",font=("arial",14,"bold"),bg="red",fg="black",relief="groove")
p_right.pack(side="left",fill="y",padx=20,pady=10)

p_left=kk.Label(root,text="This is using pack right \n padx=10,pady=20",font=("arial",14,"bold"),bg="red",fg="black",relief="groove")
p_left.pack(side="right",fill="y",padx=10,pady=20)

g_right=kk.Label(p_right,text="This is using grid row1 and column1",font=("Arial",12,"bold"),bg="black",fg="white")
g_right.grid(row=1,column=1)

g_left=kk.Label(p_left,text="This is using grid row1,column1 padx=10,pady=10",font=("Arial",12,"bold"),bg="black",fg="white")
g_left.grid(row=1,column=1,sticky="e",padx=10,pady=10)

pl_right=kk.Label(p_right,text="this is using place x=30,y=50",font=("arial",12,"bold"),bg="black",fg="white")
pl_right.place(x=30,y=50)

pl_left=kk.Label(p_left,text="this is using place \n x=80,y=200 width=250,height=80",font=("arial",12,"bold"),bg="black",fg="white")
pl_left.place(x=80, y=200, width=250, height=80)

root.mainloop()