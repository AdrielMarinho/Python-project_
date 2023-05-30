from tkinter import Tk, Entry, Button, Label, Frame
import events as ev
import sql_commands as sqlc
import tela_cadastro as tlc


def login_screen():
    window = Tk()
    window.title("Login")

    window.resizable(False, False)
    window.geometry(ev.center(window))

    frame = Frame(master=window, width=750, height=450)
    frame.pack()

    ev.bg_fun(frame)

    input_a = Entry(frame, width=45, fg="#000000")
    input_a.bind('<FocusIn>')
    input_a.place(x=250, y=178)

    input_b = Entry(frame, width=45, fg="#000000", show="*")
    input_b.bind('<FocusIn>')
    input_b.place(x=250, y=238)

    email_label = Label(frame, text='Email', fg="#FFFFFF", bg="#000000")
    email_label.place(x=250, y=150)

    password_label = Label(frame, text='Senha', fg="#FFFFFF", bg="#000000")
    password_label.place(x=250, y=210)

    button_login = Button(text="Entrar", bd=2, fg="#FFFFFF", bg="#121212", font=('inter', 10, 'bold'),
                          command=lambda: sqlc.table_login(input_a, input_b, window))
    button_login.place(x=296, y=298, width=150, height=30)

    button_signup = Button(text="Cadastrar", bd=2, fg="#FFFFFF", bg="#121212", font=('inter', 10, 'bold'),
                           command=lambda: [sqlc.create_table(), tlc.signup_screen(window)])
    button_signup.place(x=296, y=364, width=150, height=30)

    frame.mainloop()
