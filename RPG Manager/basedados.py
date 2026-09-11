import sqlite3
import hashlib
import os


class Database:

    DATABASE = "rpg.db"

    def __init__(self):
        self.criar_base_dados()

    def conectar(self):
        ligacao = sqlite3.connect(self.DATABASE)
        ligacao.execute("PRAGMA foreign_keys = ON")
        return ligacao

    def criar_base_dados(self):

        ligacao = self.conectar()
        cursor = ligacao.cursor()

        # ==========================
        # UTILIZADORES
        # ==========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)

        # ==========================
        # PERSONAGENS
        # ==========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Personagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utilizador_id INTEGER NOT NULL,
        
            nome TEXT NOT NULL,
        
            vida INTEGER DEFAULT 0,
            mana INTEGER DEFAULT 0,
        
            forca INTEGER DEFAULT 0,
            agilidade INTEGER DEFAULT 0,
            constituicao INTEGER DEFAULT 0,
            inteligencia INTEGER DEFAULT 0,
            sabedoria INTEGER DEFAULT 0,
            carisma INTEGER DEFAULT 0,
        
            descricao TEXT,
            habilidade TEXT,
        
            FOREIGN KEY (utilizador_id)
                REFERENCES Utilizadores(id)
                ON DELETE CASCADE
        );
        """)

        ligacao.commit()
        ligacao.close()


class Seguranca:

    @staticmethod
    def criar_hash(password):

        salt = os.urandom(16)

        hash_password = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            600000
        )

        return salt.hex() + ":" + hash_password.hex()

    @staticmethod
    def verificar_password(password, password_guardada):

        salt, hash_guardado = password_guardada.split(":")

        novo_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            600000
        )

        return novo_hash.hex() == hash_guardado