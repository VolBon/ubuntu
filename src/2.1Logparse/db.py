import sqlite3

data = [['19.02', '12:00', 'some log text with important in'], ['19.02', '12:00', 'some log text with important info'], ['19.02', '12:00', 'some log text with important']]

def writeDB():
    conn = sqlite3.connect('log.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS Log;

    CREATE TABLE Log (
        date     TEXT,
        time   TEXT,
        info        TEXT
            )''')

    for i in data:
        print i
        cur.execute('''INSERT INTO Log (date, time, info)
                    VALUES ( ?, ?, ? )''', (i[0], i[1], i[2]) )

    conn.commit()

writeDB()