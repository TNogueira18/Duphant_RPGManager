import interface
import database


def main():
    if hasattr(database, "initialize"):
        database.initialize()
    elif hasattr(database, "init_db"):
        database.init_db()

    if hasattr(interface, "main"):
        interface.main()
    elif hasattr(interface, "run"):
        interface.run()


if __name__ == "__main__":
    main()
