import sqlite3
from prettytable import PrettyTable

def f1():
    """Выведите список всех студентов.
    Атрибуты вывода: name, surname, age.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name, 
                 surname, 
                 age 
                 FROM student''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю
    pt.align[col_names[1]] = "l"

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()
    # raise NotImplementedError()


def f2():
    """Выведите отсортированный по фамилиям список студентов из группы ЮРИ-401.
    Имя группы произвольно.
    Атрибуты вывода: "Группа", "Фамилия", "Имя".

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                    s.surname, 
                    s.name,
                    g.name AS "group"
                 FROM student s 
                 JOIN "group" g ON s.group_id = g.id
                 WHERE g.id = 3
                 ORDER BY s.surname; 
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю
    pt.align[col_names[1]] = "l"

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()
    # raise NotImplementedError()

def f3():
    """Выведите всех девушек, обучающихся на факультете 'Реклама'.
    Атрибуты вывода: Название факультета, фамилия.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                 s.surname,
                 d.name
                 FROM student s
                 JOIN department d ON s.group_id = d.id
                 WHERE s.gender = 'Женский'
                 AND d.name = "Торг. дело"
                 ORDER BY s.surname; 
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю
    pt.align[col_names[1]] = "l"

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()
    # raise NotImplementedError()

def f4():
    """Определите количество молодых людей, обучающихся на юридическом факультете.
    Атрибуты вывода: 'Кол-во молодых людей'. Количество строк: 1.
    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT 
                 COUNT(*)
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE
                    d.name = "Юриспруденция"; 
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()
    


def f5():
    """Определите средний возраст студентов, обучающихся на юридическом факультете.
    Округлите результат до целого числа.
    Атрибуты вывода: 'Юр. фак-т. Средний возраст'. Количество строк: 1.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT ROUND(AVG(s.age)) AS "Юрфак. Средний возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция';
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()
    

def f6():
    """Выведите студентов количество, обучающихся на каждом факультете.
    Атрибуты вывода: 'Факультет', 'Количество'. Количество строк должно быть 
    равно количеству факультетов.

        """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT d.name AS "Факультет",
                 COUNT(s.id) AS "Количество"
                 FROM department d
                 LEFT JOIN "group" g ON d.id = g.department_id
                 LEFT JOIN student s ON g.id = s.group_id
                 GROUP BY d.name;
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()


def f7():
    """Выведите средний возраст студентов, обучающихся на каждом факультете.
    Результат округлите до 2-х знаков после точки.
    Атрибуты вывода: 'Факультет', 'Средний возраст'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT d.name AS "Факультет",
                 ROUND(AVG(s.age), 2) AS "Средний возраст"
                 FROM department d
                 JOIN "group" g ON d.id = g.department_id
                 JOIN student s ON g.id = s.group_id
                 GROUP BY d.name;
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()

def f8():
    """Выведите список студентов, которые не обучаются на юридическом факультете.
    Атрибуты вывода: 'Факультет', 'Группа', 'ФИО'. Атрибут ФИО  должен состоять из фамилии,
    первой буквы имени и точки (напр. Иванов И.).
    
    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                SELECT d.name AS "Факультет",
                g.name AS "Группа",
                s.surname || ' ' || SUBSTR(s.name, 1, 1) || '.' AS "ФИО"
                FROM student s
                JOIN "group" g ON s.group_id = g.id
                JOIN department d ON g.department_id = d.id
                WHERE d.name <> 'Юриспруденция';
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()

def f9():
    """Выведите список студентов юридического факультета, у которых возраст
    меньше среднего по факультету.
    Атрибуты вывода: 'Факультет', 'Фамилия', 'Возраст'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT d.name AS "Факультет",
                 s.surname AS "Фамилия",
                 s.age AS "Возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция'
                 AND s.age < (
                 SELECT AVG(s2.age)
                 FROM student s2
                 JOIN "group" g2 ON s2.group_id = g2.id
                 JOIN department d2 ON g2.department_id = d2.id
                 WHERE d2.name = 'Юриспруденция'
                 );
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()

def f10():
    """Выведите список студентов, у которых фамилия начинается на букву 'К'.
    Атрибуты вывода: 'Факультет', 'Группа', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                SELECT d.name AS "Факультет",
                g.name AS "Группа",
                s.surname AS "Фамилия"
                FROM student s
                JOIN "group" g ON s.group_id = g.id
                JOIN department d ON g.department_id = d.id
                WHERE s.surname LIKE 'К%';
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()

def f11():
    """Выведите список студентов группы ЮРИ-401 (имя группы произвольно),
    у которых имя заканчивается на букву 'й' (напр. Аркадий).
    Атрибуты вывода: 'Группа', 'Имя', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                SELECT g.name AS "Группа",
                s.name AS "Имя",
                s.surname AS "Фамилия"
                FROM student s
                JOIN "group" g ON s.group_id = g.id
                WHERE g.name = 'ТОР-102'
                AND s.name LIKE '%й';
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()


def f12():
    '''Выведите студента с самой длинной по количеству символов фамилией.
    Атрибуты вывода: "Фамилия", "Кол-во символов"

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT s.surname AS "Фамилия",
                LENGTH(s.surname) AS "Кол-во символов"
                FROM student s
                ORDER BY LENGTH(s.surname) DESC
                LIMIT 1;
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()


def f13():
    '''Выведите уникальный список женских имен и количество их повторений.
    Список должен быть отсортирован по количеству повторений в порядке убывания.
    Атрибуты вывода: "Фамилия", "Кол-во повторений"

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT s.name AS "Фамилия",
                COUNT(*) AS "Кол-во повторений"
                FROM student s
                WHERE s.gender = 'Женский'
                GROUP BY s.name
                ORDER BY COUNT(*) DESC;
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
    print(pt)
    con.close()

def f14():
    '''Выведите 3 последние записи из таблицы student.
    Сортировку не использовать.
    Атрибуты вывода: id, surname

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''
                 SELECT id, surname
                FROM student
                LIMIT 3 OFFSET (
                    SELECT COUNT(*) FROM student
                ) - 3;
                 ''')
    
    #получим имена столбцов из свойства description курсора
    col_names = [cn[0] for cn in curs.description]
    #получим данные
    rows = curs.fetchall()

    #Инициализируем таблицу c заголовками
    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l" # Выравнивание столбца по левому краю

    #Добавим данные в таблицу
    for row in rows:
        pt.add_row(row)
    
    #Выводим таблицу
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
