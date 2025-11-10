def add_item(shopping_list):
    purchase = input("Введіть назву товару: ")
    shopping_list.append(purchase)
def show_list(shopping_list):
    pass

def count_total():
    pass

def save_to_file():
    pass

def load_from_file():
    pass

def main():
    print("🛒 Вітаю у менеджері покупок!")
    shopping_list = []

    while True:
        print(''' 
    Меню:
1. Додати покупку
2. Переглянути список
3. Порахувати загальну суму
4. Зберегти у файл
5. Завантажити з файлу
6. Вихід
        ''')
        choise = int(input("Ваш вибір: "))
        match choise:
            case 1:
                add_item(shopping_list)
            case 2:
                show_list(shopping_list)
            case 3:
                count_total()
            case 4:
                save_to_file()
            case 5:
                load_from_file()
            case 6:
                print("Побачимось!")
                break
            case _: #як else, якщо не знайшло попереднє
                print("Неправильні данні! Введіть данні від 1 до 6")

main()




