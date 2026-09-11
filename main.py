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
# FUNÇÕES
# =========================================================



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

    # =====================================================
    # CONFIGURAÇÃO DO GRID
    # =====================================================

    frame.columnconfigure(0, weight=1)

    # =====================================================
    # TÍTULO
    # =====================================================

    titulo = tk.Label(
        frame,
        text="Entrar na sua Conta",
        font=("Arial", 26),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    titulo.grid(
        row=0,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(30, 25)
    )

    # =====================================================
    # EMAIL
    # =====================================================

    label_email = tk.Label(
        frame,
        text="Endereço de email",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_email.grid(
        row=1,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_email = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1
    )

    entrada_email.grid(
        row=2,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, ESPACO_WIDGET)
    )

    # =====================================================
    # PASSWORD
    # =====================================================

    label_password = tk.Label(
        frame,
        text="Palavra-passe",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_password.grid(
        row=3,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_password = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        show="*"
    )

    entrada_password.grid(
        row=4,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 25)
    )

    # =====================================================
    # LINK
    # =====================================================

    link_criar_conta = tk.Label(
        frame,
        text="Ainda não tem uma conta? Criar Conta",
        font=("Arial", 10, "underline"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        cursor="hand2"
    )

    link_criar_conta.grid(
        row=6,
        column=0,
        pady=(0, 10)
    )

    link_criar_conta.bind(
        "<Button-1>",
        lambda event: mostrar_registo()
    )

    # =====================================================
    # BOTÃO ENTRAR
    # =====================================================

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

        print("ID:", utilizador_id)
        print("Nome:", nome)
        print("Email:", email_bd)

    botao_entrar = tk.Button(
        frame,
        text="Entrar",
        font=("Arial", 11, "bold"),
        fg=BRANCO,
        bg=AZUL,
        activebackground="#0000CC",
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=fazer_login
    )

    botao_entrar.grid(
        row=7,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 15)
    )

    entrada_email.focus()


# =========================================================
# REGISTO
# =========================================================

def mostrar_registo():

    limpar_janela()

    frame = criar_frame_principal()

    # =====================================================
    # CONFIGURAÇÃO DO GRID
    # =====================================================

    frame.columnconfigure(0, weight=1)

    # =====================================================
    # TÍTULO
    # =====================================================

    titulo = tk.Label(
        frame,
        text="Criar Conta",
        font=("Arial", 26),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    titulo.grid(
        row=0,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(30, 25)
    )

    # =====================================================
    # NOME DE UTILIZADOR
    # =====================================================

    label_nome = tk.Label(
        frame,
        text="Nome de Utilizador",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_nome.grid(
        row=1,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_nome = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1
    )

    entrada_nome.grid(
        row=2,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, ESPACO_WIDGET)
    )

    # =====================================================
    # EMAIL
    # =====================================================

    label_email = tk.Label(
        frame,
        text="Endereço de email",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_email.grid(
        row=3,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_email = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1
    )

    entrada_email.grid(
        row=4,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, ESPACO_WIDGET)
    )

    # =====================================================
    # PASSWORD
    # =====================================================

    label_password = tk.Label(
        frame,
        text="Palavra-passe",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_password.grid(
        row=5,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_password = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        show="*"
    )

    entrada_password.grid(
        row=6,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, ESPACO_WIDGET)
    )

    # =====================================================
    # CONFIRMAR PASSWORD
    # =====================================================

    label_confirmar = tk.Label(
        frame,
        text="Confirmar palavra-passe",
        font=("Arial", 10, "bold"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        anchor="w"
    )

    label_confirmar.grid(
        row=7,
        column=0,
        sticky="w",
        padx=MARGEM_X,
        pady=(0, ESPACO_LABEL)
    )

    entrada_confirmar = tk.Entry(
        frame,
        font=("Arial", 12),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        insertbackground=BRANCO,
        relief="solid",
        bd=1,
        show="*"
    )

    entrada_confirmar.grid(
        row=8,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 25)
    )

    # =====================================================
    # LINK PARA LOGIN
    # =====================================================

    link_entrar = tk.Label(
        frame,
        text="Já tem uma conta? Entrar",
        font=("Arial", 10, "underline"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        cursor="hand2"
    )

    link_entrar.grid(
        row=9,
        column=0,
        pady=(0, 10)
    )

    link_entrar.bind(
        "<Button-1>",
        lambda event: mostrar_login()
    )

    # =====================================================
    # BOTÃO REGISTAR
    # =====================================================

    def fazer_registo():

        nome = entrada_nome.get().strip()
        email = entrada_email.get().strip()
        password = entrada_password.get()
        confirmar = entrada_confirmar.get()

        # -------------------------------------------------
        # VALIDAR NOME
        # -------------------------------------------------

        if nome == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza um nome de utilizador."
            )
            entrada_nome.focus()
            return

        # -------------------------------------------------
        # VALIDAR EMAIL
        # -------------------------------------------------

        if email == "":
            messagebox.showwarning(
                "Atenção",
                "Introduza um endereço de email."
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

        # -------------------------------------------------
        # VALIDAR PASSWORD
        # -------------------------------------------------

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

        # -------------------------------------------------
        # CONFIRMAR PASSWORD
        # -------------------------------------------------

        if confirmar == "":
            messagebox.showwarning(
                "Atenção",
                "Confirme a palavra-passe."
            )
            entrada_confirmar.focus()
            return

        if password != confirmar:
            messagebox.showerror(
                "Erro",
                "As palavras-passe não coincidem."
            )
            entrada_confirmar.focus()
            return

        # -------------------------------------------------
        # LIGAÇÃO À DATABASE
        # -------------------------------------------------

        password_hash = basedados.Seguranca.criar_hash(password)

        ligacao = sqlite3.connect("rpg.db")
        cursor = ligacao.cursor()

        cursor.execute("""
            INSERT INTO Utilizadores (nome, email, password)
            VALUES (?, ?, ?)
        """, (nome, email, password_hash))

        ligacao.commit()
        ligacao.close()

        messagebox.showinfo(
            "Conta criada",
            "A conta foi criada com sucesso!"
        )

        # Voltar para o login
        mostrar_login()

    # =====================================================
    # BOTÃO
    # =====================================================

    botao_registar = tk.Button(
        frame,
        text="Registar-se",
        font=("Arial", 11, "bold"),
        fg=BRANCO,
        bg=AZUL,
        activebackground="#0000CC",
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=fazer_registo
    )

    botao_registar.grid(
        row=10,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 15)
    )

    # =====================================================
    # FOCUS
    # =====================================================

    entrada_nome.focus()

    # ENTER = REGISTAR
    janela.bind(
        "<Return>",
        lambda event: fazer_registo()
    )



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

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=0)

    frame.grid_columnconfigure(0, weight=0)
    frame.grid_columnconfigure(1, weight=1)


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
        row=0,
        column=0,
        rowspan=2,
        sticky="nsew"
    )

    # Título

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


    # ------------------------------------------------------
    # Lista
    # ------------------------------------------------------

    lista_personagens = tk.Listbox(
        frame_lista,
        font=("Arial", 11),
        bg=FUNDO_WIDGET,
        fg=BRANCO,
        bd=0,
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


    # Exemplos temporários
    lista_personagens.insert(
        tk.END,
        "Personagem 1"
    )

    lista_personagens.insert(
        tk.END,
        "Personagem 2"
    )

    lista_personagens.insert(
        tk.END,
        "Personagem 3"
    )


    # ======================================================
    # ÁREA DIREITA
    # ======================================================

    frame_direita = tk.Frame(
        frame,
        bg=FUNDO_FORMULARIO,
    )

    frame_direita.grid(
        row=0,
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
        row=1,
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

    def adicionar_personagem():

        nome = entrada_nome.get().strip()

        if nome == "":

            messagebox.showwarning(
                "Atenção",
                "Introduza o nome do personagem."
            )

            entrada_nome.focus()

            return

        messagebox.showinfo(
            "Personagem",
            "Personagem adicionado!"
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

    def alterar_personagem():

        messagebox.showinfo(
            "Personagem",
            "Personagem alterado!"
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

    def apagar_personagem():

        resposta = messagebox.askyesno(
            "Apagar",
            "Tem a certeza que quer apagar este personagem?"
        )

        if resposta:

            messagebox.showinfo(
                "Personagem",
                "Personagem apagado!"
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


# ==========================================================
# ABRIR A APLICAÇÃO
# ==========================================================

mostrar_personagens()

janela.mainloop()


# =========================================================
# INICIAR NA PÁGINA DE LOGIN
# =========================================================

#mostrar_login()

#janela.mainloop()