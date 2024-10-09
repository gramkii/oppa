import sqlite3
conn = sqlite3.connect('Artistc.db')

cursor = conn.cursor()


# Запитання 1. Інформація про скількох художників представлена у базі даних?
cursor.execute('SELECT * FROM artists')
a = cursor.fetchall()
for i in a:
    print(i)

print( len(a) )

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
a = cursor.fetchall()
for i in a:
    print(i)

print( len(a) )

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" <= 1900')
a = cursor.fetchall()
for i in a:
    print(i)

print( len(a) )

# Запитання 4*. Як звати найстаршого художника?
cursor.execute('SELECT * FROM artists ORDER BY "Birth Year"')
a = cursor.fetchall()

print( a[0][1] )