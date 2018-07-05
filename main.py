import sqlite3
import create_db
import sys

def to_roman(x):
    roman_number = ''

    while x > 0:
        for row in rows:
            arabic_value = row[1]
            roman_value = row[2]
            if x > arabic_value:
                last_arabic_value = arabic_value
                last_roman_value = roman_value
                continue
            if x < arabic_value:
                roman_number += last_roman_value
                x -= last_arabic_value
                break
            elif x == arabic_value:
                roman_number += roman_value
                x = 0
                break

    return roman_number

def to_arabic(string):
    string = string[::-1]
    arabic_number = 0
    last_arabic_value = 0
    for i in range(len(string)):
        roman_char = string[i]
        for row in rows:
            arabic_value = row[1]
            roman_value = row[2]
            if roman_char == roman_value:
                arabic_number += arabic_value
                last_arabic_value = arabic_value
                break
            if ( (arabic_value > last_arabic_value) and (last_arabic_value != 0) ):
                arabic_number -= last_arabic_value * 2
                last_arabic_value = 0
    return arabic_number

#Проверка на существование таблицы с эквивалентами арабских и римских чисел
try:
    connect = sqlite3.connect('numbers.db')
    cursor = connect.cursor()
    cursor.execute(''' SELECT * FROM numbers''')
    rows = cursor.fetchall()
    print(to_roman(52))
    print(to_arabic('CCXCIV'))
except sqlite3.OperationalError:
    create_db.create_database()
    print('Database was sucessfull created. Restart main script.')
