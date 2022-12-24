from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

userpass={
    "admin":"1234"
    }

def signin(event='None'):
    username=user.get()
    password=code.get()
    print(username)
    print(userpass.keys())
    if username in userpass.keys() and password in userpass.values():
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Hello Everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username not in userpass.keys() and password not in userpass.values():
        messagebox.showerror("Invalid","invalid username and password\nCreate a account first!")
    
    elif password not in userpass.values():
        messagebox.showerror("Invalid","invalid password")
    
    elif username not in userpass.keys():
        messagebox.showerror("Invalid","invalid username")

def signup():
    username=user.get()
    password=code.get()
    userpass[username]=password
    print(userpass)
    messagebox.showerror("OK","Sign Up was sucseccful")

def QUIT(event='None'):
    root.destroy()
    quit()

img=PhotoImage(file=r"C:\Users\top.TOP-PC\Desktop\Code\py proj\Login Form\Calculator icon.png")
Label(root,image=img,bg='white').place(x=40,y=40)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft yaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

######---------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft yaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

######---------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='black',border=0,bg="white",show='*',font=('Microsoft yaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

######---------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft yaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)


root.bind('<Return>',signin)
root.bind('<Escape>',QUIT)
root.mainloop()
