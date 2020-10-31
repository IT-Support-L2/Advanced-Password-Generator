import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile 
import webbrowser
import random
import string
from tkinter import messagebox



root = tk.Tk()
root.title("P-GEN")

width=600
height=550
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)


passLen = IntVar()
passNum = IntVar()

def randompassword():

  while int(passLen.get()) >= 8 and int(passNum.get()) >= 1:

    punc = "!#($%&*+}-/<=)>?@[\]^{|"

    uchars = int(passLen.get() / 4)

    lchars = int(passLen.get() / 4)

    dchars = int(passLen.get() / 4)

    schars = int(passLen.get() / 4)

    str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''

    for i in range(uchars):
        str_uchars += random.SystemRandom().choice(string.ascii_uppercase)

    for i in range(lchars):
        str_uchars += random.SystemRandom().choice(string.ascii_lowercase)

    for i in range(dchars):
        str_uchars += random.SystemRandom().choice(string.digits)

    for i in range(schars):
        str_uchars += random.SystemRandom().choice(punc)

    random_str = str_uchars + str_lchars + str_dchars + str_schars

    random_str = ''.join(random.sample(random_str, len(random_str)))

    l = list(random_str)

    random.shuffle(l)

    result = ''.join(l)

    return str(result)

def output():
  n = 0
  while n < passNum.get():
    paStr = randompassword() + '\n'
    n=n+1
    generated_pass.insert('1.0', paStr)

def copy():
    field_value = generated_pass.get("1.0", 'end-1c')  
    copy_pass.clipboard_clear() 
    copy_pass.clipboard_append(field_value)
    copy_pass.update()

def clearr():
    generated_pass.delete('1.0', END)

def linked_in():
    url='https://linkedin.com/in/cyber-services'
    webbrowser.open_new_tab(url)

def git_hub():
    url='https://github.com/IT-Support-L2'
    webbrowser.open_new_tab(url)

def save(): 
    f = asksaveasfile(mode='w', defaultextension=".txt")
    text2save = str(generated_pass.get(1.0, END))
    f.write(text2save)
    f.close()


title_bar=tk.Label(root)
title_bar["bg"] = "#393d49"
ft = tkFont.Font(family='Arial',size=18)
title_bar["font"] = ft
title_bar["fg"] = "#33ed3f"
title_bar["justify"] = "center"
title_bar["text"] = "P-GEN"
title_bar["relief"] = "flat"
title_bar.place(x=0,y=0,width=600,height=31)

description=tk.Label(root)
description["borderwidth"] = "3px"
ft = tkFont.Font(family='Arial',size=10)
description["font"] = ft
description["fg"] = "#333333"
description["justify"] = "left"
description["text"] = "P-GEN generates secure complex passwords composed of" + "\n" + "uppercase and lowercase letters, digits and punctuations." + "\n" + "Chars length must be a multiple of 4." + "\n" + "Example of length inputs: 8 (minimum), 12, 16, 20, 24, 30, ect." + "\n" + "Else, you can generate passwords as much as you need, minimum input is 1."
description["relief"] = "raised"
description.place(x=60,y=45,width=490,height=98)

enter_chars=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
enter_chars["font"] = ft
enter_chars["fg"] = "#333333"
enter_chars["justify"] = "left"
enter_chars["text"] = "Chars Length"
enter_chars["relief"] = "groove"
enter_chars.place(x=20,y=160,width=142,height=30)


pass_length=tk.Entry(root)
pass_length["bg"] = "#d2f4d4"
pass_length["borderwidth"] = "3px"
ft = tkFont.Font(family='Arial',size=10)
pass_length["font"] = ft
pass_length["fg"] = "#333333"
pass_length["justify"] = "center"
pass_length["text"] = ""
pass_length["relief"] = "sunken"
pass_length.place(x=220,y=160,width=142,height=30)
pass_length["textvariable"] = passLen


enter_passN=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
enter_passN["font"] = ft
enter_passN["fg"] = "#333333"
enter_passN["justify"] = "left"
enter_passN["text"] = "Passwords Number"
enter_passN["relief"] = "groove"
enter_passN.place(x=20,y=210,width=142,height=30)


pass_num=tk.Entry(root)
pass_num["bg"] = "#d2f4d4"
pass_num["borderwidth"] = "3px"
ft = tkFont.Font(family='Arial',size=10)
pass_num["font"] = ft
pass_num["fg"] = "#333333"
pass_num["justify"] = "center"
pass_num["text"] = ""
pass_num["relief"] = "sunken"
pass_num.place(x=220,y=210,width=142,height=30)
pass_num["textvariable"] = passNum

gen_pass=tk.Button(root)
gen_pass["activebackground"] = "#7ff14e"
gen_pass["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
gen_pass["font"] = ft
gen_pass["fg"] = "#000000"
gen_pass["justify"] = "center"
gen_pass["text"] = "Generate Passwords"
gen_pass["relief"] = "raised"
gen_pass.place(x=20,y=270,width=142,height=30)
gen_pass["command"] = output

generated_pass=tk.Text(root)
generated_pass["bg"] = "#d2f4d4"
generated_pass["borderwidth"] = "3px"
ft = tkFont.Font(family='Arial',size=10)
generated_pass["font"] = ft
generated_pass["fg"] = "#333333"
generated_pass["relief"] = "sunken"
generated_pass.place(x=220,y=270,width=346,height=192)

copy_pass=tk.Button(root)
copy_pass["activebackground"] = "#7ff14e"
copy_pass["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
copy_pass["font"] = ft
copy_pass["fg"] = "#000000"
copy_pass["justify"] = "center"
copy_pass["text"] = "Copy Passwords"
copy_pass["relief"] = "raised"
copy_pass.place(x=20,y=320,width=142,height=30)
copy_pass["command"] = copy


export=tk.Button(root)
export["activebackground"] = "#7ff14e"
export["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
export["font"] = ft
export["fg"] = "#000000"
export["justify"] = "center"
export["text"] = "Export"
export["relief"] = "raised"
export.place(x=20,y=370,width=142,height=30)
export["command"] = lambda : save()


linkedin=tk.Button(root)
linkedin["activebackground"] = "#7ff14e"
linkedin["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
linkedin["font"] = ft
linkedin["fg"] = "#000000"
linkedin["justify"] = "center"
linkedin["text"] = "Linkedin"
linkedin["relief"] = "raised"
linkedin.place(x=20,y=420,width=142,height=30)
linkedin["command"] = linked_in

github=tk.Button(root)
github["activebackground"] = "#7ff14e"
github["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
github["font"] = ft
github["fg"] = "#000000"
github["justify"] = "center"
github["text"] = "Github"
github["relief"] = "raised"
github.place(x=20,y=470,width=142,height=30)
github["command"] = git_hub

cleaar=tk.Button(root)
cleaar["activebackground"] = "#7ff14e"
cleaar["bg"] = "#efefef"
ft = tkFont.Font(family='Arial',size=10)
cleaar["font"] = ft
cleaar["fg"] = "#000000"
cleaar["justify"] = "center"
cleaar["text"] = "Clear"
cleaar["relief"] = "raised"
cleaar.place(x=220,y=470,width=346,height=30)
cleaar["command"] = clearr

foo_ter=tk.Label(root)
foo_ter["bg"] = "#393d49"
ft = tkFont.Font(family='Arial',size=10)
foo_ter["font"] = ft
foo_ter["fg"] = "#33ed3f"
foo_ter["justify"] = "center"
foo_ter["text"] = "By Cyber-Tech ® 2020"
foo_ter["relief"] = "flat"
foo_ter.place(x=0,y=520,width=600,height=31)

  
if __name__ == "__main__":
    
    root.mainloop()
