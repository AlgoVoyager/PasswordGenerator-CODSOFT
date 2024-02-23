import random
import string
from tkinter import *

import pyperclip

usenum, usealpha, usesym = True, True, True
passwlen = 0

def genpass(inp):
    global usenum, usealpha, usesym, passwlen
    passwlen = int(inp)
    if passwlen < 4:
        print("minimum password length should be 4, Try again...")
        return

    passw = ""
    while len(passw) < passwlen:
        charSet = random.randrange(3)
        if charSet == 0 and usenum:
            passw += str(random.randint(0, 9))
        if charSet == 1 and usealpha:
            passw += random.choice(string.ascii_letters)
        if charSet == 2 and usesym:
            passw += random.choice("~!@#$%^&*()_+=-?/")
    equation.set(passw)

def checkop():
    global usenum, usealpha, usesym
    usenum = Checkbutton1.get()
    usealpha = Checkbutton2.get()
    usesym = Checkbutton3.get()
def mlen(getplen):
    if int(getplen) >4:
        plen.set(str(int(getplen)-1))
def alen(getplen):
    plen.set(str(int(getplen)+1))
if __name__ == "__main__":
    window = Tk()
    window.configure(background="#DBEAFE")
    window.title("Password Generator")
    window.geometry("450x300")
    window.resizable(False, False)

    equation = StringVar()
    plen = StringVar()
    plen.set("8")

    font_size = 14

    len_lb = Label(window, text="Password Length: ")
    len_lb.configure(background="#DBEAFE", fg='#0E2954', font=("Arial", font_size))
    len_lb.grid(row=0, column=1)
    rlen = Button(window, text=' - ', fg='#0E2954', bg='#DBEAFE',command=lambda: mlen(pass_len.get()),font=("Arial", font_size))
    rlen.grid(row=2, column=0)
    pass_len = Entry(window, width=4, textvariable=plen,justify='center')
    pass_len.configure(background="#93C5FD", fg='#0E2954', font=("Arial", font_size))
    pass_len.grid(row=2, column=1)
    rlen = Button(window, text=' + ', fg='#0E2954', bg='#DBEAFE', command=lambda: alen(pass_len.get()), font=("Arial", font_size))
    rlen.grid(row=2, column=2)

    Checkbutton1 = BooleanVar()
    Checkbutton2 = BooleanVar()
    Checkbutton3 = BooleanVar()
    Checkbutton1.set(True)
    Checkbutton2.set(True)
    Checkbutton3.set(True)

    Button1 = Checkbutton(window, text="Numbers",
                          variable=Checkbutton1,
                          onvalue=True,
                          offvalue=False,
                          height=2,
                          width=10,
                          command=checkop)

    Button2 = Checkbutton(window, text="Alphabets",
                          variable=Checkbutton2,
                          onvalue=True,
                          offvalue=False,
                          height=2,
                          width=10,
                          command=checkop)

    Button3 = Checkbutton(window, text="Symbols",
                          variable=Checkbutton3,
                          onvalue=True,
                          offvalue=False,
                          height=2,
                          width=10,
                          command=checkop)

    Button1.configure(background="#DBEAFE", fg='#0E2954', font=("Arial", font_size))
    Button2.configure(background="#DBEAFE", fg='#0E2954', font=("Arial", font_size))
    Button3.configure(background="#DBEAFE", fg='#0E2954', font=("Arial", font_size))
    Button1.grid(row=3, column=0)
    Button2.grid(row=3, column=1)
    Button3.grid(row=3, column=2)

    pass_field = Entry(window, textvariable=equation,justify='center')
    pass_field.configure(background="#93C5FD", fg='#0E2954', font=("Arial", font_size))
    pass_field.grid(row=5, column=0, columnspan=4, ipadx=10, ipady=10, padx=10, pady=10)

    Genbtn = Button(window, text='Generate', fg='#0E2954', bg='#60A5FA',
                    command=lambda: genpass(pass_len.get()), height=1, width=10, font=("Arial", font_size))
    Genbtn.grid(row=6, column=1)
    Copybtn = Button(window, text='Copy', fg='#0E2954', bg='#2E8A99',
                     command=lambda :pyperclip.copy(equation.get()), height=1, width=5, font=("Arial", 10))
    Copybtn.grid(row=4, column=1)
    window.mainloop()
