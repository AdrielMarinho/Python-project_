from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import events as ev
import sql_commands as sqlc
import connect as con


def confirmar_dado(primary_key, window_a, name):
    conn = con.db_connect()
    cursor = conn.cursor()
    name_value = name.get()
    cursor.execute("SELECT * FROM games")
    resultados = cursor.fetchall()
    for resultado in resultados:
        if name_value == resultado[1]:
            tela_alterar_dados(primary_key, window_a, name_value)
            return
    else:
        messagebox.showinfo("Erro", "Parâmetro nulo na caixa nome. Parâmetro Inválido")


def tela_alterar_dados(primary_key, window_a, name):
    conn = con.db_connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM games WHERE jogo = '{name}'")
    data = cursor.fetchall()
    for dado in data:
        old_name = dado[1]
        tags = dado[2]
        plataform = dado[3]
        price = dado[4]
        developer = dado[5]
        release_date = dado[6]
    cursor.close()
    con.db_desconnect(conn)

    name_value = name
    window_a.destroy()
    window = Tk()
    window.title('Alterar dados')
    window.geometry(ev.center_low(window))
    window.resizable(False, False)
    frame = Frame(master=window, width='650', height='350')
    frame.pack()
    ev.bg_fun_low(frame)

    name_label = Label(text="Nome: ", fg="#FFFFFF", bg="#000000")
    name_label.place(x=25, y=61)
    name_entry = Entry(frame, width=35, fg="#000000")
    name_entry.insert(0, name_value)
    name_entry.place(x=72, y=61)

    tags_label = Label(text="Gêneros: ", fg="#FFFFFF", bg="#000000")
    tags_label.place(x=25, y=101)
    tags_entry = Entry(frame, width=35, fg="#000000")
    tags_entry.insert(0, tags)
    tags_entry.place(x=80, y=101)

    platform_label = Label(text="Plataforma: ", fg="#FFFFFF", bg="#000000")
    platform_label.place(x=25, y=141)
    platform_entry = Entry(frame, width=35, fg="#000000")
    platform_entry.insert(0, plataform)
    platform_entry.place(x=95, y=141)

    release_date_label = Label(text="Data de Lançamento: ", fg="#FFFFFF", bg="#000000")
    release_date_label.place(x=345, y=61)
    release_date_entry = Entry(frame, width=25, fg="#000000")
    release_date_entry.insert(0, release_date)
    release_date_entry.place(x=472, y=61)

    developer_label = Label(text="Desenvolvedora: ", fg="#FFFFFF", bg="#000000")
    developer_label.place(x=345, y=101)
    developer_entry = Entry(frame, width=30, fg="#000000")
    developer_entry.insert(0, developer)
    developer_entry.place(x=445, y=101)

    price_label = Label(text="Preço: ", fg="#FFFFFF", bg="#000000")
    price_label.place(x=345, y=141)
    price_entry = Entry(frame, width=38, fg="#000000")
    price_entry.insert(0, price)
    price_entry.place(x=395, y=141)

    button_alterar = Button(text="Alterar", bd=2, fg="#FFFFFF", bg="#121212", font=('inter', 10, 'bold'),
                            command=lambda: sqlc.alt_data(name_entry, old_name, tags_entry, platform_entry, price_entry,
                                                          developer_entry, release_date_entry, primary_key, window))
    button_alterar.place(x=250, y=284, width=150)

    window.mainloop()
