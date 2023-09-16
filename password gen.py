#DISCLAIMER: THIS CODE IS UNREADABLE AND IF YOU TRY TO READ IT MIGHT GIVE YOU A MIGRAINE ADVANCE AT YOUR OWN RISK(NO REALLY I'M NOT JOKING)
import random, string , pyperclip
import tkinter as tk

key = Fernet.generate_key()
fernet = Fernet(key)
paslist = []
window = tk.Tk()

window.iconphoto(False, tk.PhotoImage(file='manager(1).png'))


def num():
    randint = str(random.randint(1, 10))
    paslist.append(randint)

def save(x , y , z):
    datasite = x.get()
    dataname = y.get()
    datapass = z.get()     
    f = open("password.txt" , "a")
    f.write("Site Name: " + datasite + "\n" )
    f.write("Username/E-mail: " + dataname + "\n")
    f.write("Password: " + datapass + "\n" )
    f.close()
    
def let():
    rand = random.choice(string.ascii_letters)
    paslist.append(rand)
def copy_Fun(pasword):
    pyperclip.copy(pasword)

def obliviate():
    global window
    window.destroy()
    window = tk.Tk()
    window.title("Password Manager")
    window.iconphoto(False, tk.PhotoImage(file='manager(1).png'))
    window.resizable(True, True)
    window.configure(bg='#2be334')

    labelsite = tk.Label(text="Enter Site Name").pack()
    entrysite = tk.Entry(width=35)
    entrysite.pack()
    labelpass = tk.Label(text="Password").pack()
    entrypass = tk.Entry(width=35)
    entrypass.pack()
    labelname = tk.Label(text="Username/E-mail").pack()
    entryname = tk.Entry(width=35)
    entryname.pack()
    savebtn = tk.Button(text= "Save" ,command=lambda:save(Entrysite,Entryname,Entrypass))
    savebtn.pack(pady = 20) 
    window.mainloop()
copybtn = tk.Button(text='')

copy = tk.PhotoImage(file="copy.png")


    

def thing():
    pas = 0
    while pas != 12:
        global paslist
        dec = (random.randint(0, 1))
        if dec == 1:
            num()
        elif dec == 0:
            let()
        pas = len(paslist)
    password = ' '.join(paslist)
    password = password.replace(" ", "")
    global copybtn
    copybtn.config(image=copy,
                   text=password,
                   compound=tk.BOTTOM , command = copy_Fun(password)
)


window.title("Password Manager")
window.geometry("600x400+50+50")
window.resizable(True, True)
photo1 = tk.PhotoImage(file="disk(1)(1).png")
window.configure(bg='#2be334')
create = tk.Button(window,
                   text="Generate a Password",
                   width=25,
                   height=7,
                   bg="#fa880c",
                   fg="black",
                   command=thing).place(x=110, y=140)
savebtn = tk.Button(window,
                 text="save an existing password",
                 image=photo1,
                 compound=tk.BOTTOM,
                 command=obliviate).place(x=425, y=155)

    
copybtn.pack(pady=20)
window.mainloop()
