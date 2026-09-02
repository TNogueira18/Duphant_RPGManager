import tkinter as tk
from tkinter import messagebox


# =========================================================
# CONFIGURAÇÕES
# =========================================================

FORMULARIO_LARGURA = 2 / 3
FORMULARIO_ALTURA = 2 / 3

# Cores
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
        bg=FUNDO_WIDGET,
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
        bg=FUNDO_WIDGET,
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
    # CHECKBOX
    # =====================================================

    manter_conta = tk.BooleanVar(value=False)

    frame_checkbox = tk.Frame(
        frame,
        bg=CINZENTO_TEXTO
    )

    frame_checkbox.grid(
        row=5,
        column=0,
        sticky="ew",
        padx=MARGEM_X,
        pady=(0, 20)
    )

    frame_checkbox.columnconfigure(0, weight=1)

    checkbox = tk.Checkbutton(
        frame_checkbox,
        text="Manter conta aberta neste dispositivo",
        variable=manter_conta,
        font=("Arial", 10),
        fg=BRANCO,
        bg=CINZENTO_TEXTO,
        activebackground=CINZENTO_TEXTO,
        activeforeground=BRANCO,
        selectcolor=CINZENTO_TEXTO,
        anchor="w",
        relief="flat"
    )

    checkbox.grid(
        row=0,
        column=0,
        sticky="w",
        padx=8,
        pady=35
    )

    # =====================================================
    # LINK
    # =====================================================

    link_criar_conta = tk.Label(
        frame,
        text="Ainda não tem uma conta? Criar Conta",
        font=("Arial", 10, "underline"),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
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

        messagebox.showinfo(
            "Login",
            "Login efetuado com sucesso!"
        )

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

    # =====================================================
    # TEXTO INFERIOR
    # =====================================================

    texto_privacidade = tk.Label(
        frame,
        text="O seu nome de perfil no Game será partilhado. Nunca envie palavras-passe.",
        font=("Arial", 7),
        fg=CINZENTO_TEXTO,
        bg=FUNDO_WIDGET
    )

    texto_privacidade.grid(
        row=8,
        column=0,
        pady=(0, 3)
    )

    texto_protecao = tk.Label(
        frame,
        text="Saiba como processamos os seus dados",
        font=("Arial", 7, "underline"),
        fg=BRANCO,
        bg=FUNDO_WIDGET,
        cursor="hand2"
    )

    texto_protecao.grid(
        row=9,
        column=0
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
        # FUTURA LIGAÇÃO À DATABASE
        # -------------------------------------------------

        print("================================")
        print("REGISTO")
        print("Nome:", nome)
        print("Email:", email)
        print("Password:", password)
        print("================================")

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
    # TEXTO INFERIOR
    # =====================================================

    texto_privacidade = tk.Label(
        frame,
        text="O seu nome de perfil no Game será partilhado. Nunca envie palavras-passe.",
        font=("Arial", 7),
        fg=CINZENTO_TEXTO,
        bg=FUNDO_FORMULARIO
    )

    texto_privacidade.grid(
        row=11,
        column=0,
        pady=(0, 3)
    )

    texto_protecao = tk.Label(
        frame,
        text="Saiba como processamos os seus dados",
        font=("Arial", 7, "underline"),
        fg=BRANCO,
        bg=FUNDO_FORMULARIO,
        cursor="hand2"
    )

    texto_protecao.grid(
        row=12,
        column=0
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


# =========================================================
# INICIAR NA PÁGINA DE LOGIN
# =========================================================

mostrar_login()

janela.mainloop()