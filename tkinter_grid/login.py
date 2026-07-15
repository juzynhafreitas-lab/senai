import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("sistema de login")
janela.geometry("350x200")

def login():
    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "Juliana" and senha == "123":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "usuario ou senha invalidos!")

lbl_login = ttk.Label(janela, text="Login:")
lbl_login.grid(row=0, column=0, padx=10, pady=10)

edt_login = ttk.Entry(janela, width=25)
edt_login.grid(row=0, column=1, padx=10, pady=10)

lbl_senha = ttk.Label(janela, text="Senha:")
lbl_senha.grid(row=1, column=0, padx=10, pady=10)

edt_senha = ttk.Entry(janela, width=25, show="*")
edt_senha.grid(row=1, column=1, padx=10, pady=10)

btn_login = ttk.Button(janela, text="Entrar", command=login)
btn_login.grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()
