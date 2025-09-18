import os
from queries import func_register

# Очистка экрана
cls = lambda: os.system('cls')

def show_menu():
    '''Показывает меню SQL-задач и выполняет выбранную задачу.\n
    Ввод номера задачи приводит к выполнению функции с её решением;\n
    ввод символа 'h' показывает меню заново;\n
    ввод символа 'q' завершает работу программы.'''

    choice = None # Выбранная задача или символ действия.
    is_answer = False # Показать меню заново или нет. Если введен номер задачи, меню не показывается.
 
    while choice != "q": #Цикл продолжается пока не введен 'q'.
        
        if not is_answer:
            cls()
            for key, value in func_register.items():
                print(f"{key}) {value.__doc__}")

        choice = input("Действие: ").lower().strip()

        if choice in func_register: # Выполнение выбранной задачи.
            cls() # Очистка экрана
            is_answer = True
            func_register[choice]() # Выполнение выбранной задачи.
        elif choice == 'h': # Показать меню заново.
            # print("\n" * 50)
            cls()
            is_answer = False    


if __name__ == "__main__":
    show_menu()
