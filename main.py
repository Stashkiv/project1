from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Вхід в систему")
def registration():
    text = Label(text="Зареєструйтесь")
    text_log = Label(text="Введіть логін:")
    registr_lodin = Entry()
    text_password = Label(text="Введіть пароль")
    registr_password = Entry(show="*")
    button_registr = Button(text="Зареєструватись", command= lambda: save())
    text.pack()
    text_log.pack()
    registr_lodin.pack()
    text_password.pack()
    registr_password.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_lodin.get()]=registr_password.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Тепер ви можете війти")
    text_enter_login = Label(text="введіть логін")
    enter_login = Entry()
    text_enter_pass = Label(text="введіть пароль")
    enter_pass = Entry(show="*")
    button_enter = Button(text="Війти", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("hello")
            else:
                messagebox.showerror("error")
        else:
            messagebox.showerror("ERROR", "не правильний логін або пароль")

registration()
root.mainloop()