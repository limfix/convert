import sqlite3

#Инициализация БД с указанием всех римских чисел
def create_database():
    connect = sqlite3.connect('numbers.db')
    cursor = connect.cursor()
    cursor.execute(''' CREATE TABLE numbers (   'ID' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                'arabic_value' INT,
                                                'roman_value' CHAR,
                                                'limiter' INT)
                                                ''')

    cursor.execute(''' INSERT INTO numbers (ID,arabic_value,roman_value) VALUES (0,1,'I') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (4,'IV') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (5,'V') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (9,'IX') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (10,'X') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (40,'XL') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (50,'L') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (90,'XC') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (100,'C') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (400,'CD') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (500,'D') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (900,'CM') ''')
    cursor.execute(''' INSERT INTO numbers (arabic_value,roman_value) VALUES (1000,'M') ''')
    connect.commit()
    connect.close()
