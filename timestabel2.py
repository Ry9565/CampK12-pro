import tkinter as tk

def MultiTable():
  print("\n:Multiplication Table:\n")
  print("\nTimes-Table of Number")

  for x in range(1, 11):
    number = int(EnterTable.get())
    print('\t\t', (number), 'x', (x), '=', (x*number),)

Table = tk.Tk()
Table.geometry("800x800")
Table.resizable(0,0)
Table.title("Mutiplication tabels")

EnterTable = tk.StringVar()
label1=tk.Label(Table,text="Enter Your Times_Table Number:",font=30,fg="black").grid(row=1,column= 6)
label1=tk.Label(Table,text="").grid(row=2,column=6)

entry=tk.Entry(Table,textvariable=EnterTable,justify='center').grid(row=3,column=6)

button1=tk.Button(Table,text="Generate Table",fg="blue",command=MultiTable).grid(row=5,column=6)

label1=tk.Label(Table,text="").grid(row=6,column=6)
exit=tk.Button(Table,text="Quit",fg='red',command=Table.destroy).grid(row=7,column=6)
Table.mainloop()