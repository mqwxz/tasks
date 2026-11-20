# Лабораторная работа 6. Задание 1
# Анализ текста из файла

while True:
    print('\n--- АНАЛИЗ ТЕКСТА ---\n'
          '1 - Прочитать текст из файла\n'
          '2 - Ввести свой текст\n'
          '0 - Выход')

    choice = input('Выберите действие: ')

    if choice == '0':
        print('Программа завершена.')
        break

    if choice == '1':
        name = input('Название файла без .txt: ')
        filename = name + '.txt'

        # Если файла нет, сначала создаём пустой файл.
        with open(filename, 'a', encoding='utf-8') as file:
            file.write('')

        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        if text == '':
            print('Файл пустой. Добавьте в него текст и попробуйте снова.')
            continue

    elif choice == '2':
        name = input('Название файла без .txt: ')
        filename = name + '.txt'
        text = ''

        print('Введите текст. Пустая строка завершает ввод:')
        while True:
            line = input()
            if line == '':
                break
            text = text + line + '\n'

        if text == '':
            print('Вы ничего не ввели.')
            continue

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    else:
        print('Такого пункта нет.')
        continue

    # Убираем знаки препинания, чтобы они не считались частью слов.
    for sign in '.,!?;:()"«»—-':
        text = text.replace(sign, ' ')

    words = text.split()

    if len(words) == 0:
        print('В тексте нет слов.')
        continue

    print('\n--- ЧТО НУЖНО УЗНАТЬ? ---\n'
          '1 - Средняя длина слов\n'
          '2 - Количество слов\n'
          '3 - Самое длинное слово\n'
          '4 - Количество разных слов')
    choice = input('Введите номера нужных пунктов, например 1234: ')

    result = 'Результаты для файла ' + filename + '\n'
    count = 0

    if '1' in choice:
        total = 0
        for word in words:
            total = total + len(word)
        average = round(total / len(words), 2)
        result = result + 'Средняя длина слов: ' + str(average) + '\n'
        count = count + 1

    if '2' in choice:
        result = result + 'Количество слов: ' + str(len(words)) + '\n'
        count = count + 1

    if '3' in choice:
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        result = result + 'Самое длинное слово: ' + longest + '\n'
        count = count + 1

    if '4' in choice:
        different = []
        for word in words:
            word = word.lower()
            if word not in different:
                different.append(word)
        result = result + 'Количество уникальных слов: ' + str(len(different)) + '\n'
        count = count + 1

    if count == 0:
        print('Вы не выбрали ни одного показателя.')
        continue

    result_filename = name + '_result.txt'
    with open(result_filename, 'w', encoding='utf-8') as file:
        file.write(result)

    print('\n' + result + 'Результат записан в файл ' + result_filename)

