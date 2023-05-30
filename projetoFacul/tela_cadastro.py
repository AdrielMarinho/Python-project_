from tkinter import Tk, Frame, Label, Entry, Button
import events as ev
import sql_commands as sqlc
import tela_login as tl


def signup_screen(window_a):
    window_a.destroy()

    def temporary_text(e):
        input_tel.delete(0, "end")

    def temporary_text2(e):
        input_password.delete(0, "end")

    window = Tk()
    window.geometry(ev.center(window))

    window.title("Cadastro")
    window.resizable(False, False)

    frame = Frame(master=window, width=750, height=450, bg="#000000")
    frame.pack()

    ev.bg_fun(frame)

    lb_name = Label(frame, text="Nome: ", bg="#000000", fg="#FFFFFF")
    lb_name.place(x=12, y=28)
    input_name = Entry(frame, width=45, fg="#000000")
    input_name.place(x=73, y=28)

    lb_cpf = Label(frame, text="CPF: ", bg="#000000", fg="#FFFFFF")
    lb_cpf.place(x=12, y=68)
    input_cpf = Entry(frame, width=45, fg="#000000")
    input_cpf.place(x=73, y=68)

    lb_email = Label(frame, text="Email: ", bg="#000000", fg="#FFFFFF")
    lb_email.place(x=12, y=108)
    input_email = Entry(frame, width=45, fg="#000000")
    input_email.place(x=73, y=108)

    lb_endereco = Label(frame, text="Endereço: ", bg="#000000", fg="#FFFFFF")
    lb_endereco.place(x=12, y=148)
    input_endereco = Entry(frame, width=45, fg="#000000")
    input_endereco.place(x=75, y=148)

    lb_complemento = Label(frame, text="Complemento: ", bg="#000000", fg="#FFFFFF")
    lb_complemento.place(x=12, y=188)
    input_complemento = Entry(frame, width=40, fg="#000000")
    input_complemento.place(x=105, y=188)

    lb_tel = Label(frame, text="Telefone: ", bg="#000000", fg="#FFFFFF")
    lb_tel.place(x=12, y=223)
    input_tel = Entry(frame, width=45, fg="#000000")
    input_tel.insert(0, "(DDD) Número")
    input_tel.bind("<FocusIn>", temporary_text)
    input_tel.place(x=72, y=223)

    lb_password = Label(frame, text="Senha: ", bg="#000000", fg="#FFFFFF")
    lb_password.place(x=12, y=260)
    input_password = Entry(frame, width=45, fg="#000000", show="*")
    input_password.insert(0, "No mínimo 6 caracteres")
    input_password.bind("<FocusIn>", temporary_text2)
    input_password.place(x=72, y=260)

    lb_password_conf = Label(frame, text="Confirmar senha: ", bg="#000000", fg="#FFFFFF")
    lb_password_conf.place(x=12, y=300)
    input_password_conf = Entry(frame, width=38, fg="#000000", show="*")
    input_password_conf.place(x=115, y=300)

    signup_button = Button(text="Cadastrar", bg='#000000', fg='#FFFFFF', bd=2,
                           command=lambda: sqlc.table_signup(input_cpf, input_name, input_email, input_endereco,
                                                             input_complemento, input_tel, input_password,
                                                             input_password_conf, window))
    signup_button.place(x=200, y=374, width=150, height=30)

    back_button = Button(text="Voltar", bg='#000000', fg='#FFFFFF', bd=2, command=lambda: [window.destroy(),
                                                                                           tl.login_screen()])
    back_button.place(x=400, y=374, width=150, height=30)
    window.mainloop()
