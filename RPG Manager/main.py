import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import os
import basedados


# =========================================================
# CONFIGURAÇÕES
# =========================================================

FORMULARIO_LARGURA = 2 / 3
FORMULARIO_ALTURA = 2 / 3

MARGEM_X = 20
ESPACO_LABEL = 4
ESPACO_WIDGET = 18

FUNDO_APLICACAO = "#808080"
FUNDO_FORMULARIO = "#202020"
FUNDO_WIDGET = "#404040"

BRANCO = "#FFFFFF"
ROXO = "#8A2BE2"
AZUL = "#0808F5"
CINZENTO_TEXTO = "#AAAAAA"

# Espaçamentos
MARGEM_X = 20
ESPACO_LABEL = 4
ESPACO_WIDGET = 18

utilizador_atual_id = None
personagem_selecionada_id = None


# =========================================================
# Funções
# =========================================================

# ======================================================
# LOGOUT
# ======================================================

def fazer_logout():

    global utilizador_atual_id
    global personagem_selecionada_id

    resposta = messagebox.askyesno(
        "Logout",
        "Tem a certeza que pretende terminar a sessão?"
    )

    if not resposta:
        return

    # Limpar sessão
    utilizador_atual_id = None
    personagem_selecionada_id = None

    # Voltar ao login
    mostrar_login()


# ======================================================
# SAIR DA APLICAÇÃO
# ======================================================

def sair_aplicacao():

    resposta = messagebox.askyesno(
        "Sair",
        "Tem a certeza que pretende sair da aplicação?"
    )

    if not resposta:
        return

    janela.destroy()



# =========================================================
# JANELA
# =========================================================

janela = tk.Tk()

janela.title("RPG Manager")

# Janela maximizada
janela.state("zoomed")
basedados.Database()

# Fundo cinzento
janela.configure(
    bg=FUNDO_APLICACAO
)

# =========================================================
# LIMPAR JANELA
# =========================================================

def limpar_janela():
    """
    Remove todos os widgets atualmente existentes
    na janela.
    """

    for widget in janela.winfo_children():
        widget.destroy()

# =========================================================
# CRIAR FORMULÁRIO
# =========================================================

def criar_frame_principal():

    # =====================================================
    # FRAME EXTERIOR
    # =====================================================

    frame_exterior = tk.Frame(
        janela,
        bg=ROXO
    )

    frame_exterior.place(
        relx=0.5,
        rely=0.5,
        relwidth=FORMULARIO_LARGURA,
        relheight=FORMULARIO_ALTURA,
        anchor="center"
    )

    # =====================================================
    # FRAME INTERIOR
    # =====================================================

    frame_principal = tk.Frame(
        frame_exterior,
        bg=FUNDO_FORMULARIO
    )

    frame_principal.place(
        x=2,
        y=2,
        relwidth=1,
        relheight=1,
        width=-4,
        height=-4
    )

    # Permite que a coluna aumente
    frame_principal.columnconfigure(
        0,
        weight=1
    )

    return frame_principal


# =========================================================
# LOGIN
# =========================================================

def mostrar_login():

    limpar_janela()

    frame = criar_frame_principal()

    # ======================================================
    # ESTRUTURA PRINCIPAL
    # ======================================================

    frame.grid_rowconfigure(0, weight=0)   # topo
    frame.grid_rowconfigure(1, weight=1)   # conteúdo
    frame.grid_rowconfigure(2, weight=0)   # rodapé

    frame.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # TOPO
    # ======================================================

    frame_topo = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_topo.grid(
        row=0,
        column=0,
        sticky="ew"
    )

    frame_topo.grid_columnconfigure(
        0,
        weight=1
    )


    # ------------------------------------------------------
    # TÍTULO
    # ------------------------------------------------------

    label_titulo = tk.Label(
        frame_topo,
        text="RPG Manager",
        font=("Arial", 18, "bold"),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_titulo.grid(
        row=0,
        column=0,
        padx=20,
        pady=20,
        sticky="w"
    )


    # ------------------------------------------------------
    # BOTÃO SAIR
    # ------------------------------------------------------

    botao_sair = tk.Button(
        frame_topo,
        text="Sair",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=VERMELHO,
        activeforeground=BRANCO,
        activebackground=VERMELHO_ATIVO,
        relief="solid",
        bd=2,
        cursor="hand2",
        command=sair_aplicacao
    )

    botao_sair.grid(
        row=0,
        column=1,
        padx=20,
        pady=15
    )


    # ======================================================
    # ÁREA DE CONTEÚDO
    # ======================================================

    frame_conteudo = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_conteudo.grid(
        row=1,
        column=0,
        sticky="nsew"
    )

    frame_conteudo.grid_columnconfigure(
        0,
        weight=1
    )


    # ------------------------------------------------------
    # FRAME DOS CAMPOS
    # ------------------------------------------------------

    frame_formulario = tk.Frame(
        frame_conteudo,
        bg=FUNDO_FORMULARIO
    )

    frame_formulario.grid(
        row=0,
        column=0,
        padx=80,
        pady=40,
        sticky="ew"
    )

    frame_formulario.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # TÍTULO
    # ======================================================

    label_login = tk.Label(
        frame_formulario,
        text="Entrar na sua Conta",
        font=("Arial", 22, "bold"),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_login.grid(
        row=0,
        column=0,
        pady=(0, 35)
    )


    # ======================================================
    # EMAIL
    # ======================================================

    label_email = tk.Label(
        frame_formulario,
        text="Endereço de email",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_email.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_email = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_email.grid(
        row=2,
        column=0,
        sticky="ew",
        pady=(0, 25),
        ipady=8
    )


    # ======================================================
    # PASSWORD
    # ======================================================

    label_password = tk.Label(
        frame_formulario,
        text="Palavra-passe",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_password.grid(
        row=3,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_password = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        show="*",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_password.grid(
        row=4,
        column=0,
        sticky="ew",
        pady=(0, 25),
        ipady=8
    )


    # ======================================================
    # CHECKBOX
    # ======================================================

    frame_opcoes = tk.Frame(
        frame_formulario,
        bg=FUNDO_FORMULARIO
    )

    frame_opcoes.grid(
        row=5,
        column=0,
        sticky="w",
        pady=(0, 20)
    )

    lembrar_var = tk.BooleanVar()

    checkbox_lembrar = tk.Checkbutton(
        frame_opcoes,
        text="Lembrar sessão",
        variable=lembrar_var,
        font=("Arial", 10),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO,
        activebackground=FUNDO_FORMULARIO,
        activeforeground=BRANCO,
        selectcolor=FUNDO_WIDGET
    )

    checkbox_lembrar.pack()


    # ======================================================
    # ESPAÇO EXPANSÍVEL
    # ======================================================

    frame_conteudo.grid_rowconfigure(
        0,
        weight=1
    )


    # ======================================================
    # RODAPÉ
    # ======================================================

    frame_rodape = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_rodape.grid(
        row=2,
        column=0,
        sticky="ew"
    )

    frame_rodape.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # LINK
    # ======================================================

    link_registo = tk.Label(
        frame_rodape,
        text="Ainda não tem uma conta? Criar Conta",
        font=("Arial", 10, "underline"),
        bg=FUNDO_FORMULARIO,
        fg=AZUL,
        cursor="hand2"
    )

    link_registo.grid(
        row=0,
        column=0,
        pady=(0, 15)
    )

    link_registo.bind(
        "<Button-1>",
        lambda event: mostrar_registo()
    )


    # ======================================================
    # BOTÃO ENTRAR
    # ======================================================

    def fazer_login():

        email = entrada_email.get().strip()
        password = entrada_password.get()

        # ==========================
        # VALIDAR CAMPOS
        # ==========================

        if email == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza o endereço de email."
            )
            entrada_email.focus()
            return

        if password == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza a palavra-passe."
            )
            entrada_password.focus()
            return

        # ==========================
        # LIGAR À BASE DE DADOS
        # ==========================

        try:

            ligacao = sqlite3.connect("rpg.db")
            cursor = ligacao.cursor()

            # Procurar utilizador pelo email
            cursor.execute("""
                SELECT id, nome, email, password
                FROM Utilizadores
                WHERE email = ?
            """, (email,))

            utilizador = cursor.fetchone()

            ligacao.close()

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro",
                f"Erro ao aceder à base de dados:\n{erro}"
            )

            return

        # ==========================
        # UTILIZADOR NÃO ENCONTRADO
        # ==========================

        if utilizador is None:
            messagebox.showerror(
                "Login",
                "Email ou palavra-passe incorretos."
            )

            entrada_password.delete(0, tk.END)
            entrada_password.focus()

            return

        # ==========================
        # DADOS DO UTILIZADOR
        # ==========================

        utilizador_id = utilizador[0]
        nome = utilizador[1]
        email_bd = utilizador[2]
        password_guardada = utilizador[3]

        # ==========================
        # VERIFICAR PASSWORD
        # ==========================

        if not basedados.Seguranca.verificar_password(
                password,
                password_guardada
        ):
            messagebox.showerror(
                "Login",
                "Email ou palavra-passe incorretos."
            )

            entrada_password.delete(0, tk.END)
            entrada_password.focus()



            return

        # ==========================
        # LOGIN BEM-SUCEDIDO
        # ==========================

        messagebox.showinfo(
            "Login",
            f"Login efetuado com sucesso!\n\n"
            f"Bem-vindo, {nome}!"
        )

        global utilizador_atual_id

        utilizador_atual_id = utilizador_id

        mostrar_personagens()

    botao_entrar = tk.Button(
        frame_rodape,
        text="Entrar",
        font=("Arial", 11, "bold"),
        fg=BRANCO,
        bg=AZUL,
        activebackground=AZUL_ATIVO,
        activeforeground=BRANCO,
        relief="solid",
        bd=2,
        cursor="hand2",
        command=fazer_login
    )

    botao_entrar.grid(
        row=1,
        column=0,
        padx=40,
        pady=(0, 20),
        sticky="ew",
        ipady=8
    )


    # ======================================================
    # FOOTER
    # ======================================================

    label_footer = tk.Label(
        frame_rodape,
        text="RPG Manager © 2026",
        font=("Arial", 9),
        bg=FUNDO_FORMULARIO,
        fg=CINZENTO_TEXTO
    )

    label_footer.grid(
        row=2,
        column=0,
        pady=(0, 10)
    )


    entrada_email.focus()


# =========================================================
# REGISTO
# =========================================================

# ======================================================
# REGISTO
# ======================================================

def mostrar_registo():

    limpar_janela()

    frame = criar_frame_principal()

    # ======================================================
    # ESTRUTURA PRINCIPAL
    # ======================================================

    frame.grid_rowconfigure(0, weight=0)   # topo
    frame.grid_rowconfigure(1, weight=1)   # conteúdo
    frame.grid_rowconfigure(2, weight=0)   # rodapé

    frame.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # BARRA SUPERIOR
    # ======================================================

    frame_topo = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_topo.grid(
        row=0,
        column=0,
        sticky="ew"
    )

    frame_topo.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # TÍTULO SUPERIOR
    # ======================================================

    label_titulo = tk.Label(
        frame_topo,
        text="RPG Manager",
        font=("Arial", 18, "bold"),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_titulo.grid(
        row=0,
        column=0,
        padx=20,
        pady=20,
        sticky="w"
    )


    # ======================================================
    # BOTÃO SAIR
    # ======================================================

    botao_sair = tk.Button(
        frame_topo,
        text="Sair",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=VERMELHO,
        activeforeground=BRANCO,
        activebackground=VERMELHO_ATIVO,
        relief="solid",
        bd=2,
        cursor="hand2",
        command=sair_aplicacao
    )

    botao_sair.grid(
        row=0,
        column=1,
        padx=20,
        pady=15
    )


    # ======================================================
    # ÁREA DE CONTEÚDO
    # ======================================================

    frame_conteudo = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_conteudo.grid(
        row=1,
        column=0,
        sticky="nsew"
    )

    frame_conteudo.grid_columnconfigure(
        0,
        weight=1
    )

    frame_conteudo.grid_rowconfigure(
        0,
        weight=1
    )


    # ======================================================
    # FORMULÁRIO
    # ======================================================

    frame_formulario = tk.Frame(
        frame_conteudo,
        bg=FUNDO_FORMULARIO
    )

    frame_formulario.grid(
        row=0,
        column=0,
        padx=80,
        pady=40,
        sticky="ew"
    )

    frame_formulario.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # TÍTULO
    # ======================================================

    label_registo = tk.Label(
        frame_formulario,
        text="Criar Conta",
        font=("Arial", 22, "bold"),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_registo.grid(
        row=0,
        column=0,
        pady=(0, 30)
    )


    # ======================================================
    # NOME
    # ======================================================

    label_nome = tk.Label(
        frame_formulario,
        text="Nome de Utilizador",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_nome.grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_nome = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_nome.grid(
        row=2,
        column=0,
        sticky="ew",
        ipady=8,
        pady=(0, 20)
    )


    # ======================================================
    # EMAIL
    # ======================================================

    label_email = tk.Label(
        frame_formulario,
        text="Endereço de email",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_email.grid(
        row=3,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_email = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_email.grid(
        row=4,
        column=0,
        sticky="ew",
        ipady=8,
        pady=(0, 20)
    )


    # ======================================================
    # PASSWORD
    # ======================================================

    label_password = tk.Label(
        frame_formulario,
        text="Palavra-passe",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_password.grid(
        row=5,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_password = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        show="*",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_password.grid(
        row=6,
        column=0,
        sticky="ew",
        ipady=8,
        pady=(0, 20)
    )


    # ======================================================
    # CONFIRMAR PASSWORD
    # ======================================================

    label_confirmar_password = tk.Label(
        frame_formulario,
        text="Confirmar palavra-passe",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_confirmar_password.grid(
        row=7,
        column=0,
        sticky="w",
        pady=(0, 6)
    )


    entrada_confirmar_password = tk.Entry(
        frame_formulario,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        insertbackground=BRANCO,
        show="*",
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#555555",
        highlightcolor=ROXO
    )

    entrada_confirmar_password.grid(
        row=8,
        column=0,
        sticky="ew",
        ipady=8,
        pady=(0, 10)
    )


    # ======================================================
    # RODAPÉ
    # ======================================================

    frame_rodape = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO
    )

    frame_rodape.grid(
        row=2,
        column=0,
        sticky="ew"
    )

    frame_rodape.grid_columnconfigure(
        0,
        weight=1
    )


    # ======================================================
    # LINK PARA LOGIN
    # ======================================================

    link_login = tk.Label(
        frame_rodape,
        text="Já tem uma conta? Entrar",
        font=("Arial", 10, "underline"),
        bg=FUNDO_FORMULARIO,
        fg=AZUL,
        cursor="hand2"
    )

    link_login.grid(
        row=0,
        column=0,
        pady=(0, 15)
    )

    link_login.bind(
        "<Button-1>",
        lambda event: mostrar_login()
    )


    # ======================================================
    # BOTÃO REGISTAR
    # ======================================================

    def fazer_registo():

        nome = entrada_nome.get().strip()
        email = entrada_email.get().strip()
        password = entrada_password.get()
        confirmar_password = entrada_confirmar_password.get()


        # ==============================================
        # VALIDAR NOME
        # ==============================================

        if nome == "":

            messagebox.showwarning(
                "Atenção",
                "Introduza o nome de utilizador."
            )

            entrada_nome.focus()

            return


        # ==============================================
        # VALIDAR EMAIL
        # ==============================================

        if email == "":

            messagebox.showwarning(
                "Atenção",
                "Introduza o endereço de email."
            )

            entrada_email.focus()

            return


        if "@" not in email:

            messagebox.showwarning(
                "Atenção",
                "Introduza um endereço de email válido."
            )

            entrada_email.focus()

            return


        # ==============================================
        # VALIDAR PASSWORD
        # ==============================================

        if password == "":

            messagebox.showwarning(
                "Atenção",
                "Introduza uma palavra-passe."
            )

            entrada_password.focus()

            return


        if len(password) < 6:

            messagebox.showwarning(
                "Atenção",
                "A palavra-passe deve ter pelo menos 6 caracteres."
            )

            entrada_password.focus()

            return


        # ==============================================
        # CONFIRMAR PASSWORD
        # ==============================================

        if confirmar_password == "":

            messagebox.showwarning(
                "Atenção",
                "Confirme a palavra-passe."
            )

            entrada_confirmar_password.focus()

            return


        if password != confirmar_password:

            messagebox.showwarning(
                "Atenção",
                "As palavras-passe não coincidem."
            )

            entrada_confirmar_password.focus()

            return


        # ==============================================
        # VERIFICAR SE EMAIL JÁ EXISTE
        # ==============================================

        ligacao = None

        try:

            ligacao = sqlite3.connect("rpg.db")

            cursor = ligacao.cursor()

            cursor.execute("""
                SELECT id
                FROM Utilizadores
                WHERE email = ?
            """, (email,))

            utilizador_existente = cursor.fetchone()

            if utilizador_existente is not None:

                ligacao.close()
                ligacao = None

                messagebox.showwarning(
                    "Atenção",
                    "Já existe uma conta com este endereço de email."
                )

                entrada_email.focus()

                return


            # ==========================================
            # CRIAR HASH DA PASSWORD
            # ==========================================

            password_hash = basedados.Seguranca.criar_hash(
                password
            )


            # ==========================================
            # INSERIR UTILIZADOR
            # ==========================================

            cursor.execute("""
                INSERT INTO Utilizadores (
                    nome,
                    email,
                    password
                )
                VALUES (?, ?, ?)
            """, (
                nome,
                email,
                password_hash
            ))

            ligacao.commit()

            ligacao.close()
            ligacao = None

        except sqlite3.Error as erro:

            if ligacao is not None:

                ligacao.rollback()
                ligacao.close()

            messagebox.showerror(
                "Erro",
                f"Não foi possível criar a conta:\n\n{erro}"
            )

            return


        # ==============================================
        # REGISTO CONCLUÍDO
        # ==============================================

        messagebox.showinfo(
            "Conta criada",
            "A conta foi criada com sucesso!\n\n"
            "Agora pode iniciar sessão."
        )

        mostrar_login()


    botao_registar = tk.Button(
        frame_rodape,
        text="Registar-se",
        font=("Arial", 11, "bold"),
        fg=BRANCO,
        bg=VERDE,
        activeforeground=BRANCO,
        activebackground=VERDE_ATIVO,
        relief="solid",
        bd=2,
        cursor="hand2",
        command=fazer_registo
    )

    botao_registar.grid(
        row=1,
        column=0,
        padx=40,
        pady=(0, 20),
        sticky="ew",
        ipady=8
    )


    # ======================================================
    # FOOTER
    # ======================================================

    label_footer = tk.Label(
        frame_rodape,
        text="RPG Manager © 2026",
        font=("Arial", 9),
        bg=FUNDO_FORMULARIO,
        fg=CINZENTO_TEXTO
    )

    label_footer.grid(
        row=2,
        column=0,
        pady=(0, 10)
    )


    # ======================================================
    # FOCUS
    # ======================================================

    entrada_nome.focus()



# ==========================================================
# CRIAR Janela de Gestão de Personagens
# ==========================================================



# ==========================================================
# CORES
# ==========================================================

FUNDO_APLICACAO = "#151515"
FUNDO_FORMULARIO = "#202020"
FUNDO_WIDGET = "#303030"

BRANCO = "#FFFFFF"
ROXO = "#8A2BE2"
AZUL = "#0808F5"
CINZENTO_TEXTO = "#AAAAAA"

PRETO = "#000000"
BRANCO_WIDGET = "#303030"

# ==========================================================
# CORES DOS BOTÕES
# ==========================================================

VERDE = "#28A745"
VERDE_HOVER = "#34C759"
VERDE_ATIVO = "#1E7E34"

AMARELO = "#FFC107"
AMARELO_HOVER = "#FFD54F"
AMARELO_ATIVO = "#C79100"

AZUL_BOTAO = "#007BFF"
AZUL_HOVER = "#3399FF"
AZUL_ATIVO = "#0056B3"

VERMELHO = "#DC3545"
VERMELHO_HOVER = "#FF4D5A"
VERMELHO_ATIVO = "#A71D2A"

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

FORMULARIO_LARGURA = 0.90
FORMULARIO_ALTURA = 0.90

MARGEM_X = 20
MARGEM_Y = 10

# ==========================================================
# CRIAR ÁREA PRINCIPAL
# ==========================================================

def criar_frame_principal():

    frame_exterior = tk.Frame(
        janela,
        bg=PRETO
    )

    frame_exterior.place(
        relx=0.5,
        rely=0.5,
        relwidth=FORMULARIO_LARGURA,
        relheight=FORMULARIO_ALTURA,
        anchor="center"
    )

    # ------------------------------------------------------
    # Frame interior
    # ------------------------------------------------------

    frame = tk.Frame(
        frame_exterior,
        bg=FUNDO_FORMULARIO
    )

    frame.place(
        x=3,
        y=3,
        relwidth=1,
        relheight=1,
        width=-6,
        height=-6
    )

    return frame







# ==========================================================
# GESTÃO DE PERSONAGENS
# ==========================================================








def mostrar_personagens():

    limpar_janela()

    frame = criar_frame_principal()

    # ======================================================
    # ESTRUTURA PRINCIPAL
    # ======================================================

    frame.grid_rowconfigure(0, weight=0)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=0)

    frame.grid_columnconfigure(0, weight=0)
    frame.grid_columnconfigure(1, weight=1)

    # ======================================================
    # BARRA SUPERIOR
    # ======================================================

    frame_topo = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO,
        height=60
    )

    frame_topo.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew"
    )

    frame_topo.grid_columnconfigure(
        0,
        weight=1
    )

    # ======================================================
    # Barra Superior - Título
    # ======================================================

    label_titulo = tk.Label(
        frame_topo,
        text="Gestão de Personagens",
        font=("Arial", 18, "bold"),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_titulo.grid(
        row=0,
        column=0,
        padx=20,
        pady=10,
        sticky="w"
    )

    # ======================================================
    # Barra Superior - Botão Logout
    # ======================================================

    botao_logout = tk.Button(
        frame_topo,
        text="Logout",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=ROXO,
        activeforeground=BRANCO,
        activebackground="#6419A8",
        relief="solid",
        bd=2,
        cursor="hand2",
        command=fazer_logout
    )

    botao_logout.grid(
        row=0,
        column=1,
        padx=(10, 5),
        pady=10
    )


    # ======================================================
    # Barra Superior - Botão Sair
    # ======================================================

    botao_sair = tk.Button(
        frame_topo,
        text="Sair",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=VERMELHO,
        activeforeground=BRANCO,
        activebackground=VERMELHO_ATIVO,
        relief="solid",
        bd=2,
        cursor="hand2",
        command=sair_aplicacao
    )

    botao_sair.grid(
        row=0,
        column=2,
        padx=(5, 20),
        pady=10
    )

    # ======================================================
    # LADO ESQUERDO - LISTA DE PERSONAGENS
    # ======================================================

    frame_lista = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO,
        bd=2,
        relief="solid"
    )

    frame_lista.grid(
        row=1,
        column=0,
        rowspan=2,
        sticky="nsew"
    )

    # ======================================================
    # TÍTULO
    # ======================================================

    label_lista = tk.Label(
        frame_lista,
        text="Lista de Personagens",
        font=("Arial", 12),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_lista.pack(
        pady=40
    )

    # ======================================================
    # LISTBOX
    # ======================================================

    lista_personagens = tk.Listbox(
        frame_lista,
        font=("Arial", 11),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        bd=1,
        relief="solid",
        highlightthickness=0,
        selectbackground=ROXO,
        selectforeground=BRANCO
    )

    lista_personagens.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    # ======================================================
    # CARREGAR PERSONAGENS
    # ======================================================

    def carregar_personagens():

        lista_personagens.delete(
            0,
            tk.END
        )

        try:

            ligacao = sqlite3.connect("rpg.db")
            cursor = ligacao.cursor()

            cursor.execute("""
                SELECT id, nome
                FROM Personagens
                WHERE utilizador_id = ?
                ORDER BY id
            """, (utilizador_atual_id,))

            personagens = cursor.fetchall()

            ligacao.close()

            for personagem in personagens:
                personagem_id = personagem[0]
                nome = personagem[1]

                lista_personagens.insert(
                    tk.END,
                    f"{personagem_id} - {nome}"
                )

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar as personagens:\n{erro}"
            )

    carregar_personagens()

    def selecionar_personagem(event=None):

        global personagem_selecionada_id

        selecao = lista_personagens.curselection()

        # Nenhuma personagem selecionada
        if not selecao:
            return

        # Obter o texto selecionado
        texto = lista_personagens.get(selecao[0])

        # Exemplo:
        # "4 - Aragorn"

        try:
            personagem_id = int(
                texto.split(" - ")[0]
            )
        except (ValueError, IndexError):
            return

        personagem_selecionada_id = personagem_id

        # ======================================================
        # PESQUISAR NA BASE DE DADOS
        # ======================================================

        try:

            ligacao = sqlite3.connect("rpg.db")
            cursor = ligacao.cursor()

            cursor.execute("""
                SELECT
                    id,
                    nome,
                    vida,
                    mana,
                    forca,
                    agilidade,
                    constituicao,
                    inteligencia,
                    sabedoria,
                    carisma,
                    descricao,
                    habilidade

                FROM Personagens

                WHERE id = ?
                AND utilizador_id = ?
            """, (
                personagem_id,
                utilizador_atual_id
            ))

            personagem = cursor.fetchone()

            ligacao.close()

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar a personagem:\n{erro}"
            )

            return

        # ======================================================
        # PERSONAGEM NÃO ENCONTRADA
        # ======================================================

        if personagem is None:
            messagebox.showerror(
                "Erro",
                "Não foi possível encontrar a personagem."
            )

            return

        # ======================================================
        # PREENCHER OS CAMPOS
        # ======================================================

        entrada_nome.delete(
            0,
            tk.END
        )

        entrada_nome.insert(
            0,
            personagem[1]
        )

        entrada_vida.delete(
            0,
            tk.END
        )

        entrada_vida.insert(
            0,
            personagem[2]
        )

        entrada_mana.delete(
            0,
            tk.END
        )

        entrada_mana.insert(
            0,
            personagem[3]
        )

        entrada_forca.delete(
            0,
            tk.END
        )

        entrada_forca.insert(
            0,
            personagem[4]
        )

        entrada_agilidade.delete(
            0,
            tk.END
        )

        entrada_agilidade.insert(
            0,
            personagem[5]
        )

        entrada_constituicao.delete(
            0,
            tk.END
        )

        entrada_constituicao.insert(
            0,
            personagem[6]
        )

        entrada_inteligencia.delete(
            0,
            tk.END
        )

        entrada_inteligencia.insert(
            0,
            personagem[7]
        )

        entrada_sabedoria.delete(
            0,
            tk.END
        )

        entrada_sabedoria.insert(
            0,
            personagem[8]
        )

        entrada_carisma.delete(
            0,
            tk.END
        )

        entrada_carisma.insert(
            0,
            personagem[9]
        )

        texto_descricao.delete(
            "1.0",
            tk.END
        )

        if personagem[10] is not None:
            texto_descricao.insert(
                "1.0",
                personagem[10]
            )

        texto_habilidade.delete(
            "1.0",
            tk.END
        )

        if personagem[11] is not None:
            texto_habilidade.insert(
                "1.0",
                personagem[11]
            )

    lista_personagens.bind(
        "<<ListboxSelect>>",
        selecionar_personagem
    )


    # ======================================================
    # ÁREA DIREITA
    # ======================================================

    frame_direita = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO,
    )

    frame_direita.grid(
        row=1,
        column=1,
        sticky="nsew"
    )

    frame_direita.grid_columnconfigure(
        0,
        weight=1
    )

    frame_direita.grid_columnconfigure(
        1,
        weight=1
    )


    # ======================================================
    # NOME DO PERSONAGEM
    # ======================================================

    label_nome = tk.Label(
        frame_direita,
        text="Nome do Personagem",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_nome.grid(
        row=0,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(30, 5)
    )


    entrada_nome = tk.Entry(
        frame_direita,
        font=("Arial", 12),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        relief="flat",
        bd=0,
        highlightthickness=2,
        highlightbackground="#CCCCCC",
        highlightcolor=ROXO
    )

    entrada_nome.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 15)
    )

    # ======================================================
    # PONTOS DE VIDA E DE MANA
    # ======================================================

    label_vida_mana = tk.Label(
        frame_direita,
        text="Pontos de Vida e de Mana",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_vida_mana.grid(
        row=2,
        column=0,
        pady=(0, 5)
    )

    # ======================================================
    # FRAME PARA VIDA E MANA
    # ======================================================

    frame_vida_mana = tk.Frame(
        frame_direita,
        bg=FUNDO_FORMULARIO
    )

    frame_vida_mana.grid(
        row=3,
        column=0,
        sticky="n",
        padx=MARGEM_X,
        pady=(0, 15)
    )

    # Não deixar as colunas expandirem
    frame_vida_mana.grid_columnconfigure(
        0,
        weight=0
    )

    frame_vida_mana.grid_columnconfigure(
        1,
        weight=0
    )

    frame_vida_mana.grid_columnconfigure(
        2,
        weight=0
    )

    # ======================================================
    # VIDA
    # ======================================================

    entrada_vida = tk.Entry(
        frame_vida_mana,
        font=("Arial", 10),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        relief="solid",
        bd=1,
        width=8,
        highlightthickness = 2,
        highlightbackground = "#CCCCCC",
        highlightcolor = ROXO
    )

    entrada_vida.grid(
        row=0,
        column=0,
    )

    # ======================================================
    # ESPAÇO
    # ======================================================

    espaco_vida_mana = tk.Frame(
        frame_vida_mana,
        bg=FUNDO_FORMULARIO,
        width=30
    )

    espaco_vida_mana.grid(
        row=0,
        column=1,
    )

    # ======================================================
    # MANA
    # ======================================================

    entrada_mana = tk.Entry(
        frame_vida_mana,
        font=("Arial", 10),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        relief="solid",
        bd=1,
        width=8,
        highlightthickness = 2,
        highlightbackground = "#CCCCCC",
        highlightcolor = ROXO
    )

    entrada_mana.grid(
        row=0,
        column=2
    )


    # ======================================================
    # ÍNDICES FÍSICOS E MENTAIS
    # ======================================================

    label_indices = tk.Label(
        frame_direita,
        text="Índices Físicos e Mentais",
        font=("Arial", 16),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_indices.grid(
        row=4,
        column=0,
        columnspan=2,
        sticky="w",
        padx=MARGEM_X,
        pady=(25, 10)
    )


    # ======================================================
    # INDICES
    # ======================================================

    frame_stats = tk.Frame(
        frame_direita,
        bg=FUNDO_FORMULARIO
    )

    frame_stats.grid(
        row=5,
        column=0,
        sticky="nsew",
        padx=MARGEM_X
    )

    frame_stats.grid_columnconfigure(0, weight=1)
    frame_stats.grid_columnconfigure(1, weight=1)
    frame_stats.grid_columnconfigure(2, weight=1)


    # ------------------------------------------------------
    # FUNÇÃO PARA CRIAR STAT
    # ------------------------------------------------------

    def criar_stat(nome, linha, coluna):

        frame_stat = tk.Frame(
            frame_stats,
            bg=FUNDO_FORMULARIO
        )

        frame_stat.grid(
            row=linha,
            column=coluna,
            padx=5,
            pady=5,
            sticky="ew"
        )

        label = tk.Label(
            frame_stat,
            text=nome,
            font=("Arial", 9),
            bg=FUNDO_FORMULARIO,
            fg=BRANCO
        )

        label.pack(
            anchor="w"
        )

        entrada = tk.Entry(
            frame_stat,
            font=("Arial", 10),
            bg=FUNDO_WIDGET,
            fg=BRANCO,
            relief="flat",
            bd=0,
            highlightthickness = 2,
            highlightbackground = "#CCCCCC",
            highlightcolor = ROXO
        )

        entrada.pack(
            fill="x"
        )

        return entrada


    # ------------------------------------------------------
    # PRIMEIRA LINHA
    # ------------------------------------------------------

    entrada_forca = criar_stat(
        "Força",
        0,
        0
    )

    entrada_agilidade = criar_stat(
        "Agilidade",
        0,
        1
    )

    entrada_constituicao = criar_stat(
        "Constituição",
        0,
        2
    )


    # ------------------------------------------------------
    # SEGUNDA LINHA
    # ------------------------------------------------------

    entrada_inteligencia = criar_stat(
        "Inteligência",
        1,
        0
    )

    entrada_sabedoria = criar_stat(
        "Sabedoria",
        1,
        1
    )

    entrada_carisma = criar_stat(
        "Carisma",
        1,
        2
    )


    # ======================================================
    # DESCRIÇÃO
    # ======================================================

    label_descricao = tk.Label(
        frame_direita,
        text="Descrição do personagem",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_descricao.grid(
        row=0,
        column=1,
        pady=(30, 5)
    )


    texto_descricao = tk.Text(
        frame_direita,
        font=("Arial", 11),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        relief="flat",
        bd=0,
        height=4,
        highlightthickness=2,
        highlightbackground="#CCCCCC",
        highlightcolor=ROXO
    )

    texto_descricao.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=(10, MARGEM_X),
        pady=(0, 15)
    )


    # ======================================================
    # HABILIDADE
    # ======================================================

    label_habilidade = tk.Label(
        frame_direita,
        text="Habilidade do Personagem",
        font=("Arial", 11),
        bg=FUNDO_FORMULARIO,
        fg=BRANCO
    )

    label_habilidade.grid(
        row=2,
        column=1,
        pady=(0, 5)
    )


    texto_habilidade = tk.Text(
        frame_direita,
        font=("Arial", 11),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        relief="flat",
        bd=0,
        height=4,
        highlightthickness=2,
        highlightbackground="#CCCCCC",
        highlightcolor=ROXO
    )

    texto_habilidade.grid(
        row=3,
        column=1,
        sticky="ew",
        padx=(10, MARGEM_X),
        pady=(0, 15)
    )


    # ======================================================
    # PARTE INFERIOR
    # ======================================================

    frame_botoes = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO,
        bd=2,
        relief="solid"
    )

    frame_botoes.grid(
        row=2,
        column=1,
        sticky="ew"
    )

    frame_botoes.grid_columnconfigure(
        0,
        weight=1
    )

    frame_botoes.grid_columnconfigure(
        1,
        weight=1
    )

    def criar_botao(
            parent,
            texto,
            comando,
            cor,
            cor_hover,
            cor_ativo
    ):

        botao = tk.Button(
            parent,
            text=texto,
            font=("Arial", 10, "bold"),
            fg=BRANCO,
            bg=cor,
            activeforeground=BRANCO,
            activebackground=cor_ativo,
            relief="solid",
            bd=2,
            highlightthickness=0,
            cursor="hand2",
            command=comando
        )

        # ------------------------------------------------------
        # Passar o rato por cima
        # ------------------------------------------------------

        def mouse_entrou(event):
            botao.config(
                bg=cor_hover
            )

        def mouse_saiu(event):
            botao.config(
                bg=cor
            )

        botao.bind(
            "<Enter>",
            mouse_entrou
        )

        botao.bind(
            "<Leave>",
            mouse_saiu
        )

        return botao



    # ======================================================
    # BOTÃO ADICIONAR
    # ======================================================



    # ======================================================
    # ADICIONAR PERSONAGEM
    # ======================================================

    def adicionar_personagem():

        global personagem_selecionada_id

        # ==================================================
        # OBTER DADOS DOS CAMPOS
        # ==================================================

        nome = entrada_nome.get().strip()
        vida = entrada_vida.get().strip()
        mana = entrada_mana.get().strip()

        forca = entrada_forca.get().strip()
        agilidade = entrada_agilidade.get().strip()
        constituicao = entrada_constituicao.get().strip()

        inteligencia = entrada_inteligencia.get().strip()
        sabedoria = entrada_sabedoria.get().strip()
        carisma = entrada_carisma.get().strip()

        descricao = texto_descricao.get(
            "1.0",
            tk.END
        ).strip()

        habilidade = texto_habilidade.get(
            "1.0",
            tk.END
        ).strip()

        # ==================================================
        # VERIFICAR UTILIZADOR
        # ==================================================

        if utilizador_atual_id is None:
            messagebox.showerror(
                "Erro",
                "Não existe nenhum utilizador autenticado."
            )

            return

        # ==================================================
        # VALIDAR NOME
        # ==================================================

        if nome == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza o nome da personagem."
            )

            entrada_nome.focus()

            return

        # ==================================================
        # VALIDAR VALORES NUMÉRICOS
        # ==================================================

        campos_numericos = {
            "Vida": vida,
            "Mana": mana,
            "Força": forca,
            "Agilidade": agilidade,
            "Constituição": constituicao,
            "Inteligência": inteligencia,
            "Sabedoria": sabedoria,
            "Carisma": carisma
        }

        valores = {}

        for nome_campo, valor in campos_numericos.items():

            if valor == "":
                valor = "0"

            try:

                valor = int(valor)

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    f"O campo '{nome_campo}' deve conter um número inteiro."
                )

                return

            if valor < 0:
                messagebox.showwarning(
                    "Atenção",
                    f"O campo '{nome_campo}' não pode ser negativo."
                )

                return

            valores[nome_campo] = valor

        # ==================================================
        # CONFIRMAR ADIÇÃO
        # ==================================================

        resposta = messagebox.askyesno(
            "Adicionar Personagem",
            f"Tem a certeza que pretende adicionar a personagem "
            f"'{nome}'?"
        )

        if not resposta:
            return

        # ==================================================
        # INSERIR NA BASE DE DADOS
        # ==================================================

        ligacao = None

        try:

            ligacao = sqlite3.connect("rpg.db")

            cursor = ligacao.cursor()

            cursor.execute("""
                INSERT INTO Personagens (
                    utilizador_id,
                    nome,
                    vida,
                    mana,
                    forca,
                    agilidade,
                    constituicao,
                    inteligencia,
                    sabedoria,
                    carisma,
                    descricao,
                    habilidade
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                utilizador_atual_id,
                nome,
                valores["Vida"],
                valores["Mana"],
                valores["Força"],
                valores["Agilidade"],
                valores["Constituição"],
                valores["Inteligência"],
                valores["Sabedoria"],
                valores["Carisma"],
                descricao,
                habilidade
            ))

            # Guardar alterações
            ligacao.commit()

            # Obter o ID atribuído automaticamente
            personagem_selecionada_id = cursor.lastrowid

            ligacao.close()
            ligacao = None

        except sqlite3.Error as erro:

            if ligacao is not None:
                ligacao.rollback()
                ligacao.close()

            messagebox.showerror(
                "Erro",
                f"Não foi possível adicionar a personagem:\n\n{erro}"
            )

            return

        # ==================================================
        # ATUALIZAR LISTBOX
        # ==================================================

        carregar_personagens()

        # ==================================================
        # LIMPAR CAMPOS
        # ==================================================

        limpar_campos()

        # ==================================================
        # MOSTRAR RESULTADO
        # ==================================================

        messagebox.showinfo(
            "Personagem",
            f"Personagem '{nome}' adicionada com sucesso!"
        )

    botao_adicionar = criar_botao(
        frame_botoes,
        "Adicionar",
        adicionar_personagem,
        VERDE,
        VERDE_HOVER,
        VERDE_ATIVO
    )

    botao_adicionar.grid(
        row=0,
        column=0,
        padx=80,
        pady=(15, 5),
        sticky="ew"
    )




    # ======================================================
    # BOTÃO LIMPAR
    # ======================================================



    def limpar_campos():

        entrada_nome.delete(
            0,
            tk.END
        )

        entrada_vida.delete(
            0,
            tk.END
        )

        entrada_mana.delete(
            0,
            tk.END
        )

        for entrada in (
            entrada_forca,
            entrada_agilidade,
            entrada_constituicao,
            entrada_inteligencia,
            entrada_sabedoria,
            entrada_carisma
        ):

            entrada.delete(
                0,
                tk.END
            )

        texto_descricao.delete(
            "1.0",
            tk.END
        )

        texto_habilidade.delete(
            "1.0",
            tk.END
        )

        global personagem_selecionada_id

        personagem_selecionada_id = None

    botao_limpar = criar_botao(
        frame_botoes,
        "Limpar",
        limpar_campos,
        AZUL_BOTAO,
        AZUL_HOVER,
        AZUL_ATIVO
    )

    botao_limpar.grid(
        row=0,
        column=1,
        padx=80,
        pady=(15, 5),
        sticky="ew"
    )




    # ======================================================
    # BOTÃO ALTERAR
    # ======================================================



    # ======================================================
    # ALTERAR PERSONAGEM
    # ======================================================

    def alterar_personagem():

        global personagem_selecionada_id

        # ==================================================
        # VERIFICAR SE EXISTE PERSONAGEM SELECIONADA
        # ==================================================

        if personagem_selecionada_id is None:
            messagebox.showwarning(
                "Atenção",
                "Selecione primeiro uma personagem na lista."
            )

            return

        # ==================================================
        # OBTER DADOS DOS CAMPOS
        # ==================================================

        nome = entrada_nome.get().strip()
        vida = entrada_vida.get().strip()
        mana = entrada_mana.get().strip()

        forca = entrada_forca.get().strip()
        agilidade = entrada_agilidade.get().strip()
        constituicao = entrada_constituicao.get().strip()

        inteligencia = entrada_inteligencia.get().strip()
        sabedoria = entrada_sabedoria.get().strip()
        carisma = entrada_carisma.get().strip()

        descricao = texto_descricao.get(
            "1.0",
            tk.END
        ).strip()

        habilidade = texto_habilidade.get(
            "1.0",
            tk.END
        ).strip()

        # ==================================================
        # VALIDAR NOME
        # ==================================================

        if nome == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza o nome da personagem."
            )

            entrada_nome.focus()

            return

        # ==================================================
        # VALIDAR VALORES NUMÉRICOS
        # ==================================================

        campos_numericos = {
            "Vida": vida,
            "Mana": mana,
            "Força": forca,
            "Agilidade": agilidade,
            "Constituição": constituicao,
            "Inteligência": inteligencia,
            "Sabedoria": sabedoria,
            "Carisma": carisma
        }

        valores = {}

        for nome_campo, valor in campos_numericos.items():

            if valor == "":
                valor = "0"

            try:

                valor = int(valor)

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    f"O campo '{nome_campo}' deve conter um número inteiro."
                )

                return

            if valor < 0:
                messagebox.showwarning(
                    "Atenção",
                    f"O campo '{nome_campo}' não pode ser negativo."
                )

                return

            valores[nome_campo] = valor

        # ==================================================
        # CONFIRMAR ALTERAÇÃO
        # ==================================================

        resposta = messagebox.askyesno(
            "Alterar Personagem",
            f"Tem a certeza que pretende guardar as alterações "
            f"da personagem '{nome}'?"
        )

        if not resposta:
            return

        # ==================================================
        # ATUALIZAR BASE DE DADOS
        # ==================================================

        ligacao = None

        try:

            ligacao = sqlite3.connect("rpg.db")

            cursor = ligacao.cursor()

            cursor.execute("""
                UPDATE Personagens
                SET
                    nome = ?,
                    vida = ?,
                    mana = ?,
                    forca = ?,
                    agilidade = ?,
                    constituicao = ?,
                    inteligencia = ?,
                    sabedoria = ?,
                    carisma = ?,
                    descricao = ?,
                    habilidade = ?
                WHERE id = ?
                AND utilizador_id = ?
            """, (
                nome,
                valores["Vida"],
                valores["Mana"],
                valores["Força"],
                valores["Agilidade"],
                valores["Constituição"],
                valores["Inteligência"],
                valores["Sabedoria"],
                valores["Carisma"],
                descricao,
                habilidade,
                personagem_selecionada_id,
                utilizador_atual_id
            ))

            # ==================================================
            # VERIFICAR SE ALGUMA LINHA FOI ALTERADA
            # ==================================================

            if cursor.rowcount == 0:
                ligacao.rollback()
                ligacao.close()
                ligacao = None

                messagebox.showerror(
                    "Erro",
                    "A personagem não foi encontrada."
                )

                return

            # Guardar alterações

            ligacao.commit()

            ligacao.close()
            ligacao = None

        except sqlite3.Error as erro:

            if ligacao is not None:
                ligacao.rollback()
                ligacao.close()

            messagebox.showerror(
                "Erro",
                f"Não foi possível alterar a personagem:\n\n{erro}"
            )

            return

        # ==================================================
        # ATUALIZAR LISTBOX
        # ==================================================

        carregar_personagens()

        # ==================================================
        # VOLTAR A SELECIONAR A PERSONAGEM
        # ==================================================

        for indice in range(lista_personagens.size()):

            texto = lista_personagens.get(indice)

            try:

                personagem_id = int(
                    texto.split(" - ")[0]
                )

            except (ValueError, IndexError):
                continue

            if personagem_id == personagem_selecionada_id:
                lista_personagens.selection_set(indice)

                lista_personagens.see(indice)

                break

        # ==================================================
        # CONFIRMAÇÃO
        # ==================================================

        messagebox.showinfo(
            "Personagem",
            f"Personagem '{nome}' alterada com sucesso!"
        )

    botao_alterar = criar_botao(
        frame_botoes,
        "Alterar",
        alterar_personagem,
        AMARELO,
        AMARELO_HOVER,
        AMARELO_ATIVO
    )

    botao_alterar.grid(
        row=1,
        column=0,
        padx=80,
        pady=(5, 15),
        sticky="ew"
    )




    # ======================================================
    # BOTÃO APAGAR
    # ======================================================

    # ======================================================
    # APAGAR PERSONAGEM
    # ======================================================

    def apagar_personagem():

        global personagem_selecionada_id

        # ==================================================
        # VERIFICAR SE EXISTE PERSONAGEM SELECIONADA
        # ==================================================

        if personagem_selecionada_id is None:
            messagebox.showwarning(
                "Atenção",
                "Selecione primeiro uma personagem na lista."
            )

            return

        # ==================================================
        # OBTER NOME DA PERSONAGEM
        # ==================================================

        try:

            ligacao = sqlite3.connect("rpg.db")
            cursor = ligacao.cursor()

            cursor.execute("""
                SELECT nome
                FROM Personagens
                WHERE id = ?
                AND utilizador_id = ?
            """, (
                personagem_selecionada_id,
                utilizador_atual_id
            ))

            personagem = cursor.fetchone()

            ligacao.close()

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível encontrar a personagem:\n\n{erro}"
            )

            return

        # ==================================================
        # PERSONAGEM NÃO ENCONTRADA
        # ==================================================

        if personagem is None:
            messagebox.showerror(
                "Erro",
                "A personagem selecionada não foi encontrada."
            )

            return

        nome_personagem = personagem[0]

        # ==================================================
        # PEDIR CONFIRMAÇÃO
        # ==================================================

        resposta = messagebox.askyesno(
            "Apagar Personagem",
            f"Tem a certeza que pretende apagar a personagem "
            f"'{nome_personagem}'?\n\n"
            f"Esta ação não pode ser desfeita."
        )

        if not resposta:
            return

        # ==================================================
        # APAGAR DA BASE DE DADOS
        # ==================================================

        ligacao = None

        try:

            ligacao = sqlite3.connect("rpg.db")
            cursor = ligacao.cursor()

            cursor.execute("""
                DELETE FROM Personagens
                WHERE id = ?
                AND utilizador_id = ?
            """, (
                personagem_selecionada_id,
                utilizador_atual_id
            ))

            # Verificar se foi realmente apagada
            if cursor.rowcount == 0:
                ligacao.rollback()
                ligacao.close()
                ligacao = None

                messagebox.showerror(
                    "Erro",
                    "Não foi possível apagar a personagem."
                )

                return

            ligacao.commit()

            ligacao.close()
            ligacao = None

        except sqlite3.Error as erro:

            if ligacao is not None:
                ligacao.rollback()
                ligacao.close()

            messagebox.showerror(
                "Erro",
                f"Não foi possível apagar a personagem:\n\n{erro}"
            )

            return

        # ==================================================
        # LIMPAR ID DA PERSONAGEM SELECIONADA
        # ==================================================

        personagem_selecionada_id = None

        # ==================================================
        # ATUALIZAR LISTBOX
        # ==================================================

        carregar_personagens()

        # ==================================================
        # LIMPAR CAMPOS
        # ==================================================

        limpar_campos()

        # ==================================================
        # CONFIRMAÇÃO
        # ==================================================

        messagebox.showinfo(
            "Personagem",
            f"A personagem '{nome_personagem}' foi apagada com sucesso!"
        )

    botao_apagar = criar_botao(
        frame_botoes,
        "Apagar",
        apagar_personagem,
        VERMELHO,
        VERMELHO_HOVER,
        VERMELHO_ATIVO
    )

    botao_apagar.grid(
        row=1,
        column=1,
        padx=80,
        pady=(5, 15),
        sticky="ew"
    )


# =========================================================
# INICIAR NA PÁGINA DE LOGIN
# =========================================================

mostrar_login()

janela.mainloop()