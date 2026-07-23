import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "rpg_manager.db"

SQL_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS Players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Races (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        strength_bonus INTEGER DEFAULT 0,
        dexterity_bonus INTEGER DEFAULT 0,
        constitution_bonus INTEGER DEFAULT 0,
        intelligence_bonus INTEGER DEFAULT 0,
        wisdom_bonus INTEGER DEFAULT 0,
        charisma_bonus INTEGER DEFAULT 0
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        hp_dice TEXT,
        mana_bonus INTEGER DEFAULT 0,
        stamina_bonus INTEGER DEFAULT 0
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_number INTEGER NOT NULL UNIQUE,
        experience_required INTEGER DEFAULT 0,
        attribute_points INTEGER DEFAULT 0
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        nickname TEXT,
        level INTEGER NOT NULL,
        experience INTEGER DEFAULT 0,
        race_id INTEGER,
        class_id INTEGER,
        hp_max INTEGER DEFAULT 0,
        hp_current INTEGER DEFAULT 0,
        mana_max INTEGER DEFAULT 0,
        mana_current INTEGER DEFAULT 0,
        stamina_max INTEGER DEFAULT 0,
        stamina_current INTEGER DEFAULT 0,
        strength INTEGER DEFAULT 0,
        dexterity INTEGER DEFAULT 0,
        constitution INTEGER DEFAULT 0,
        intelligence INTEGER DEFAULT 0,
        wisdom INTEGER DEFAULT 0,
        charisma INTEGER DEFAULT 0,
        gold INTEGER DEFAULT 0,
        appearance TEXT,
        notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(player_id) REFERENCES Players(id) ON DELETE CASCADE,
        FOREIGN KEY(level) REFERENCES Levels(level_number),
        FOREIGN KEY(race_id) REFERENCES Races(id),
        FOREIGN KEY(class_id) REFERENCES Classes(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        effect TEXT,
        type TEXT,
        rarity TEXT,
        attack INTEGER DEFAULT 0,
        defense INTEGER DEFAULT 0,
        value INTEGER DEFAULT 0,
        weight REAL DEFAULT 0
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Character_Items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        equipped INTEGER DEFAULT 0,
        slot TEXT,
        FOREIGN KEY(character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY(item_id) REFERENCES Items(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        effect TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Character_Skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER NOT NULL,
        skill_id INTEGER NOT NULL,
        level INTEGER DEFAULT 1,
        FOREIGN KEY(character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY(skill_id) REFERENCES Skills(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Feats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        effect TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Character_Feats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER NOT NULL,
        feat_id INTEGER NOT NULL,
        level INTEGER DEFAULT 1,
        FOREIGN KEY(character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY(feat_id) REFERENCES Feats(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Spells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        effect TEXT,
        spell_level INTEGER DEFAULT 0,
        mana_cost INTEGER DEFAULT 0,
        cooldown INTEGER DEFAULT 0,
        school TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Character_Spells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER NOT NULL,
        spell_id INTEGER NOT NULL,
        FOREIGN KEY(character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY(spell_id) REFERENCES Spells(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT,
        description TEXT,
        danger_level INTEGER DEFAULT 0,
        parent_location_id INTEGER,
        FOREIGN KEY(parent_location_id) REFERENCES Locations(id) ON DELETE SET NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS NPCs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        title TEXT,
        race_id INTEGER,
        class_id INTEGER,
        level INTEGER DEFAULT 1,
        hp_max INTEGER DEFAULT 0,
        mana_max INTEGER DEFAULT 0,
        location_id INTEGER,
        description TEXT,
        notes TEXT,
        FOREIGN KEY(race_id) REFERENCES Races(id),
        FOREIGN KEY(class_id) REFERENCES Classes(id),
        FOREIGN KEY(location_id) REFERENCES Locations(id) ON DELETE SET NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Monsters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        tier TEXT,
        type TEXT,
        level INTEGER DEFAULT 1,
        hp INTEGER DEFAULT 0,
        damage INTEGER DEFAULT 0,
        armor INTEGER DEFAULT 0,
        experience_reward INTEGER DEFAULT 0,
        gold_reward INTEGER DEFAULT 0,
        weakness TEXT,
        description TEXT,
        location_id INTEGER,
        FOREIGN KEY(location_id) REFERENCES Locations(id) ON DELETE SET NULL
    );
    """
]


def create_connection(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    with conn:
        for statement in SQL_STATEMENTS:
            conn.execute(statement)


def initialize_database(db_path: Path | str = DB_FILE) -> Path:
    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)
    with create_connection(db_file) as conn:
        create_tables(conn)
    return db_file


if __name__ == "__main__":
    initialize_database()
