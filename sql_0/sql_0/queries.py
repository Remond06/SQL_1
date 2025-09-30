import sqlite3
from prettytable import PrettyTable

def f1():
    """Выведите список всех студентов.
    Атрибуты вывода: name, surname, age.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name, 
                 surname, 
                 age 
                 FROM student''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"
    pt.align[col_names[1]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f2():
    """Выведите отсортированный по фамилиям список студентов из группы ЮРИ-401.
    Имя группы произвольно.
    Атрибуты вывода: "Группа", "Фамилия", "Имя".

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    "group" as "Группа",
                    surname as "Фамилия", 
                    name as "Имя"
                 FROM student
                 WHERE "group" = 'ЮРИ-401'
                 ORDER BY surname; 
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"
    pt.align[col_names[1]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f3():
    """Выведите всех девушек, обучающихся на факультете 'Реклама'.
    Атрибуты вывода: Название факультета, фамилия.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    # Используем группу как индикатор факультета
    curs.execute('''
                 SELECT 
                 "group" as "Факультет/Группа",
                 surname as "Фамилия"
                 FROM student
                 WHERE gender = 'Женский'
                 AND "group" LIKE '%РЕК%' OR "group" LIKE '%Реклама%'
                 ORDER BY surname; 
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"
    pt.align[col_names[1]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f4():
    """Определите количество молодых людей, обучающихся на юридическом факультете.
    Атрибуты вывода: 'Кол-во молодых людей'. Количество строк: 1.
    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                 COUNT(*) as "Кол-во молодых людей"
                 FROM student
                 WHERE gender = 'Мужской'
                 AND ("group" LIKE 'ЮРИ%' OR "group" LIKE '%Юр%');
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f5():
    """Определите средний возраст студентов, обучающихся на юридическом факультете.
    Округлите результат до целого числа.
    Атрибуты вывода: 'Юр. фак-т. Средний возраст'. Количество строк: 1.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT ROUND(AVG(age)) AS "Юрфак. Средний возраст"
                 FROM student
                 WHERE "group" LIKE 'ЮРИ%' OR "group" LIKE '%Юр%';
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f6():
    """Выведите студентов количество, обучающихся на каждом факультете.
    Атрибуты вывода: 'Факультет', 'Количество'. Количество строк должно быть 
    равно количеству факультетов.

        """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    # Используем первые 3 символа группы как факультет
    curs.execute('''
                 SELECT 
                    SUBSTR("group", 1, 3) AS "Факультет",
                    COUNT(*) AS "Количество"
                 FROM student
                 GROUP BY SUBSTR("group", 1, 3);
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f7():
    """Выведите средний возраст студентов, обучающихся на каждом факультете.
    Результат округлите до 2-х знаков после точки.
    Атрибуты вывода: 'Факультет', 'Средний возраст'.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    SUBSTR("group", 1, 3) AS "Факультет",
                    ROUND(AVG(age), 2) AS "Средний возраст"
                 FROM student
                 GROUP BY SUBSTR("group", 1, 3);
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f8():
    """Выведите список студентов, которые не обучаются на юридическом факультете.
    Атрибуты вывода: 'Факультет', 'Группа', 'ФИО'. Атрибут ФИО  должен состоять из фамилии,
    первой буквы имени и точки (напр. Иванов И.).
    
    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                SELECT 
                    SUBSTR("group", 1, 3) AS "Факультет",
                    "group" AS "Группа",
                    surname || ' ' || SUBSTR(name, 1, 1) || '.' AS "ФИО"
                FROM student
                WHERE "group" NOT LIKE 'ЮРИ%' AND "group" NOT LIKE '%Юр%';
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f9():
    """Выведите список студентов юридического факультета, у которых возраст
    меньше среднего по факультету.
    Атрибуты вывода: 'Факультет', 'Фамилия', 'Возраст'.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    "group" AS "Группа",
                    surname AS "Фамилия",
                    age AS "Возраст"
                 FROM student
                 WHERE ("group" LIKE 'ЮРИ%' OR "group" LIKE '%Юр%')
                 AND age < (
                     SELECT AVG(age) 
                     FROM student 
                     WHERE "group" LIKE 'ЮРИ%' OR "group" LIKE '%Юр%'
                 );
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f10():
    """Выведите список студентов, у которых фамилия начинается на букву 'К'.
    Атрибуты вывода: 'Факультет', 'Группа', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                SELECT 
                    SUBSTR("group", 1, 3) AS "Факультет",
                    "group" AS "Группа",
                    surname AS "Фамилия"
                FROM student
                WHERE surname LIKE 'К%';
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f11():
    """Выведите список студентов группы ЮРИ-401 (имя группы произвольно),
    у которых имя заканчивается на букву 'й' (напр. Аркадий).
    Атрибуты вывода: 'Группа', 'Имя', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                SELECT 
                    "group" AS "Группа",
                    name AS "Имя",
                    surname AS "Фамилия"
                FROM student
                WHERE "group" = 'ЮРИ-401'
                AND name LIKE '%й';
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f12():
    '''Выведите студента с самой длинной по количеству символов фамилией.
    Атрибуты вывода: "Фамилия", "Кол-во символов"

    '''
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    surname AS "Фамилия",
                    LENGTH(surname) AS "Кол-во символов"
                 FROM student
                 ORDER BY LENGTH(surname) DESC
                 LIMIT 1;
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f13():
    '''Выведите уникальный список женских имен и количество их повторений.
    Список должен быть отсортирован по количеству повторений в порядке убывания.
    Атрибуты вывода: "Имя", "Кол-во повторений"

    '''
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    name AS "Имя",
                    COUNT(*) AS "Кол-во повторений"
                 FROM student
                 WHERE gender = 'Женский'
                 GROUP BY name
                 ORDER BY COUNT(*) DESC;
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

def f14():
    '''Выведите 3 последние записи из таблицы student.
    Сортировку не использовать.
    Атрибуты вывода: id, surname

    '''
    print("\n")
    con = sqlite3.connect("university.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT ID, surname
                 FROM student
                 ORDER BY ID DESC
                 LIMIT 3;
                 ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print(pt)
    con.close()

func_register = {
    '1': f1,
    '2': f2,
    '3': f3,
    '4': f4,
    '5': f5,
    '6': f6,
    '7': f7,
    '8': f8,
    '9': f9,
    '10': f10,
    '11': f11,
    '12': f12,
    '13': f13,
    '14': f14
}
