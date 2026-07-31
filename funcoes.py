from basedados import Database

import sqlite3
import tkinter as tk


class Funcoes_BD:
    def __init__(self):
        self.db = Database()
        self.db.criar_base_dados()

    def inserir_race(self, nome, description):
        self.db.cursor.execute("INSERT INTO Races (nome, description) VALUES (?, ?)", (nome, description))
        self.db.ligacao.commit()

    def inserir_player(self, nome, nickname):
        self.db.cursor.execute("INSERT INTO Players (nome, nickname) VALUES (?, ?)", (nome, nickname))
        self.db.ligacao.commit()

    def inserir_location(self, nome, nivel, localizacao):
        self.db.cursor.execute("INSERT INTO Locations (nome, nivel_perigo, localizacao) VALUES (?, ?, ?)", (nome, nivel, localizacao))
        self.db.ligacao.commit()

    def inserir_class(self, nome, description):
        self.db.cursor.execute("INSERT INTO Classes (nome, description) VALUES (?, ?)", (nome, description))
        self.db.ligacao.commit()

    def inserir_item(self, nome, description, dmg, hp, stat):
        self.db.cursor.execute("INSERT INTO Items (nome, description, dmg, hp, stat_used) VALUES (?, ?, ?, ?, ?)", (nome, description, dmg, hp, stat))
        self.db.ligacao.commit()

    def inserir_skill(self, nome, description, stamina_cost, cooldown):
        self.db.cursor.execute("INSERT INTO Skills (nome, description, stamina_cost, cooldown) VALUES (?, ?, ?, ?)", (nome, description, stamina_cost, cooldown))
        self.db.ligacao.commit()

    def inserir_spell(self, nome, description, mana_cost, cooldown):
        self.db.cursor.execute("INSERT INTO Spells (nome, description, mana_cost, cooldown) VALUES (?, ?)", (nome, description, mana_cost, cooldown))
        self.db.ligacao.commit()

    def inserir_character(self, nome, race_id, class_id, player_id):
        self.db.cursor.execute("INSERT INTO Characters (nome, race_id, class_id, player_id) VALUES (?, ?, ?, ?)", (nome, race_id, class_id, player_id))
        self.db.ligacao.commit()