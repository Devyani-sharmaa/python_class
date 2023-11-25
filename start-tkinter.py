# tkinter


# import tkinter as tk

# window = tk.Tk()

# window.geometry("500x700")
# window.title("Calculater")
# window.config(background = "green")

# lbl = tk.Label(window, text = "Hwllo world", font = ("robort", 2, "bold"), bg = "green", foreground="blue")

# lbl.pack(fill = "x", padx = 20, pady=30, ipady=10, side = "top")

# en = tk.Button(window, font("robort", 20, "italic"))
# en.pack()

# btn = tk.Button(window, text = "Click Me", font = ("robort", 25, "bold"), bg="red")
# btn.pack(pady=20)

# x = tk.Checkbutton(window)
# x.pack()

# x = tk.Radiobutton(window)
# x.pack()


# x=tk.BASELINE(window)
# # window.mainloop()



# # pack()
# # grid()
# # place()

# ye grid se krr rhe hai


import tkinter as tk

import mysql.connector

coon = mysql.connector.connect(host = "localhost", username = "root", password = "devyani@12", database = "excellence")

curser = coon.cursor()


def saveinfo():
    name = en1.get()
    age = en2.get()
    email = en4.get()
    number = en3.get()

    curser.execute(f"insert into xyz values('{name}', {age}, '{number}', '{email}')")
    coon.commit()

    en1.delete(0, tk.END)
    en2.delete(0, tk.END)
    en3.delete(0, tk.END)
    en4.delete(0, tk.END)

window = tk.Tk()

window.geometry("500x300")
window.title("Calculater")
window.config(background = "green")

lbl = tk.Label(window, text = "", background="green")
#lbl.grid(fill = "x", padx = 20, pady=30, ipady=10, side = "top")
lbl.grid(row=0,column=0, padx=10, pady=10)


lbl = tk.Label(window, text = "Name", font = ("robort",20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=1,column=1,padx=30, pady=2)    


lbl = tk.Label(window, text = "Age", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=2,column=1,padx=30, pady=2) 


lbl = tk.Label(window, text = "Number", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=3,column=1,padx=30, pady=2) 


lbl = tk.Label(window, text = "Email", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=4,column=1,padx=30, pady=2) 

lbl = tk.Label(window, text = ":", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=1,column=2,padx=2, pady=2) 


lbl = tk.Label(window, text = ":", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=2,column=2,padx=2, pady=2) 

lbl = tk.Label(window, text = ":", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=3,column=2,padx=2, pady=2) 


lbl = tk.Label(window, text = ":", font = ("robort", 20, "bold"), bg = "green", foreground="blue")
lbl.grid(row=4,column=2,padx=2, pady=2) 


en1=tk.Entry(window)
en1.grid(row=1,column=3,padx=5,pady=5)

en2 = tk.Entry(window)
en2.grid(row=2,column=3,padx=5,pady=5)


en3 = tk.Entry(window)
en3.grid(row=3,column=3,padx=5,pady=5)

en4 = tk.Entry(window)
en4.grid(row=4,column=3,padx=5,pady=5)

btn = tk.Button(window, text = "Submit", font = ("robort", 15, "bold"), bg="red", command=saveinfo)

btn.grid(row=5,column=3,padx=20,pady=2)

window.mainloop()