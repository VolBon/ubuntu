import sqlite3
def writeDB(date, time, info):
    conn = sqlite3.connect('log.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS Log;

    CREATE TABLE Log (
        date     TEXT,
        time   TEXT,
        info        TEXT,
        PRIMARY KEY (date)
    )''')

    for 
    cur.execute('''INSERT INTO Log (date, time, info)
                    VALUES ( ?, ?, ? )''', (date, time, info) )

    conn.commit()

for i in data():
    writeDB(date, time, info)