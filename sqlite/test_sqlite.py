import sqlite3

# Proč je connection podtržené? Oprav chybu

# Co tu chybí?
connection = sqlite3.connect("filmy.db")

cursor = connection.cursor()

int_film = input("Jméno filmu: ")
int_hodnoceni = int(input("Hodnocení filmu ?/10: "))


# Oprav vytváření tabulky - hodnocení je číselné
cursor.execute(
    'CREATE TABLE IF NOT EXISTS hodnoceni (id INTEGER PRIMARY KEY,nazev_filmu,hodnoceni INTEGER)'
)

# Zapsání do databáze

# tady by měl vepsat hodnocení do databáze - není potřeba využívat input, stačí zapsat statický údaj
# cursor.???

cursor.execute('INSERT INTO hodnoceni (nazev_filmu, hodnoceni) VALUES (?,?)', (int_film, int_hodnoceni))

connection.commit()


# Vypisování hodnocení

cursor.execute("SELECT * FROM hodnoceni")

rows = cursor.fetchall()

# tady printne hodnocení filmu z databáze
for row in rows:
    print(row[1], row[2])

connection.close()
