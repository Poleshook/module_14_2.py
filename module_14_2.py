import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#for i in range(10):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
#                   (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", "1000"))
#cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")
#cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
#results = cursor.fetchall()
#for i in results:
#    print(f"Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}")

cursor.execute("DELETE FROM Users WHERE id = 6") #Удаление из базы данных not_telegram.db записи с id = 6
cursor.execute("SELECT COUNT(*) FROM Users") #Подсчёт общего количества записей
total1 = cursor.fetchone()[0] #Присвоение переменной
cursor.execute("SELECT SUM(balance) FROM Users") #Подсчёт суммы всех балансов.
total2 = cursor.fetchone()[0] #Присвоение переменной
print(total2 / total1) #Вывод в консоль среднего баланса всех пользователей


connection.commit()
connection.close()
