import sqlite3

def create_db(): #создать бд
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dolg_table (
                    № INTEGER PRIMARY KEY,
                    Фамилия TEXT,
                    Имя TEXT,
                    Задолженность REAL
                )
            ''')
    cursor.execute("DELETE FROM dolg_table")
    conn.commit()
    conn.close()

def insert_db(data_to_insert): #добавить данные в бд
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dolg_table")
    cursor.executemany('''
            INSERT INTO dolg_table (Фамилия, Имя, Задолженность)
            VALUES (?, ?, ?)
        ''', data_to_insert)
    conn.commit()
    conn.close()

def read_db(): #получить данные из бд
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dolg_table")
    data_from_db = cursor.fetchall()
    conn.close()
    return data_from_db

def delete_db(): #удалить все данные из бд
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dolg_table")
    conn.commit()
    conn.close()