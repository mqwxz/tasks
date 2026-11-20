from datetime import datetime

# Списки для заметок и дат
notes = []
dates = []

# Создаём файл, если его ещё нет
with open('notes.txt', 'a', encoding='utf-8') as file:
    file.write('')

# Читаем сохранённые заметки
with open('notes.txt', 'r', encoding='utf-8') as file:
    while True:
        number = file.readline()
        if number == '':
            break
        date = file.readline().strip()
        text = file.readline().strip()
        dates.append(date)
        notes.append(text)


def save_notes():
    with open('notes.txt', 'w', encoding='utf-8') as file:
        for i in range(len(notes)):
            file.write(str(i + 1) + '\n')
            file.write(dates[i] + '\n')
            file.write(notes[i] + '\n')


def add_note(text):
    date = datetime.now().strftime('%d.%m.%Y %H:%M')
    dates.append(date)
    notes.append(text)
    save_notes()


def add_steps(count):
    # Создаём файл с шагами, если его нет
    with open('steps.txt', 'a', encoding='utf-8') as file:
        file.write('')

    with open('steps.txt', 'r', encoding='utf-8') as file:
        saved = file.read()

    total = 0
    if saved != '':
        total = int(saved)

    total = total + count

    with open('steps.txt', 'w', encoding='utf-8') as file:
        file.write(str(total))

    text = 'Сегодня пройдено ' + str(count) + ' шагов, всего пройдено - ' + str(total)
    add_note(text)


def add_temperature(value):
    text = 'Сегодняшняя температура - ' + str(value)
    add_note(text)


def add_activity(activity, amount):
    text = 'Активность: ' + activity + ', количество: ' + amount
    add_note(text)


while True:
    print('''
--- МЕНЕДЖЕР ЗАМЕТОК ---
1 - Показать заметки
2 - Добавить заметку
3 - Изменить заметку
4 - Удалить заметку
5 - Записать шаги
6 - Записать температуру
7 - Записать активность
0 - Выход
''')

    choice = input('\nВыберите пункт: ')

    if choice == '1':
        if len(notes) == 0:
            print('Заметок пока нет.')
        else:
            print('\n--- СПИСОК ЗАМЕТОК ---')
            for i in range(len(notes)):
                print('Номер:', i + 1)
                print('Дата:', dates[i])
                print('Текст:', notes[i])
                print()

    elif choice == '2':
        text = input('Введите текст заметки: ')
        add_note(text)
        print('Заметка добавлена.')

    elif choice == '3':
        number = input('Введите номер заметки: ')
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(notes):
                notes[number - 1] = input('Введите новый текст: ')
                save_notes()
                print('Заметка изменена.')
            else:
                print('Такой заметки нет.')
        else:
            print('Нужно ввести номер.')

    elif choice == '4':
        number = input('Введите номер заметки: ')
        if number.isdigit():
            number = int(number)
            if 1 <= number <= len(notes):
                notes.pop(number - 1)
                dates.pop(number - 1)
                save_notes()
                print('Заметка удалена.')
            else:
                print('Такой заметки нет.')
        else:
            print('Нужно ввести номер.')

    elif choice == '5':
        count = input('Сколько шагов прошли? ')
        if count.isdigit():
            add_steps(int(count))
            print('Шаги записаны.')
        else:
            print('Введите число.')

    elif choice == '6':
        value = float(input('Введите температуру (например, 36.6): '))
        add_temperature(value)
        print('Температура записана.')

    elif choice == '7':
        activity = input('Введите название активности: ')
        amount = input('Введите количество: ')
        add_activity(activity, amount)
        print('Активность записана.')

    elif choice == '0':
        print('Работа завершена.')
        break

    else:
        print('Такого пункта нет.')
