import sqlite3


DATABASE = "rpg.db"


def criar_base_dados():

    ligacao = sqlite3.connect(DATABASE)
    cursor = ligacao.cursor()

    # Ativar Foreign Keys
    cursor.execute("""
        PRAGMA foreign_keys = ON;
    """)


    # ==========================
    # RACES
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Races (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT
    );
    """)


    # ==========================
    # PLAYERS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nickname TEXT
    );
    """)


    # ==========================
    # CLASSES
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT
    );
    """)


    # ==========================
    # LOCATIONS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nivel_perigo INTEGER,
        localizacao TEXT
    );
    """)


    # ==========================
    # LEVELS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        xp_required INTEGER NOT NULL,
        bonus INTEGER
    );
    """)


    # ==========================
    # CHARACTERS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Characters (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        player_id INTEGER,
        raca INTEGER,
        classe INTEGER,
        constituition INTEGER,
        dexterity INTEGER,
        strength INTEGER,
        wisdom INTEGER,
        inteligence INTEGER,
        charisma INTEGER,
        ouro INTEGER DEFAULT 0,
        stamina INTEGER,
        stamina_max INTEGER,
        mana INTEGER,
        mana_max INTEGER,
        vida INTEGER,
        vida_max INTEGER,
        level INTEGER DEFAULT 1,

        FOREIGN KEY(player_id)
            REFERENCES Players(id),
        FOREIGN KEY(raca)
            REFERENCES Races(id),
        FOREIGN KEY(classe)
            REFERENCES Classes(id),
        FOREIGN KEY(level)
            REFERENCES Levels(id)

    );
    """)


    # ==========================
    # ITEMS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Items (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT,
        dmg INTEGER,
        stat_used TEXT

    );
    """)


    # ==========================
    # NPCs
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS NPCs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        raca INTEGER,
        trabalho TEXT,
        constituition INTEGER,
        dexterity INTEGER,
        strength INTEGER,
        wisdom INTEGER,
        inteligence INTEGER,
        charisma INTEGER,
        vida INTEGER,
        vida_max INTEGER,
        ouro INTEGER,

        FOREIGN KEY(raca)
            REFERENCES Races(id)

    );
    """)


    # ==========================
    # MONSTROS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Monstros (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        xp_reward INTEGER,
        constituition INTEGER,
        dexterity INTEGER,
        strength INTEGER,
        wisdom INTEGER,
        inteligence INTEGER,
        charisma INTEGER,
        mana INTEGER,
        mana_max INTEGER,
        stamina INTEGER,
        stamina_max INTEGER,
        vida INTEGER,
        vida_max INTEGER

    );
    """)


    # ==========================
    # SKILLS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Skills (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT,
        stamina_cost INTEGER

    );
    """)


    # ==========================
    # FEATS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Feats (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT

    );
    """)


    # ==========================
    # SPELLS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Spells (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        description TEXT,
        mana_cost INTEGER

    );
    """)



    # =================================================
    # TABELAS DE LIGAÇÃO
    # =================================================


    # Character Items

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Items (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        item_id INTEGER,
        quantidade INTEGER DEFAULT 1,

        FOREIGN KEY(character_id)
            REFERENCES Characters(id),

        FOREIGN KEY(item_id)
            REFERENCES Items(id)

    );
    """)



    # Character Skills

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Skills (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        skill_id INTEGER,
        nivel INTEGER DEFAULT 1,

        FOREIGN KEY(character_id)
            REFERENCES Characters(id),

        FOREIGN KEY(skill_id)
            REFERENCES Skills(id)

    );
    """)



    # Character Feats

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Feats (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        feat_id INTEGER,
        nivel INTEGER DEFAULT 1,

        FOREIGN KEY(character_id)
            REFERENCES Characters(id),

        FOREIGN KEY(feat_id)
            REFERENCES Feats(id)

    );
    """)



    # Character Spells

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Spells (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        spell_id INTEGER,

        FOREIGN KEY(character_id)
            REFERENCES Characters(id),

        FOREIGN KEY(spell_id)
            REFERENCES Spells(id)

    );
    """)



    # Monsters Locations

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Location_Monsters (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_id INTEGER,
        monster_id INTEGER,

        FOREIGN KEY(location_id)
            REFERENCES Locations(id),

        FOREIGN KEY(monster_id)
            REFERENCES Monstros(id)

    );
    """)



    ligacao.commit()
    ligacao.close()


    print("Base de dados criada com sucesso!")


# Executar criação

if __name__ == "__main__":
    criar_base_dados()