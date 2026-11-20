from datetime import datetime

# Товары магазина
names = []
categories = []
prices = []
cart = []

# Деньги покупателя
money = 5000

# Создаём файл каталога, если его нет
with open('catalog.txt', 'a', encoding='utf-8') as file:
    file.write('')

# Читаем товары из файла
with open('catalog.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.split(',')

        if len(parts) == 3:
            name = parts[0].strip()
            category = parts[1].strip()
            price = parts[2].strip()

            if name != '' and category != '' and price.isdigit():
                names.append(name)
                categories.append(category)
                prices.append(int(price))
                cart.append(0)
            else:
                print('Неверная строка в каталоге:', line.strip())
        else:
            print('Неверная строка в каталоге:', line.strip())

while True:
    print('''
--- МАГАЗИН ---
1 - Показать все товары
2 - Найти товары
3 - Добавить в корзину
4 - Посмотреть корзину
5 - Оплатить покупку
6 - Изменить каталог
0 - Выход
''')
    print('Ваши деньги:', money, 'руб.')
    choice = input('Выберите пункт: ')

    if choice == '1':
        print('\n--- КАТАЛОГ ---')
        if len(names) == 0:
            print('Товаров пока нет.')
        else:
            for i in range(len(names)):
                print(i + 1, '-', names[i], '|', categories[i], '|', prices[i], 'руб.')

    elif choice == '2':
        print('''
--- ПОИСК ТОВАРОВ ---
1 - По категории
2 - По цене
3 - По категории и цене
''')
        mode = input('Выберите вариант: ')

        if mode == '1' or mode == '2' or mode == '3':
            if mode == '1' or mode == '3':
                category = input('Введите категорию: ')

            if mode == '2' or mode == '3':
                min_price = int(input('Цена от: '))
                max_price = int(input('Цена до: '))

            print('\n--- НАЙДЕННЫЕ ТОВАРЫ ---')
            found = 0
            for i in range(len(names)):
                show = True

                if mode == '1' or mode == '3':
                    if categories[i].lower() != category.lower():
                        show = False

                if mode == '2' or mode == '3':
                    if prices[i] < min_price or prices[i] > max_price:
                        show = False

                if show:
                    print(i + 1, '-', names[i], '|', categories[i], '|', prices[i], 'руб.')
                    found = found + 1

            if found == 0:
                print('Подходящих товаров нет.')
        else:
            print('Такого варианта нет.')

    elif choice == '3':
        if len(names) == 0:
            print('В каталоге нет товаров.')
        else:
            print('\n--- ТОВАРЫ ---')
            for i in range(len(names)):
                print(i + 1, '-', names[i], '-', prices[i], 'руб.')

            number = input('Номер товара: ')
            if number.isdigit():
                number = int(number)
                if 1 <= number <= len(names):
                    count = input('Количество: ')
                    if count.isdigit() and int(count) > 0:
                        cart[number - 1] = cart[number - 1] + int(count)
                        print('Товар добавлен в корзину.')
                    else:
                        print('Введите правильное количество.')
                else:
                    print('Такого товара нет.')
            else:
                print('Введите номер товара.')

    elif choice == '4':
        print('\n--- КОРЗИНА ---')
        total = 0
        for i in range(len(names)):
            if cart[i] > 0:
                cost = prices[i] * cart[i]
                print(names[i], '-', cart[i], 'шт. -', cost, 'руб.')
                total = total + cost

        if total == 0:
            print('Корзина пустая.')
        else:
            print('Итого:', total, 'руб.')

    elif choice == '5':
        total = 0
        for i in range(len(names)):
            total = total + prices[i] * cart[i]

        if total == 0:
            print('Корзина пустая.')
        elif total > money:
            print('Недостаточно денег. Нужно:', total, 'руб.')
            print('У вас есть:', money, 'руб.')
        else:
            date = datetime.now().strftime('%d.%m.%Y %H:%M')

            with open('checks.txt', 'a', encoding='utf-8') as file:
                file.write('--- ЧЕК ---\n')
                file.write('Дата: ' + date + '\n')
                for i in range(len(names)):
                    if cart[i] > 0:
                        cost = prices[i] * cart[i]
                        file.write(names[i] + ' - ' + str(cart[i]) + ' шт. - ' + str(cost) + ' руб.\n')
                file.write('Итого: ' + str(total) + ' руб.\n\n')

            money = money - total
            for i in range(len(cart)):
                cart[i] = 0

            print('Покупка оплачена!')
            print('Сумма покупки:', total, 'руб.')
            print('Осталось денег:', money, 'руб.')
            print('Чек сохранён в файле checks.txt.')

    elif choice == '6':
        print('''
--- ИЗМЕНЕНИЕ КАТАЛОГА ---
1 - Добавить товар
2 - Изменить товар
3 - Удалить товар
0 - Назад
''')
        action = input('Выберите пункт: ')
        changed = False

        if action == '1':
            name = input('Название товара: ')
            category = input('Категория: ')
            price = input('Цена: ')

            if name != '' and category != '' and price.isdigit() and ',' not in name and ',' not in category:
                names.append(name)
                categories.append(category)
                prices.append(int(price))
                cart.append(0)
                changed = True
                print('Товар добавлен.')
            else:
                print('Неправильно введены данные.')

        elif action == '2' or action == '3':
            for i in range(len(names)):
                print(i + 1, '-', names[i], '-', prices[i], 'руб.')

            number = input('Введите номер товара: ')
            if number.isdigit() and 1 <= int(number) <= len(names):
                number = int(number) - 1

                if action == '2':
                    name = input('Новое название: ')
                    category = input('Новая категория: ')
                    price = input('Новая цена: ')

                    if name != '' and category != '' and price.isdigit() and ',' not in name and ',' not in category:
                        names[number] = name
                        categories[number] = category
                        prices[number] = int(price)
                        changed = True
                        print('Товар изменён.')
                    else:
                        print('Неправильно введены данные.')
                else:
                    names.pop(number)
                    categories.pop(number)
                    prices.pop(number)
                    cart.pop(number)
                    changed = True
                    print('Товар удалён.')
            else:
                print('Такого товара нет.')

        elif action != '0':
            print('Такого пункта нет.')

        if changed:
            with open('catalog.txt', 'w', encoding='utf-8') as file:
                for i in range(len(names)):
                    file.write(names[i] + ', ' + categories[i] + ', ' + str(prices[i]) + '\n')

    elif choice == '0':
        print('До свидания!')
        break

    else:
        print('Такого пункта нет.')
