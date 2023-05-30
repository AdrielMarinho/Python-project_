from tkinter import ttk, Tk, Frame, Scrollbar, Label, Entry, Button
import events as ev
import tela_cadastro_jogos as tcj
import tela_alterar_jogos as taj
import connect as con
import sql_commands as sqlc


def main_window(primary_key):

    def list_all():
        conn = con.db_connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM games WHERE id_user_tipo = '{primary_key}'")
        data = cursor.fetchall()
        list_view.delete(*list_view.get_children())
        for dado in data:
            list_view.insert("", "end", values=(dado[0], dado[1], dado[2], dado[6]))
        cursor.close()
        con.db_desconnect(conn)

    def search_data():
        conn = con.db_connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM games WHERE id_user_tipo = '{primary_key}'")
        data = cursor.fetchall()
        for dado in data:
            if dado[1] == name_entry.get().title():
                list_view.delete(*list_view.get_children())
                list_view.insert("", "end", values=(dado[0], dado[1], dado[2], dado[6]))

        cursor.close()
        con.db_desconnect(conn)

    window = Tk()
    window.title('Main')
    window.geometry(ev.center(window))
    window.resizable(False, False)

    frame = Frame(master=window, width=750, height=450, bg='#000000')
    frame.pack()

    ev.bg_fun(frame)

    label_name = Label(frame, text="Nome: ", fg="#FFFFFF", bg="#000000", font=14)
    label_name.place(x=30, y=43)

    name_entry = Entry(frame, width=35, fg="#000000")
    name_entry.place(x=90, y=43)

    button_add = Button(text="Adicionar", bd=2, fg="#000000", bg="#FFFFFF", font=('inter', 10, 'bold'),
                        command=lambda: tcj.cadastro_jogos(primary_key, window))
    button_add.place(x=30, y=145, width=78, height=30)

    button_alt = Button(text="Alterar", bd=2, fg="#000000", bg="#FFFFFF", font=('inter', 10, 'bold'),
                        command=lambda: taj.confirmar_dado(primary_key, window, name_entry))
    button_alt.place(x=115, y=145, width=78, height=30)

    button_del = Button(text="Deletar", bd=2, fg="#000000", bg="#FFFFFF", font=('inter', 10, 'bold'),
                        command=lambda: [sqlc.delete_data(name_entry, primary_key), list_all()])
    button_del.place(x=200, y=145, width=78, height=30)

    button_search = Button(text="Buscar", bd=2, fg="#000000", bg="#FFFFFF", font=('inter', 10, 'bold'),
                           command=search_data)
    button_search.place(x=401, y=42, width=78, height=25)

    button_list = Button(text="Listar", bd=2, fg="#000000", bg="#FFFFFF", font=('inter', 10, 'bold'), command=list_all)
    button_list.place(x=318, y=42, width=78, height=25)

    list_view = ttk.Treeview(frame, height=220, columns=("col1", "col2", "col3", "col4"))
    list_view.heading("#0", text="")
    list_view.heading("#1", text="Id")
    list_view.heading("#2", text="Nome")
    list_view.heading("#3", text="Gêneros")
    list_view.heading("#4", text="Data de lançamento")

    list_view.column("#0", width=1)
    list_view.column("#1", width=25)
    list_view.column("#2", width=190)
    list_view.column("#3", width=190)
    list_view.column("#4", width=190)
    list_view.place(x=30, y=180, width=690, height=260)

    list_all()

    scroll_list = Scrollbar(frame, orient="vertical")
    list_view.configure(yscrollcommand=scroll_list.set)
    scroll_list.place(x=700, y=205, height=234)

    window.mainloop()
