import sqlite3 

db_name = 'quiz.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys = on''')

    do('''CREATE TABLE IF NOT EXISTS quiz(id INTEGER PRIMARY KEY, name TEXT)''')

    do('''CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY, question TEXT, answer TEXT, wrong1 TEXT,
       wrong2 TEXT,
       wrong3 TEXT)''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz_content(id INTEGER PRIMARY KEY, id_quiz INTEGER,
       id_question INTEGER,
       FOREIGN KEY (id_quiz) REFERENCES quiz(id),
       FOREIGN KEY (id_question) REFERENCES questions(id) )''')
    
    close()

def clearDB():
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    close()

def addQuestions():
    questions = [('Скільки місяців мають 28 днів ?', 'Всі', 'Один', 'Жодного', 'Два' )]
    open()
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES(?,?,?,?,?)''', questions)
    conn.commit()
    close()

def main():
    clearDB()
    create()
    addQuestions()

if __name__ == '__main__':
    main()
