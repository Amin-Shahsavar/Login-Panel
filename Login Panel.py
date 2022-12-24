import tkinter
from tkinter.ttk import *

def login(U , P):
    user_pass = {
        'password' : '7981',
        'username' : 'admin'
        }

    U = U.lower()
    if U not in user_pass:
        S = "Username Not Found!"
        condition_label.config(text=S,font=("tahoma',40,'italic'"),fg='red')
        print(S)
        
#         continue

    elif user_pass[U] == P:
        S = "Login Successful!"
        print(S)
        condition_label.config(text=S,font=("tahoma',40,'italic'"),fg='green')
        return True
            #break
    else: 
        S = "Incorrect Password!\nLogin Failed!"
        print(S)
        condition_label.config(text=S,font=("tahoma',40,'italic'"),fg='#ff0000')
        exit(0)

def SignUp(U , P):
    user_pass = {'Amin' : '7981'}
    user_pass['{U}'] = '{P}'

def GET():
    U = user_entry.get()
    P = pass_entry.get()
    S = f'welcome {U}\nYour Password is: {P}'
    print(S)
    condition_label.config(text=S , font=("tahoma',40,'italic'"))

def QUIT(event='None'):
    login_win.destroy()
    quit()

#Login panel
login_win = tkinter.Tk()
login_win.title('Login Panel')
login_win.geometry('400x250')
login_win.configure(bg="#333333")
win_frame = tkinter.Frame(bg='#333333')

# Panel Label
panel_label = tkinter.Label(win_frame , text='Login' , bg='#333333' , fg='#FF3399' , font=('times' , 30 , 'bold'))
panel_label.grid(row=0 , column=0 , columnspan=2)

# Label and Entry of username
user_label = tkinter.Label(win_frame , text='Username: ' ,bg='#333333' , fg='#FF3399' , font=('times' , 20 , 'bold'))
user_label.grid(row=1 , column=0)
user_entry = tkinter.Entry(win_frame)
user_entry.grid(row=1 , column=1)
user_entry.focus_set()

# Label and Entry of password
pass_label = tkinter.Label(win_frame , text='Password: ' , bg='#333333' , fg='#FF3399', font=('times' , 20 , 'bold'))
pass_label.grid(row=2 , column=0)
pass_entry = tkinter.Entry(win_frame , show='*')
pass_entry.grid(row=2 , column=1)

# Sign In button
signin_button = tkinter.Button(win_frame , text='Sign In' , bg='#FF3399' , command=GET)
signin_button.grid(row=3 , column=0 , columnspan=2)

# Sing Up button
singup_button = tkinter.Button(win_frame , text='Sign Up' , bg='#FF3399' , command=SignUp)
singup_button.grid(row=4 , column=0 , columnspan=2)

# Label of login condition
condition_label = tkinter.Label(win_frame , bg='#333333' , fg='#ffffff')
condition_label.grid(row=5 , column=0 , columnspan=2)

login_win.bind('<Return>',GET)
login_win.bind('<Escape>',QUIT)
win_frame.pack()
login_win.mainloop()
