import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import csv

_bgcolor = 'gray82'
_fgcolor = 'black'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'

root = tk.Tk()
root.geometry("587x681+468+170")
root.minsize(120, 1)
root.maxsize(1540, 941)
root.resizable(1, 1)
root.title("RY")
root.configure(background=_bgcolor)

img1 = tk.PhotoImage(file="4.png")
img2 = tk.PhotoImage(file="OIP.png")
img3 = tk.PhotoImage(file="R(1).png")
img4 = tk.PhotoImage(file="R2.png")
img5 = tk.PhotoImage(file="lina.png")
img6 = tk.PhotoImage(file="bre(1).png")
img7 = tk.PhotoImage(file="plu.png")

Frame1 = tk.Frame(root)
Frame1.place(relx=0.0, rely=0.441, relheight=0.565, relwidth=1.014)
Frame1.configure(relief='groove', background="#b4cdba", borderwidth="2")

Entry1 = tk.Entry(Frame1)
Entry1.place(relx=0.05, rely=0.33, height=20, relwidth=0.141)
Entry1.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry2 = tk.Entry(Frame1)
Entry2.place(relx=0.05, rely=0.234, height=20, relwidth=0.141)
Entry2.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')

Entry12 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry12.place(relx=0.29, rely=0.33, height=20, relwidth=0.141)
Entry22 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry22.place(relx=0.29, rely=0.234, height=20, relwidth=0.141)


Entry13 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry13.place(relx=0.53, rely=0.33, height=20, relwidth=0.141)
Entry23 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry23.place(relx=0.53, rely=0.234, height=20, relwidth=0.141)

Entry14 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry14.place(relx=0.77, rely=0.33, height=20, relwidth=0.141)
Entry24 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry24.place(relx=0.77, rely=0.234, height=20, relwidth=0.141)

Entry15 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry15.place(relx=0.05, rely=0.896, height=20, relwidth=0.141)
Entry25 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry25.place(relx=0.05, rely=0.80, height=20, relwidth=0.141)

Entry16 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry16.place(relx=0.29, rely=0.896, height=20, relwidth=0.141)
Entry26 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry26.place(relx=0.29, rely=0.80, height=20, relwidth=0.141)

Entry17 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry17.place(relx=0.53, rely=0.896, height=20, relwidth=0.141)
Entry27 = tk.Entry(Frame1,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,foreground='green', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d",cursor='hand2')
Entry27.place(relx=0.53, rely=0.80, height=20, relwidth=0.141)

# دالة لحفظ الرقم في Entry1 عند إغلاق البرنامج
def save_entry1():
    with open('entry1.txt', 'w') as file:
        file.write(Entry1.get())
# دالة لتحميل الرقم من الملف عند بدء البرنامج
def load_entry1():
    if os.path.exists('entry1.txt'):
        with open('entry1.txt', 'r') as file:
            Entry1.insert(0, file.read())
# دالة لحفظ الرقم في Entry2 عند إغلاق البرنامج
def save_entry2():
    with open('entry2.txt', 'w') as file:
        file.write(Entry2.get())
# دالة لتحميل الرقم من الملف عند بدء البرنامج
def load_entry2():
    if os.path.exists('entry2.txt'):
        with open('entry2.txt', 'r') as file:
            Entry2.insert(0, file.read())
# تحميل الأرقام عند بدء البرنامج
load_entry1()
load_entry2()

def save_entry12():
    with open('entry12.txt', 'w') as file:
        file.write(Entry12.get())
def load_entry12():
    if os.path.exists('entry12.txt'):
        with open('entry12.txt', 'r') as file:
            Entry12.insert(0, file.read())
def save_entry22():
    with open('entry22.txt', 'w') as file:
        file.write(Entry22.get())
def load_entry22():
    if os.path.exists('entry22.txt'):
        with open('entry22.txt', 'r') as file:
            Entry22.insert(0, file.read())
load_entry12()
load_entry22()

def save_entry13():
    with open('entry13.txt', 'w') as file:
        file.write(Entry13.get())
def load_entry13():
    if os.path.exists('entry13.txt'):
        with open('entry13.txt', 'r') as file:
            Entry13.insert(0, file.read())
def save_entry23():
    with open('entry23.txt', 'w') as file:
        file.write(Entry23.get())
def load_entry23():
    if os.path.exists('entry2.txt'):
        with open('entry23.txt', 'r') as file:
            Entry23.insert(0, file.read())
load_entry13()
load_entry23()

def save_entry14():
    with open('entry14.txt', 'w') as file:
        file.write(Entry14.get())
def load_entry14():
    if os.path.exists('entry14.txt'):
        with open('entry14.txt', 'r') as file:
            Entry14.insert(0, file.read())
def save_entry24():
    with open('entry24.txt', 'w') as file:
        file.write(Entry24.get())
def load_entry24():
    if os.path.exists('entry24.txt'):
        with open('entry24.txt', 'r') as file:
            Entry24.insert(0, file.read())
load_entry14()
load_entry24()

def save_entry15():
    with open('entry15.txt', 'w') as file:
        file.write(Entry15.get())
def load_entry15():
    if os.path.exists('entry15.txt'):
        with open('entry15.txt', 'r') as file:
            Entry15.insert(0, file.read())
def save_entry25():
    with open('entry25.txt', 'w') as file:
        file.write(Entry25.get())
def load_entry25():
    if os.path.exists('entry25.txt'):
        with open('entry25.txt', 'r') as file:
            Entry25.insert(0, file.read())
load_entry15()
load_entry25()

def save_entry16():
    with open('entry16.txt', 'w') as file:
        file.write(Entry16.get())
def load_entry16():
    if os.path.exists('entry16.txt'):
        with open('entry16.txt', 'r') as file:
            Entry16.insert(0, file.read())
def save_entry26():
    with open('entry26.txt', 'w') as file:
        file.write(Entry26.get())
def load_entry26():
    if os.path.exists('entry26.txt'):
        with open('entry26.txt', 'r') as file:
            Entry26.insert(0, file.read())
load_entry16()
load_entry26()

def save_entry17():
    with open('entry17.txt', 'w') as file:
        file.write(Entry17.get())
def load_entry17():
    if os.path.exists('entry17.txt'):
        with open('entry17.txt', 'r') as file:
            Entry17.insert(0, file.read())
def save_entry27():
    with open('entry27.txt', 'w') as file:
        file.write(Entry27.get())
def load_entry27():
    if os.path.exists('entry27.txt'):
        with open('entry27.txt', 'r') as file:
            Entry27.insert(0, file.read())
load_entry17()
load_entry27()



def save_to_csv(treeview):
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview.get_children():
            row = treeview.item(row_id)['text'], *treeview.item(row_id)['values']
            writer.writerow(row)
def load_from_csv(treeview):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data.csv' not found.")

def save_to_csv2(treeview2):
    with open('data2.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview2.get_children():
            row = treeview2.item(row_id)['text'], *treeview2.item(row_id)['values']
            writer.writerow(row)
def load_from_csv2(treeview2):
    if os.path.exists('data2.csv'):
        with open('data2.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview2.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data2.csv' not found.")

def save_to_csv3(treeview3):
    with open('data3.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview3.get_children():
            row = treeview3.item(row_id)['text'], *treeview3.item(row_id)['values']
            writer.writerow(row)
def load_from_csv3(treeview3):
    if os.path.exists('data3.csv'):
        with open('data3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview3.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data3.csv' not found.")

def save_to_csv4(treeview4):
    with open('data4.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview4.get_children():
            row = treeview4.item(row_id)['text'], *treeview4.item(row_id)['values']
            writer.writerow(row)
def load_from_csv4(treeview4):
    if os.path.exists('data4.csv'):
        with open('data4.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview4.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data4.csv' not found.")

def save_to_csv5(treeview5):
    with open('data5.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview5.get_children():
            row = treeview5.item(row_id)['text'], *treeview5.item(row_id)['values']
            writer.writerow(row)
def load_from_csv5(treeview5):
    if os.path.exists('data5.csv'):
        with open('data5.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview5.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data5.csv' not found.")

def save_to_csv6(treeview6):
    with open('data6.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview6.get_children():
            row = treeview6.item(row_id)['text'], *treeview6.item(row_id)['values']
            writer.writerow(row)
def load_from_csv6(treeview6):
    if os.path.exists('data6.csv'):
        with open('data6.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview6.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data6.csv' not found.")

def save_to_csv7(treeview7):
    with open('data7.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row_id in treeview7.get_children():
            row = treeview7.item(row_id)['text'], *treeview7.item(row_id)['values']
            writer.writerow(row)
def load_from_csv7(treeview7):
    if os.path.exists('data7.csv'):
        with open('data7.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview7.insert("", "end", text=row[0], values=row[1:])
    else:
        print("File 'data7.csv' not found.")

def add_to_treeview(entry1, entry2, treeview):
    mawad = entry1.get()
    prix = entry2.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview.insert("", "end", text=mawad, values=(prix,))
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            calculate_totals(treeview)
            save_to_csv(treeview)

    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview2(entry12, entry22,treeview2):
    mawad = entry12.get()
    prix = entry22.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview2.insert("", "end", text=mawad, values=(prix,))
            entry12.delete(0, tk.END)
            entry22.delete(0, tk.END)
            calculate_totals2(treeview2)
            save_to_csv2(treeview2)
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview3(entry13, entry23,treeview3):
    mawad = entry13.get()
    prix = entry23.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview3.insert("", "end", text=mawad, values=(prix,))
            entry13.delete(0, tk.END)
            entry23.delete(0, tk.END)
            calculate_totals3(treeview3)
            (save_to_csv3(treeview3))
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview4(entry14, entry24,treeview4):
    mawad = entry14.get()
    prix = entry24.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview4.insert("", "end", text=mawad, values=(prix,))
            entry14.delete(0, tk.END)
            entry24.delete(0, tk.END)
            calculate_totals4(treeview4)
            (save_to_csv4(treeview4))
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview5(entry15, entry25,treeview5):
    mawad = entry15.get()
    prix = entry25.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview5.insert("", "end", text=mawad, values=(prix,))
            entry15.delete(0, tk.END)
            entry25.delete(0, tk.END)
            calculate_totals5(treeview5)
            (save_to_csv5(treeview5))
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview6(entry16, entry26,treeview6):
    mawad = entry16.get()
    prix = entry26.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview6.insert("", "end", text=mawad, values=(prix,))
            entry16.delete(0, tk.END)
            entry26.delete(0, tk.END)
            calculate_totals6(treeview6)
            (save_to_csv6(treeview6))
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")
def add_to_treeview7(entry17, entry27,treeview7):
    mawad = entry17.get()
    prix = entry27.get()
    try:
        prix = float(prix)
        if mawad and prix:
            treeview7.insert("", "end", text=mawad, values=(prix,))
            entry17.delete(0, tk.END)
            entry27.delete(0, tk.END)
            calculate_totals7(treeview7)
            (save_to_csv7(treeview7))
    except ValueError:
        messagebox.showerror("ERROR >-0 ", "Please enter a valid number for 'prix'.")

def frame_control():
    new_frame = tk.Frame(root)
    new_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.5)
    new_frame.configure(relief='groove', borderwidth="2", background="#6D9B94")
    ARG_T = tk.Label(new_frame, text='''ARG TOT''', anchor='w', background="#6D9B94",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_T.place(relx=0.067, rely=0.01, height=43, width=70)
    ARG_L = tk.Label(new_frame, text='''ARG L''', anchor='w', background="#6D9B94",
                    font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_L.place(relx=0.067, rely=0.2, height=43, width=70)
    ARG_BIM = tk.Label(new_frame, text='''ARG BIM''', anchor='w', background="#6D9B94",
                    font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_BIM.place(relx=0.067, rely=0.3, height=43, width=70)
    ARG_V = tk.Label(new_frame, text='''ARG V''', anchor='w', background="#6D9B94",
                     font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_V.place(relx=0.067, rely=0.4, height=43, width=70)
    ARG_LINA = tk.Label(new_frame, text='''ARG LINA''', anchor='w', background="#6D9B94",
                     font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_LINA.place(relx=0.067, rely=0.5, height=43, width=70)
    ARG_MOD = tk.Label(new_frame, text='''ARG MOD''', anchor='w', background="#6D9B94",
                        font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_MOD.place(relx=0.067, rely=0.6, height=43, width=70)
    ARG_PLUS = tk.Label(new_frame, text='''ARG PLUS''', anchor='w', background="#6D9B94",
                       font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    ARG_PLUS.place(relx=0.067, rely=0.7, height=43, width=70)
    ARG_TT = tk.Entry(new_frame, background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_TT.place(relx=0.4, rely=0.035, height=20, width=70)
    ARG_LL = tk.Entry(new_frame, background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_LL.place(relx=0.4, rely=0.225, height=20, width=70)
    ARG_BIMM = tk.Entry(new_frame,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_BIMM.place(relx=0.4, rely=0.325, height=20, width=70)
    ARG_VV = tk.Entry(new_frame, background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_VV.place(relx=0.4, rely=0.425, height=20, width=70)
    ARG_LINAA = tk.Entry(new_frame,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_LINAA.place(relx=0.4, rely=0.525,height=20, width=70)
    ARG_MODD = tk.Entry(new_frame,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_MODD.place(relx=0.4, rely=0.625,height=20, width=70)
    ARG_PLUSS = tk.Entry(new_frame,background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
    ARG_PLUSS.place(relx=0.4, rely=0.725, height=20, width=70)
    hide_button = tk.Button(new_frame, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2',
                            command=new_frame.destroy)
    hide_button.place(relx=0.7, rely=0.01, height=30, width=80)

def calculate_totals(treeview):
    total = 0
    for child in treeview.get_children():
        total += float(treeview.item(child, 'values')[0])

    Entry1.delete(0, tk.END)
    Entry1.insert(0, str(total))

    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    #new_value = current_value - entry4_value
    new_value_en2 = 600 - total

    # تحديث Entry4
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0
    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value + entry3_value + entry4_value + entry5_value + entry6_value + entry7_value))
    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2600-entry4_value ))  # تعيين قيمة ARG_TT هنا
    Entry2.delete(0, tk.END)
    Entry2.insert(0, str(new_value_en2))
    khobztotal(treeview)
    khodar(treeview)
    fawakih(treeview)
def calculate_totals2(treeview2):
    total2 = 0
    for child in treeview2.get_children():
        total2 += float(treeview2.item(child, 'values')[0])
    Entry12.delete(0, tk.END)
    Entry12.insert(0, str(total2))

    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    # new_value = current_value - entry4_value
    new_value_en2 = 500 - total2
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value)))
    Entry22.delete(0, tk.END)
    Entry22.insert(0, str(new_value_en2))
def calculate_totals3(treeview3):
    total3 = 0
    for child in treeview3.get_children():
        total3 += float(treeview3.item(child, 'values')[0])
    Entry13.delete(0, tk.END)
    Entry13.insert(0, str(total3))


    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    #new_value = current_value - entry4_value
    new_value_en3 = 500 - total3
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value)))
    Entry23.delete(0, tk.END)
    Entry23.insert(0, str(new_value_en3))
def calculate_totals4(treeview4):
    total4 = 0
    for child in treeview4.get_children():
        total4 += float(treeview4.item(child, 'values')[0])
    Entry14.delete(0, tk.END)
    Entry14.insert(0, str(total4))

    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    #new_value = current_value - entry4_value
    new_value_en4 = 300 - total4
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value)))
    Entry24.delete(0, tk.END)
    Entry24.insert(0, str(new_value_en4))
def calculate_totals5(treeview5):
    total5 = 0
    for child in treeview5.get_children():
        total5 += float(treeview5.item(child, 'values')[0])
    Entry15.delete(0, tk.END)
    Entry15.insert(0, str(total5))


    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    #new_value = current_value - entry4_value
    new_value_en5 = 200 - total5
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value)))
    Entry25.delete(0, tk.END)
    Entry25.insert(0, str(new_value_en5))
def calculate_totals6(treeview6):
    total6 = 0
    for child in treeview6.get_children():
        total6 += float(treeview6.item(child, 'values')[0])
    Entry16.delete(0, tk.END)
    Entry16.insert(0, str(total6))


    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4
    #new_value = current_value - entry4_value
    new_value_en6 = 100 - total6
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value)))
    (Entry26.delete(0, tk.END))
    Entry26.insert(0, str(new_value_en6))
def calculate_totals7(treeview7):
    total7 = 0
    for child in treeview7.get_children():
        total7 += float(treeview7.item(child, 'values')[0])
    Entry17.delete(0, tk.END)
    Entry17.insert(0, str(total7))
    # احسب القيمة الجديدة لـ Entry5 بطرح قيمة Entry4

    new_value_en7 = 700 - total7
    try:
        entry1_value = float(Entry1.get())
    except ValueError:
        entry1_value = 0

    try:
        entry12_value = float(Entry12.get())
    except ValueError:
        entry12_value = 0
    # تحديث Entry4
    try:
        entry3_value = float(Entry13.get())
    except ValueError:
        entry3_value = 0
    try:
        entry4_value = float(Entry14.get())
    except ValueError:
        entry_value = 0
    try:
        entry5_value = float(Entry15.get())
    except ValueError:
        entry5_value = 0
    try:
        entry6_value = float(Entry16.get())
    except ValueError:
        entry6_value = 0
    try:
        entry7_value = float(Entry17.get())
    except ValueError:
        entry7_value = 0

    Entry4.delete(0, tk.END)
    Entry4.insert(0, str(entry1_value + entry12_value+entry3_value +entry4_value +entry5_value +entry6_value +entry7_value))

    # تحديث Entry5 و Entry2
    Entry5.delete(0, tk.END)
    Entry5.insert(0, str(2000 - (entry1_value + entry12_value + entry3_value +entry4_value +entry5_value +entry6_value+entry7_value)))
    (Entry27.delete(0, tk.END))
    Entry27.insert(0, str(new_value_en7))
    bara(treeview7)

def delete_selected(treeview):
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
        calculate_totals(treeview)
        save_to_csv(treeview)
def delete_selected2(treeview2):
    selected_item = treeview2.selection()
    if selected_item:
        treeview2.delete(selected_item)
        calculate_totals2(treeview2)
        save_to_csv2(treeview2)
def delete_selected3(treeview3):
    selected_item = treeview3.selection()
    if selected_item:
        treeview3.delete(selected_item)
        calculate_totals3(treeview3)
        save_to_csv(treeview3)
def delete_selected4(treeview4):
    selected_item = treeview4.selection()
    if selected_item:
        treeview4.delete(selected_item)
        calculate_totals4(treeview4)
        save_to_csv(treeview4)
def delete_selected5(treeview5):
    selected_item = treeview5.selection()
    if selected_item:
        treeview5.delete(selected_item)
        calculate_totals5(treeview5)
        save_to_csv(treeview5)
def delete_selected6(treeview6):
    selected_item = treeview6.selection()
    if selected_item:
        treeview6.delete(selected_item)
        calculate_totals6(treeview6)
        save_to_csv(treeview6)
def delete_selected7(treeview7):
    selected_item = treeview7.selection()
    if selected_item:
        treeview7.delete(selected_item)
        calculate_totals6(treeview7)
        save_to_csv(treeview7)

def clear_treeview(treeview):
    for item in treeview.get_children():
        treeview.delete(item)
    save_to_csv(treeview)  # حفظ التغييرات في الملف
    Entry1.delete(0, tk.END)  # حذف كل النص في Entry1
    calculate_totals(treeview)
def clear_treeview2(treeview2):
    for item in treeview2.get_children():
        treeview2.delete(item)
    save_to_csv(treeview2)  # حفظ التغييرات في الملف
    Entry12.delete(0, tk.END)
    calculate_totals2(treeview2)
def clear_treeview3(treeview3):
    for item in treeview3.get_children():
        treeview3.delete(item)
    save_to_csv(treeview3)  # حفظ التغييرات في الملف
    Entry13.delete(0, tk.END)
    calculate_totals3(treeview3)
def clear_treeview4(treeview4):
    for item in treeview4.get_children():
        treeview4.delete(item)
    save_to_csv(treeview4)  # حفظ التغييرات في الملف
    Entry14.delete(0, tk.END)
    calculate_totals4(treeview4)
def clear_treeview5(treeview5):
    for item in treeview5.get_children():
        treeview5.delete(item)
    save_to_csv(treeview5)  # حفظ التغييرات في الملف
    Entry15.delete(0, tk.END)
    calculate_totals5(treeview5)
def clear_treeview6(treeview6):
    for item in treeview6.get_children():
        treeview6.delete(item)
    save_to_csv(treeview6)  # حفظ التغييرات في الملف
    Entry16.delete(0, tk.END)
    calculate_totals6(treeview6)
def clear_treeview7(treeview7):
    for item in treeview7.get_children():
        treeview7.delete(item)
    save_to_csv(treeview7)  # حفظ التغييرات في الملف
    Entry17.delete(0, tk.END)
    calculate_totals7(treeview7)

def create_new_frame():
    new_frame = tk.Frame(root)
    new_frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame, text='''légumes''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)
    materials = ["خبز", "بطاطس", "مطيشة", "بصلة", "فلفلة", "ربيع", "بنان", "تفاح", "خيزو", "جلبانة", "دنجال", "عطرية", "نعناع", "خوخ", "خضرة طعام", "حامض", "خيار"]

    entry_mwad = ttk.Combobox(new_frame, values=materials)
    entry_mwad.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad.configure(font="TkFixedFont")

    entry_prix = tk.Entry(new_frame)
    entry_prix.place(relx=0.3, rely=0.25, height=20, relwidth=0.2)
    entry_prix.configure(font="TkFixedFont")

    global trv
    trv = ttk.Treeview(new_frame, selectmode='browse')
    trv.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv["columns"] = ('1',)
    trv.column("#0", width=250, anchor='c')
    trv.column("1", width=100, anchor='c')
    trv.heading("#0", text="mawad", anchor='c')
    trv.heading("1", text="prix", anchor='c')

    load_from_csv(trv)

    new_button1 = tk.Button(new_frame, text="ajout",width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85
    , command=lambda: add_to_treeview(entry_mwad, entry_prix, trv))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d" )
    TOTO.insert(0, Entry1.get())

    L = tk.Label(new_frame, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame, text="supprimer",width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85, command=lambda: delete_selected(trv))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame, text="Hide ",width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)



    clear_button = tk.Button(new_frame,text="S tout",width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview(trv))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame2():
    new_frame2 = tk.Frame(root)
    new_frame2.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame2.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame2, text='''Products''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame2, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)

    materials = [
    "بوطة", "زيت", "طاكوس", "عسل", "كنفتير", "طون", "حليب", "تيد", "ليباط", "اندومي", "فلوطة", "بيض", "سكر",
    "ليباط", "بيض", "فرماج", "dentifrice", "اتاي", "yaghort", "mayiz", "شكلاط", "لانشون", "biscuit", "javil",
    "flota", "سنيكروة", "ميونيز", "سباكيتي", "سميدة طعام", "mia", "chiffon", "cafe", "سنيدة", "دقيق", "خميرة"
     ]

    entry_mwad2 = ttk.Combobox(new_frame2, values=materials)
    entry_mwad2.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad2.configure(font="TkFixedFont")

    entry_prix2 = tk.Entry(new_frame2)
    entry_prix2.place(relx=0.3, rely=0.25, height=20, relwidth=0.2)
    entry_prix2.configure(font="TkFixedFont")

    global trv2
    trv2 = ttk.Treeview(new_frame2, selectmode='browse')
    trv2.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv2["columns"] = ('1',)
    trv2.column("#0", width=250, anchor='c')
    trv2.column("1", width=100, anchor='c')
    trv2.heading("#0", text="mawad", anchor='c')
    trv2.heading("1", text="prix", anchor='c')

    load_from_csv2(trv2)

    new_button1 = tk.Button(new_frame2, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview2(entry_mwad2, entry_prix2,trv2))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame2)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry12.get())

    L = tk.Label(new_frame2, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame2, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected2(trv2))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame2, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame2.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame2, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview2(trv2))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame3():
    new_frame3 = tk.Frame(root)
    new_frame3.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame3.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame3, text='''Viande''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame3, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)

    materials =  [
    "دجاج", "كفتة", "داند", "بقر", "سمطة", "سردين", "بسمان"
      ]

    entry_mwad3 = ttk.Combobox(new_frame3, values=materials)
    entry_mwad3.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad3.configure(font="TkFixedFont")

    entry_prix3 = tk.Entry(new_frame3)
    entry_prix3.place(relx=0.3, rely=0.25, height=20, relwidth=0.2)
    entry_prix3.configure(font="TkFixedFont")

    global trv3
    trv3 = ttk.Treeview(new_frame3, selectmode='browse')
    trv3.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv3["columns"] = ('1',)
    trv3.column("#0", width=250, anchor='c')
    trv3.column("1", width=100, anchor='c')
    trv3.heading("#0", text="mawad", anchor='c')
    trv3.heading("1", text="prix", anchor='c')

    load_from_csv3(trv3)

    new_button1 = tk.Button(new_frame3, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview3(entry_mwad3, entry_prix3,trv3))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame3)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry13.get())

    L = tk.Label(new_frame3, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame3, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected3(trv3))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame3, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame3.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame3, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview3(trv3))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame4():
    new_frame4 = tk.Frame(root)
    new_frame4.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame4.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame4, text='''MOTO''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame4, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)
    materials = [
        "essance", "garage", "pièce","gardien"
    ]

    entry_mwad4 = ttk.Combobox(new_frame4, values=materials)
    entry_mwad4.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad4.configure(font="TkFixedFont")

    entry_prix4 = tk.Entry(new_frame4)
    entry_prix4.place(relx=0.3, rely=0.25, height=20, relwidth=0.2)
    entry_prix4.configure(font="TkFixedFont")

    global trv4
    trv4 = ttk.Treeview(new_frame4, selectmode='browse')
    trv4.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv4["columns"] = ('1',)
    trv4.column("#0", width=250, anchor='c')
    trv4.column("1", width=100, anchor='c')
    trv4.heading("#0", text="mawad", anchor='c')
    trv4.heading("1", text="prix", anchor='c')

    load_from_csv4(trv4)

    new_button1 = tk.Button(new_frame4, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview4(entry_mwad4, entry_prix4,trv4))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame4)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry14.get())

    L = tk.Label(new_frame4, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame4, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected4(trv4))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame4, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame4.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame4, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview4(trv4))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame5():
    new_frame5 = tk.Frame(root)
    new_frame5.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame5.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame5, text='''LINA''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame5, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)
    materials = [
    "حليب", "calin", "زبيب", "كركاع", "لوز", "شوفان", "لباس", "mouchoire", "pirli", "كينطا" ]
    entry_mwad5 = ttk.Combobox(new_frame5, values=materials)
    entry_mwad5.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad5.configure(font="TkFixedFont")

    entry_prix5 = tk.Entry(new_frame5)
    entry_prix5.place(relx=0.3, rely=0.25, height=20, relwidth=0.2)
    entry_prix5.configure(font="TkFixedFont")

    global trv5
    trv5 = ttk.Treeview(new_frame5, selectmode='browse')
    trv5.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv5["columns"] = ('1',)
    trv5.column("#0", width=250, anchor='c')
    trv5.column("1", width=100, anchor='c')
    trv5.heading("#0", text="mawad", anchor='c')
    trv5.heading("1", text="prix", anchor='c')

    load_from_csv5(trv5)

    new_button1 = tk.Button(new_frame5, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview5(entry_mwad5, entry_prix5,trv5))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame5)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry15.get())

    L = tk.Label(new_frame5, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame5, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected5(trv5))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame5, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame5.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame5, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview5(trv5))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame6():
    new_frame6 = tk.Frame(root)
    new_frame6.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame6.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame6, text='''modif''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame6, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)
    materials = []
    entry_mwad6 = ttk.Combobox(new_frame6, values=materials)
    entry_mwad6.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad6.configure(font="TkFixedFont")

    entry_prix6 = tk.Entry(new_frame6)
    (entry_prix6.place(relx=0.3, rely=0.25, height=20, relwidth=0.2))
    entry_prix6.configure(font="TkFixedFont")

    global trv6
    trv6 = ttk.Treeview(new_frame6, selectmode='browse')
    trv6.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv6["columns"] = ('1',)
    trv6.column("#0", width=250, anchor='c')
    trv6.column("1", width=100, anchor='c')
    trv6.heading("#0", text="mawad", anchor='c')
    trv6.heading("1", text="prix", anchor='c')

    load_from_csv6(trv6)

    new_button1 = tk.Button(new_frame6, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview6(entry_mwad6, entry_prix6,trv6))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame6)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry16.get())

    L = tk.Label(new_frame6, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame6, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected6(trv6))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame6, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame6.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame6, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview6(trv6))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)
def create_new_frame7():
    new_frame7 = tk.Frame(root)
    new_frame7.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    new_frame7.configure(relief='groove', borderwidth="2", background="#d7d5aa")

    TOT = tk.Label(new_frame7, text='''modif''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    TOT.place(relx=0.067, rely=0.125, height=43, width=54)
    prix = tk.Label(new_frame7, text='''prix''', anchor='w', background="#d7d5aa",
                   font="-family {Segoe UI} -size 10 -weight bold", foreground="black")
    prix.place(relx=0.067, rely=0.23, height=43, width=54)
    materials =[
     "خالتي", "مركوب", "بابوش", "زريعة", "مركوب خالتي", "كينة ","بومادة", "بطارية",
    "cafe", "زريعة", "تشيبس", "كبال", "لبن", "كينة الراس", "سكوتش", "ستيلو", "بريكات",
    "زريعة", "لبن", "زريعة", "coiffeur", "روز", "تشيشة", "بابوش", "سكر", "كينة",
    "نفاخة", "زريعة", "حمص"]

    entry_mwad7 = ttk.Combobox(new_frame7, values=materials)
    entry_mwad7.place(relx=0.3, rely=0.15, height=20, relwidth=0.2)
    entry_mwad7.configure(font="TkFixedFont")

    entry_prix7 = tk.Entry(new_frame7)
    (entry_prix7.place(relx=0.3, rely=0.25, height=20, relwidth=0.2))
    entry_prix7.configure(font="TkFixedFont")

    global trv7
    trv7 = ttk.Treeview(new_frame7, selectmode='browse')
    trv7.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)
    trv7["columns"] = ('1',)
    trv7.column("#0", width=250, anchor='c')
    trv7.column("1", width=100, anchor='c')
    trv7.heading("#0", text="mawad", anchor='c')
    trv7.heading("1", text="prix", anchor='c')

    load_from_csv7(trv7)

    new_button1 = tk.Button(new_frame7, text="ajout", width=88, bg='green', bd=1, relief=SOLID, cursor='hand2', height=85,
                            command=lambda: add_to_treeview7(entry_mwad7, entry_prix7,trv7))
    new_button1.place(relx=0.6, rely=0.1, height=30, width=80)

    TOTO = tk.Entry(new_frame7)
    TOTO.place(relx=0.6, rely=0.4, height=30, width=80)
    TOTO.configure(cursor='hand2', foreground='red', font="-family {Segoe UI} -size 14 -weight bold", disabledforeground="#9d9d9d")
    TOTO.insert(0, Entry17.get())

    L = tk.Label(new_frame7, text='''TOT''', anchor='w', background="#d7d5aa",
                 font="-family {Segoe UI} -size 14 -weight bold", foreground="black")
    L.place(relx=0.8, rely=0.4, height=30, width=80)

    delete_button = tk.Button(new_frame7, text="supprimer", width=88, bg='#EA582A', bd=1, relief=SOLID, cursor='hand2', height=85,
                              command=lambda: delete_selected7(trv7))
    delete_button.place(relx=0.6, rely=0.2, height=30, width=80)

    hide_button = tk.Button(new_frame7, text="Hide ", width=88, bg='#DFD610', bd=1, relief=SOLID, cursor='hand2', command=new_frame7.destroy)
    hide_button.place(relx=0.8, rely=0.01, height=30, width=80)

    clear_button = tk.Button(new_frame7, text="S tout", width=88, bg='#DF1010', bd=1, relief=SOLID, cursor='hand2', command=lambda: clear_treeview7(trv7))
    clear_button.place(relx=0.6, rely=0.3, height=30, width=80)



Button1 = tk.Button(Frame1, text="خضروات", command=create_new_frame)
Button1.place(relx=0.05, rely=0.052, height=66, width=87)
Button1.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img1)
Button2 = tk.Button(Frame1, text="BIM", command=create_new_frame2)
Button2.place(relx=0.29, rely=0.052, height=66, width=87)
Button2.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img2)
Button3 = tk.Button(Frame1, text="Viande", command=create_new_frame3)
Button3.place(relx=0.53, rely=0.052, height=66, width=87)
Button3.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img3)
Button4 = tk.Button(Frame1, text="Viande", command=create_new_frame4)
Button4.place(relx=0.77, rely=0.052, height=66, width=87)
Button4.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img4)
Button5 = tk.Button(Frame1, text="Viande", command=create_new_frame5)
Button5.place(relx=0.05, rely=0.6, height=66, width=87)
Button5.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img5)
Button6 = tk.Button(Frame1, text="Viande", command=create_new_frame6)
Button6.place(relx=0.29, rely=0.6, height=66, width=87)
Button6.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img6)
Button7 = tk.Button(Frame1, text="Viande", command=create_new_frame7)
Button7.place(relx=0.53, rely=0.6, height=66, width=87)
Button7.configure(activebackground="#d9d9d9", activeforeground="black", background=_bgcolor, foreground=_fgcolor,image=img7)

Frame2 = tk.Frame(root)
Frame2.place(relx=0.0, rely=0.015, relheight=0.42, relwidth=1.014)
Frame2.configure(relief='groove', borderwidth="2", background="#d7d5aa", highlightbackground=_bgcolor, highlightcolor=_fgcolor)

Label1 = tk.Label(Frame2)
Label1.place(relx=0.099, rely=0.182, height=43, width=54)
Label1.configure(activebackground="#d9d9d9", text='''TOT''', activeforeground="black", anchor='w',
                 background="#d7d5aa", compound='left', disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 14 -weight bold",
                 foreground="blue", highlightbackground=_bgcolor)
Label22 = tk.Label(Frame2)
Label22.place(relx=0.099, rely=0.55, height=42, width=54)
Label22.configure(activebackground="#d9d9d9", text='''REST''', activeforeground="black", anchor='w',
                 background="#d7d5aa", compound='left', disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 14 -weight bold",
                 foreground="green", highlightbackground=_bgcolor)

Entry4 = tk.Entry(Frame2)
Entry4.place(relx=0.269, rely=0.143, height=60, relwidth=0.141)
Entry4.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="blue", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")
Buttoncontrol = tk.Button(Frame2, text="CONTRÔLE", command=frame_control,bg='#6D8B74', bd=1, relief=SOLID, cursor='hand2')
Buttoncontrol.place(relx=0.01, rely=0.001, height=30, width=65)

def save_entry4():
    with open('entry4.txt', 'w') as file:
        file.write(Entry4.get())
# دالة لتحميل الرقم من الملف عند بدء البرنامج
def load_entry4():
    if os.path.exists('entry4.txt'):
        with open('entry4.txt', 'r') as file:
            Entry4.insert(0, file.read())
# تحميل الرقم عند بدء البرنامج
load_entry4()

Entry5 = tk.Entry(Frame2)
Entry5.place(relx=0.269, rely=0.51, height=60, relwidth=0.141)
Entry5.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground="green", font="-family {Segoe UI} -size 16 -weight bold", disabledforeground="#9d9d9d")

# دالة لحفظ الرقم في Entry5 عند إغلاق البرنامج
def save_entry5():
    with open('entry5.txt', 'w') as file:
        file.write(Entry5.get())
# دالة لتحميل الرقم من الملف عند بدء البرنامج
def load_entry5():
    if os.path.exists('entry5.txt'):
        with open('entry5.txt', 'r') as file:
            Entry5.insert(0, file.read())
# تحميل الرقم عند بدء البرنامج
load_entry5()

Entry6 = tk.Entry(Frame2)
Entry6.place(relx=0.773, rely=0.143, height=20, relwidth=0.141)
Entry6.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground=_fgcolor, font="TkFixedFont", disabledforeground="#9d9d9d")
Label2 = tk.Label(Frame2)
Label2.place(relx=0.655, rely=0.143, height=22, width=34)
Label2.configure(activebackground="#d9d9d9", activeforeground="black", anchor='w', background='#d7d5aa', compound='left',
                 disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 10", foreground="black", highlightbackground=_bgcolor,
                 highlightcolor=_fgcolor, text='''خبز''')

Entry7 = tk.Entry(Frame2)
Entry7.place(relx=0.773, rely=0.23, height=20, relwidth=0.141)
Entry7.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground=_fgcolor, font="TkFixedFont", disabledforeground="#9d9d9d")
Label3 = tk.Label(Frame2)
Label3.place(relx=0.655, rely=0.23, height=22, width=34)
Label3.configure(activebackground="#d9d9d9", activeforeground="black", anchor='w', background='#d7d5aa', compound='left',
                 disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 10", foreground="black", highlightbackground=_bgcolor,
                 highlightcolor=_fgcolor, text='''خضر''')

Entry8 = tk.Entry(Frame2)
Entry8.place(relx=0.773, rely=0.32, height=20, relwidth=0.141)
Entry8.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground=_fgcolor, font="TkFixedFont", disabledforeground="#9d9d9d")
Label3 = tk.Label(Frame2)
Label3.place(relx=0.655, rely=0.32, height=22, width=34)
Label3.configure(activebackground="#d9d9d9", activeforeground="black", anchor='w', background='#d7d5aa', compound='left',
                 disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 10", foreground="black", highlightbackground=_bgcolor,
                 highlightcolor=_fgcolor, text='''فواكه''')
Entry9 = tk.Entry(Frame2)
Entry9.place(relx=0.773, rely=0.41, height=20, relwidth=0.141)
Entry9.configure(background=_bgcolor, insertbackground=_fgcolor, highlightcolor=_fgcolor, highlightbackground=_bgcolor,
                 foreground=_fgcolor, font="TkFixedFont", disabledforeground="#9d9d9d")
Label3 = tk.Label(Frame2)
Label3.place(relx=0.655, rely=0.41, height=22, width=34)
Label3.configure(activebackground="#d9d9d9", activeforeground="black", anchor='w', background='#d7d5aa', compound='left',
                 disabledforeground="#9d9d9d", font="-family {Segoe UI} -size 10", foreground="black", highlightbackground=_bgcolor,
                 highlightcolor=_fgcolor, text='''برا''')

def khobztotal(treeview):
    total = 0
    for child in treeview.get_children():
        item_text = treeview.item(child, 'text')
        if item_text == 'خبز':
            try:
                value = float(treeview.item(child, 'values')[0])
                total += value
            except ValueError:
                print(f"Error converting value: {treeview.item(child, 'values')[0]}")

    Entry6.delete(0, tk.END)
    Entry6.insert(0, str(total))
def khodar(treeview):
    total = 0
    vegetables = ['بطاطس', 'بصلة', 'مطيشة', 'فلفلة', 'خيزو', 'ربيع', 'خضر', 'خضرة طعام', 'جلبانة', 'دنجال', 'حامض', 'خيار']
    for child in treeview.get_children():
        item_text = treeview.item(child, 'text')
        if item_text in vegetables:
            try:
                value = float(treeview.item(child, 'values')[0])
                total += value
            except ValueError:
                print(f"Error converting value: {treeview.item(child, 'values')[0]}")

    Entry7.delete(0, tk.END)
    Entry7.insert(0, str(total))
def fawakih(treeview):
    total = 0
    fruit = ['تفاح', 'بنان', 'خوخ', 'فواكه']
    for child in treeview.get_children():
        item_text = treeview.item(child, 'text')
        if item_text in fruit:
            try:
                value = float(treeview.item(child, 'values')[0])
                total += value
            except ValueError:
                print(f"Error converting value: {treeview.item(child, 'values')[0]}")

    Entry8.delete(0, tk.END)
    Entry8.insert(0, str(total))
def bara(treeview7):
    total = 0
    fruit = ["بابوش", "زريعة", "cafe", "زريعة", "تشيبس", "كبال",]
    for child in treeview7.get_children():
        item_text = treeview7.item(child, 'text')
        if item_text in fruit:
            try:
                value = float(treeview7.item(child, 'values')[0])
                total += value
            except ValueError:
                print(f"Error converting value: {treeview7.item(child, 'values')[0]}")

    Entry9.delete(0, tk.END)
    Entry9.insert(0, str(total))
# حفظ الرقم عند إغلاق البرنامج
root.protocol("WM_DELETE_WINDOW", lambda: [save_entry4(), save_entry2(),save_entry1(),save_entry22()
              ,save_entry12(),save_entry23(),save_entry13(),save_entry24(),save_entry14(),save_entry25(),save_entry15(),save_entry26(),save_entry16()
              ,save_entry27(),save_entry17(), root.destroy()])

root.mainloop()

