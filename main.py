def add_item(shopping_list):
    name = input("Введіть назву товару: ")
    amount = int(input("Введіть кількість:  "))
    price = float(input("Введіть ціну за одиницю: "))
    item = {
        "name" : name,
        "amount" : amount,
        "price" : price
    }
    shopping_list.append(item)

    print(f"✅{name} додано ло списку")

def show_list(shopping_list):
    if not shopping_list:
        print("Ваш список порожній. Додайте щось в пункті 1")
        return
    # for i in range(len(shopping_list)):
    #     print(f"{i+1} : {shopping_list[i]["name"]} - {shopping_list[i]["amount"]} x {shopping_list[i]["price"]} гривень")
    print("\n Ваш список: ")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i} : {item["name"]} - {item["amount"]} x {item["price"]} гривень")


def count_total(shopping_list):
    total = 0
    for item in shopping_list:
        total += item["amount"] * item["price"]
    print(f"Ви витратили {total:.2f} €!")

def save_to_file(shopping_list):
     # "w" - перезаписує файл якщо той є або створює новий, якщо немає
    # "a" - дописує (за замовчуванням у кінці файлу) у існуючий файл, якщо файлу немає - помилка
    # file = open("text.txt", "w", encoding="utf-8")
    # file.write("Ok")
    # file.write("2 line")
    # file.write("new_line")
    # file.close()
    # with open("text.txt", "w", encoding="utf-8") as f:
    #     f.write("Ok")
    #     f.write("2 line")
    #     f.write("new_line")
    # Відкриваємо (або створюємо) файл text.txt у режимі запису з кодуванням UTF-8 (усі знаки всіх мов)
    with open("text.txt", "w", encoding="utf-8") as f:
        # Перебираємо всі елементи списку з нумерацією, починаючи з 1
        for i, item in enumerate(shopping_list, start=1):
            # Записуємо кожен товар у файл у форматі: "1. Яблука - 3 x 2.5€"
            f.write(f"{i}. {item['name']} - {item['amount']} x {item['price']}€\n")
    # Повідомлення про успішне збереження
    print("✅ Shopping_list збережено в text.txt")

# Функція для завантаження списку покупок із файлу
def load_from_file():
    shopping_list = []  # створюємо порожній список для зчитаних елементів
    # Відкриваємо файл text.txt у режимі читання
    with open("text.txt", "r", encoding="utf-8") as f:
        # Зчитуємо кожен рядок файлу
        for line in f:
            # Видаляємо пробіли на краях рядка, прибираємо останній символ (€), розділяємо слова
            line_list = line.strip()[:-1].split()
            # Розбираємо елементи за позиціями:
            # [1] — назва, [3] — кількість, [5] — ціна
            name, quantity, price = line_list[1], line_list[3], line_list[5]
            # Формуємо словник товару
            item = {
                "name": name,
                "amount": int(quantity),
                "price": float(price)
            }
            # Додаємо товар до списку
            shopping_list.append(item)
    print("✅Файл завантажено")
    # Повертаємо відновлений список покупок
    return shopping_list
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
        try:
            choise = int(input("Ваш вибір: "))
        except ValueError:
            print("Введіть число від 1 до 6")
            continue
        match choise:
            case 1:
                try:
                    add_item(shopping_list)
                # except:
                #     print("Error")
                except Exception as e:
                    print(f"Your error is {e}")
            case 2:
                show_list(shopping_list)
            case 3:
                count_total(shopping_list)
            case 4:
                save_to_file(shopping_list)
            case 5:
                try:
                    shopping_list = load_from_file()
                except FileNotFoundError:
                    print("FileNotFoundError")
            case 6:
                print("Побачимось!")
                break
            case _: #як else, якщо не знайшло попереднє
                print("Неправильні данні! Введіть данні від 1 до 6")


if __name__ == "__main__":
    main()
