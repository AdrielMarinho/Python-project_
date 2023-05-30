import connect as con
import tela_principal as tc
import tela_login as tl
from tkinter import messagebox


def create_table():
    conn = con.db_connect()
    table1 = conn.cursor()
    table1.execute("""CREATE TABLE IF NOT EXISTS users (id_user INT PRIMARY KEY NOT NULL AUTO_INCREMENT, cpf VARCHAR(20)
                    NOT NULL, nome VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL, endereço VARCHAR(30) NOT NULL,
                    complemento VARCHAR(30) NOT NULL, telefone BIGINT NOT NULL, senha VARCHAR(15) NOT NULL);""")
    conn.commit()
    table1.close()
    con.db_desconnect(conn)


def add_games(game, tags, plataform, price, developer, release_date, primary_key, window):
    conn = con.db_connect()
    cursor = conn.cursor()
    game_value = game.get().title()
    tags_value = tags.get()
    plataform_value = plataform.get()
    price_value = price.get()
    developer_value = developer.get()
    release_date_value = release_date.get()

    cursor.execute("CREATE TABLE IF NOT EXISTS games (id_games INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
                   " jogo VARCHAR(100) NOT NULL, gêneros VARCHAR(100) NOT NULL, plataforma VARCHAR(80),"
                   "preço INT NOT NULL, desenvolvedora VARCHAR(30) NOT NULL, data_de_lançamento VARCHAR(30) NOT NULL,"
                   " id_user_tipo INT NOT NULL, FOREIGN KEY (id_user_tipo) REFERENCES users(id_user));")

    sql_stmt = ("INSERT INTO games (jogo, gêneros, plataforma, preço, desenvolvedora, data_de_lançamento, id_user_tipo)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s);")
    data = (game_value, tags_value, plataform_value, price_value, developer_value, release_date_value, primary_key)
    cursor.execute(sql_stmt, data)
    conn.commit()
    messagebox.showinfo("Sucesso", "Dados adicionados com sucesso.")
    window.destroy()
    tc.main_window(primary_key)


def table_login(email, senha, window):
    conn = con.db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    email_var = email.get()
    senha_var = senha.get()
    resultados = cursor.fetchall()
    for resultado in resultados:
        if resultado[3] == email_var and resultado[7] == senha_var:
            primary_key_id_user = resultado[0]
            window.destroy()
            tc.main_window(primary_key_id_user)
            con.db_desconnect(conn)
            return
    else:
        messagebox.showinfo("Erro", "Usuário ou Senha incorretos.")


def table_signup(cpf, nome, email, endereco, complemento, telefone, senha, confimar_senha, window):
    conn = con.db_connect()
    cursor = conn.cursor()
    name_value = nome.get().title().strip()
    cpf_value = cpf.get().strip()
    email_value = email.get().strip()
    endereco_value = endereco.get().title().strip()
    complemento_value = complemento.get().title().strip()
    telefone_value = int(telefone.get().strip())
    password_value = senha.get().strip()
    password_confirm_value = confimar_senha.get().strip()

    def password_verification():

        if len(password_value) <= 6:
            messagebox.showinfo("Erro de validação", "Senha deve ter mais do que 6 caracteres")
            return

        if password_value == password_confirm_value:
            sql_stmt = ("INSERT INTO users (cpf, nome, email, endereço, complemento, telefone, senha) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            data = (cpf_value, name_value, email_value, endereco_value, complemento_value, telefone_value,
                    password_value)
            cursor.execute(sql_stmt, data)
            conn.commit()
            messagebox.showinfo("Cadastro Realizado", "Cadastro realizado com sucesso.")
            window.destroy()
            tl.login_screen()
            con.db_desconnect(conn)
        else:
            messagebox.showinfo("Validação incorreta", "Senha e Confirmar senha são incompatíveis.")

    for letras in email_value:
        if letras == '@':
            password_verification()
            return
    else:
        messagebox.showinfo("Erro de validação", 'Email sem @.')
        return


def search_data(name):
    conn = con.db_connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM games WHERE name='{name}'")


def delete_data(name, primary_key):
    conn = con.db_connect()
    cursor = conn.cursor()
    name_value = name.get()
    sql_stmt = "DELETE FROM games WHERE jogo = %s AND id_user_tipo = %s"
    values = (name_value, primary_key)
    cursor.execute(sql_stmt, values)
    messagebox.showinfo("Excluir", "Dado excluído com sucesso")
    conn.commit()
    con.db_desconnect(conn)


def alt_data(name, old_name, tags, plataform, price, developer, release_date, primary_key, window):
    conn = con.db_connect()
    cursor = conn.cursor()
    old_name_value = old_name
    name_value = name.get().title()
    tags_value = tags.get()
    plataform_value = plataform.get()
    price_value = price.get()
    developer_value = developer.get()
    release_value = release_date.get()

    sql_stmt = ("UPDATE games SET jogo = %s, gêneros = %s, plataforma = %s, preço = %s, desenvolvedora = %s, data_de_lançamento = %s WHERE jogo = %s AND id_user_tipo = %s;")
    data = (name_value, tags_value, plataform_value, price_value, developer_value, release_value, old_name_value,
            primary_key)
    cursor.execute(sql_stmt, data)
    conn.commit()
    cursor.close()
    con.db_desconnect(conn)
    window.destroy()

    tc.main_window(primary_key)
