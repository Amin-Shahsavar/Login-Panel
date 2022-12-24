import tkinter

def login(phone):
    phone = {'phone' : '09300968349'}

    if phone_entry.get() == phone['phone']:
        check_code()

    else:
        print('phone nymber is incorect')
    

def check_code(code):
    code = {'code' : '1234'}
    if code_entry.get() == code['code']:
        print('login sucssecful')
    win_code = tkinter.Tk()
    win_code.geometry('200x200')
    win_code.title('Sended Code')

    code_lable = tkinter.Label(win_code , text='Sended Code').pack()
    code_entry = tkinter.Entry(win_code).pack()
    code_bottun = tkinter.Button(win_code , text='check').pack()

win_phone = tkinter.Tk()
win_phone.geometry('200x200')
win_phone.title('Phone Number')

phone_label = tkinter.Label(win_phone , text='Phone Number').pack()
phone_entry = tkinter.Entry(win_phone).pack()
phone_botton = tkinter.Button(win_phone , text='Send Code' , command=login).pack()


tkinter.mainloop()