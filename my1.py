import telebot
from telebot import types
#5336653664:AAHZjXdFcgTDur3CO4iLMNMx7lYbvi-vtws
bot = telebot.TeleBot('5336653664:AAHZjXdFcgTDur3CO4iLMNMx7lYbvi-vtws')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Справочный материал')
    item2 = types.KeyboardButton('Программы')
    item3 = types.KeyboardButton('Сайты')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}! '
                                      'PyBot содержит справочный материал по языку программирования Python,'
                                      ' а также может посоветовать тебе некоторые полезные сайты или программы. '
                                      'Что именно тебя интересует?'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Справочный материал':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Основы программирования')
            item2 = types.KeyboardButton('Основы промышленного программирования')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Справочный материал', reply_markup = markup)

        elif message.text == 'Программы':
            bot.send_message(message.chat.id, 'бидэ')

        elif message.text == 'Сайты':
            bot.send_message(message.chat.id, 'вада')

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Справочный материал')
            item2 = types.KeyboardButton('Программы')
            item3 = types.KeyboardButton('Сайты')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Назад'.format(message.from_user),
                             reply_markup=markup)

        elif message.text == 'Основы программирования':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Переменные')
            item2 = types.KeyboardButton('Ввод')
            item3 = types.KeyboardButton('Вывод')
            item4 = types.KeyboardButton('Комментарии')
            item5 = types.KeyboardButton('Условный оператор')
            item6 = types.KeyboardButton('Операции над строками')
            item7 = types.KeyboardButton('Операции над числами')
            item8 = types.KeyboardButton('Циклы')
            item9 = types.KeyboardButton('Множества')
            item10 = types.KeyboardButton('Классы')
            item11 = types.KeyboardButton('Кортежи')
            item12 = types.KeyboardButton('Списки')
            item13 = types.KeyboardButton('Словари')
            item14 = types.KeyboardButton('Функции')
            item15 = types.KeyboardButton('Обработка коллекций. Потоковый ввод')
            item16 = types.KeyboardButton('Библиотеки')
            item17 = types.KeyboardButton('ООП')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,
                       item11, item12, item13, item14, item15, item16, item17, item18)
            bot.send_message(message.chat.id, 'Основы программирования', reply_markup=markup)

        elif message.text == 'Переменные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Имя переменной должно отражать ее назначение и может состоять из латинских букв, цифр и символа подчеркивания.'
                             ' Имя не может начинаться с цифры.' + '\n'
                             ' Для именования переменных принято использовать слова из маленьких букв с подчеркиваниями.'
                             ' Избегайте использовать такие символы, которые могут не однозначно трактоваться в различных шрифтах:'
                             ' это буква О (большая и маленькая) и цифра 0, буква I (большая и маленькая) и цифра 1. '
                             'Нельзя использовать в качестве имени переменной и ключевые слова, которые существуют в языке.' + '\n'
                             ' Если вы хотите, чтобы у вас была переменная с каким-то именем и каким-то значением, нужно написать на отдельной строчке:'
                             ' <имя переменной> = <значение переменной>' + '\n' +
                             'Пример:' + '\n' + ' bird = "Тук-тук"', reply_markup=markup)

        elif message.text == 'Ввод':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Здесь используется команда input()' + '\n' +
                             'Всегда пишется с круглыми скобками. Команда работает так: ' + '\n' +
                             'когда программа доходит до места, где есть input(), она ждет, пока пользователь введет строку '
                             'с клавиатуры (ввод завершается нажатием клавиши Enter). Введенная строка подставляется на место input().' + '\n' +
                             ' input() получает от пользователя какие-то данные и в место вызова подставляет строковое значение. ' + '\n' +
                             'Если нужно, чтобы пользователь что-то напечатал с клавиатуры и чтобы программа могла использовать эти данные, — пишем input().' + '\n' +
                             'Пример:' + '\n' + ' name = input()', reply_markup=markup)

        elif message.text == 'Вывод':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Для вывода на экран используется команда print()' + '\n' +
                             'Внутри круглых скобок через запятую мы указываем то, что необходимо вывести на экран.'
                             ' Если это какой-то текст, указываем его внутри кавычек.'
                             ' Кавычки могут быть как одинарными, так и двойными.'
                             ' Главное, чтобы текст начинался и заканчивался кавычками одного типа.'
                             ' Команда print записывается только строчными буквами, другое написание недопустимо,'
                             ' так как в Python строчные и заглавные буквы различны.' + '\n' +
                             'Пример:' + '\n' + "print('Привет!')", reply_markup=markup)

        elif message.text == 'Комментарии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Для удобства можно использовать комментарии, '
                             'которые позволяют программисту делать для себя пометки в коде или делать часть кода не выполнимой,'
                             ' не видимой для интерпретатора.' + '\n' +
                             'Если вы начнете строчку со знака решетки #, интерпретатор Python будет игнорировать всю эту строчку.'
                             ' Программа будет выполняться так, как будто строчки нет. Такая строчка называется комментарием.' + '\n' +
                             'Комментарии нужны в двух случаях:' + '\n' +
                             'Когда нужно добавить в программу какую-то пометку для человека, который будет читать эту программу' + '\n' +
                             'Когда нужно убрать какую-то строчку кода, но удалять ее не хочется (например, потом ее, возможно, понадобится вернуть).'
                             ' Это называется «закомментировать» строчку.', reply_markup=markup)

        elif message.text == 'Условный оператор':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Условный оператор используется, когда некая часть программы должна быть выполнена,'
                             ' только если верно какое-либо условие.' + '\n' + 'Для записи условного оператора используются'
                             ' ключевые слова if и else («если», «иначе»), двоеточие и  отступ в четыре пробела.' +'\n' +
                             'Для сравнения нужно использовать двойной знак равенства: ==.' + '\n' +
                             'Пример:' + '\n' + 'if условие:' + '\n' + "    Действия, если условие верно" + '\n' +
                             'else:' + '\n' + '    Действия, если условие неверно' + '\n' + '\n' +
                             'Сложное условие. Логические операции'
                             'Иногда в условном операторе нужно задать сложное условие. '
                             'Для этого можно использовать логические операции and («и»), or («или») и not («не»).' + '\n' +
                             'Чтобы задать одновременное выполнение двух условий, используем and («и»), '
                             'если достаточно выполнения одного из двух вариантов (или обоих сразу) — используем or («или»), '
                             'а если нужно убрать какой-то вариант — not («не»).', reply_markup=markup)

        elif message.text == 'Операции над строками':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Методы строк')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Строки в Python - упорядоченные последовательности символов,'
                                              ' используемые для хранения и представления текстовой информации.' + '\n' +
                                              'Нумерация символов начинается с 0'
                                              'По индексу можно получить соответствующий ему символ строки.'
                                              ' Для этого нужно после самой строки написать в квадратных скобках индекс символа.' + '\n' +
                                              'Пример:' + '\n' + "word = 'привет'" + '\n' + 'initial_letter = word[0]' + '\n' +
                                              "print(initial_letter)  # сделает то же, что print('п')" + '\n' + "other_letter = word[3]" + '\n' +
                                              "print(other_letter)  # сделает то же, что print('в')" + '\n' + '\n' +
                                              'Кроме «прямой» индексации (начинающейся с 0), в Python разрешены'
                                              ' отрицательные индексы: word[-1] означает последний символ строки word,'
                                              ' word[-2] — предпоследний и т д.'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Методы строк':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Проверка, что подстрока s2 содержится в s:' + '\n' +
                             's2 in s' + '\n' + 'Проверка, что подстрока s2 не содержится в s то же, что not (s2 in s):' + '\n' +
                             'Конкатенация (склейка) строк, то есть строка, в которой сначала идут все символы из s,'
                             ' а затем все символы из s2:' + '\n' + 's + s2' + '\n' + 'Строка s, повторенная k раз:' + '\n' +
                             's * k' + '\n' + 'n-й элемент строки, отрицательные n — для отсчета с конца:' + '\n' +
                             's[n]' + '\n' + 'Срез строки:' + '\n' + 's[start:stop:step]' + '\n' +
                             'Длина строки:' + '\n' + 'len(s)' + '\n' + 'Индекс начала первого или последнего вхождения'
                             ' подстроки s2 в s (вернет -1, если s2 not in s):' + '\n' + 's.find(s2)' + '\n' + 's.rfind(s2)' + '\n' +
                             'Количество неперекрывающихся вхождений s2 в s:' + '\n' + 's.count(s2)' + '\n' +
                             'Проверка, что s начинается с s2 или оканчивается на s2:' + '\n' + 's.startswith(s2)' + '\n' +
                             's.endswith(s2)' + '\n' + 'Заменить содержимое строки на s + s2 и s * k соответственно:' + '\n' +
                             's += s2' + '\n' + 's *= k' + '\n' + 'Проверка, что в строке s все символы — цифры, буквы (включая кириллические), '
                             'цифры или буквы соответственно:' + '\n' + 's.isdigit()' + '\n' + 's.isalpha()' + '\n' + 's.isalnum()' + '\n' +
                             'Проверка, что в строке s не встречаются большие буквы, маленькие буквы. Обратите внимание,'
                             ' что для обеих этих функций знаки препинания и цифры дают True:' + '\n' + 's.islower()' + '\n' +
                             's.isupper()' + '\n' + 'Строка s, в которой все буквы (включая кириллические) приведены к верхнему или нижнему регистру, '
                             'т. е. заменены на строчные (маленькие) или заглавные (большие):' + '\n' + 's.lower()' + '\n' + 's.upper()' + '\n' +
                             'Строка s, в которой первая буква — заглавная:' + '\n' + 's.capitalize()' + '\n' + 'Строка s,'
                             'у которой удалены символы пустого пространства (пробелы, табуляции) в начале, в конце или с обеих сторон:' + '\n' +
                             's.lstrip()' + '\n' +  's.rstrip()' +  '\n' + 's.strip()' + '\n' + 'Добавляет справа или слева нужное количество '
                             'символов c, чтобы длина s достигла k:' + '\n' + 's.ljust(k, c)' + '\n' + 's.rjust(k, c)' + '\n' +
                             'Склеивает строки из списка a через символ s:' + '\n' + 's.join(a)' + '\n' + 'Список всех слов строки s'
                             '(подстрок, разделенных строками s2):' + '\n' + 's.split(s2)' + '\n' + 'Cтрока s, в которой все неперекрывающиеся'
                             'вхождения s2 заменены на s3. Есть необязательный третий параметр, с помощью которого можно указать,'
                             'сколько раз производить замену:' + '\n' + 's.replace(s2, s3)' + '\n' + 'Список символов из строки строки s:' + '\n' +
                             'list(s)' + '\n' + 'Проверка, что строка не пустая (возвращает True, если не пустая, и False в противном случае):' + '\n' +
                             'bool(s)' + '\n' + 'Если в строке s записано целое (дробное) число, получить это число, иначе — ошибка:' + '\n' +
                             'int(s)' + '\n' + 'float(s)' + '\n' + 'Представить любой объект x в виде строки:' + '\n' + 'str(x)', reply_markup=markup)

        elif message.text == 'Операции над числами':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                              'Сложение:' + '\n' + 'a + b' + '\n' + 'Вычитание:' + '\n' + 'a - b' + '\n' + 'Умножение:' + '\n' + 'a * b' +
                              'Возведение в степень:' + '\n' + 'a ** b' + '\n' + 'Деление:' + '\n' + 'a / b' + '\n' + 'Целочисленное деление:' + '\n' +
                              'a // b' + '\n' + 'Получение остатка от деления:' + '\n' + 'a % b', reply_markup=markup)

        elif message.text == 'Циклы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Цикл while')
            item2 = types.KeyboardButton('Цикл for')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Циклы'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Цикл while':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Выполняет блок кода, пока истинно какое-то условие.' + '\n' + 'Оператор while («пока»)'
                                              ' проверяет условие и в случае его истинности выполняет следующий блок кода (тело цикла).'
                                              ' Однако после выполнения этого блока кода выполняется не то, что идет после него, '
                                              'а снова проверяется условие, записанное после while.' + '\n' +
                                              'while условие:' + '\n' + '    блок кода (тело цикла)', reply_markup=markup)

        elif message.text == 'Цикл for':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Цикл for выполняет блок кода заданное количество раз.' + '\n' + 'for ... in range(...):' + '\n' + '    блок кода (тело цикла)'
                             'В цикле вида for ... in range(...): вместо первого многоточия указывается какая-то переменная,'
                             ' которая на начальной итерации принимает значение 0, на следующей — 1, и так далее, до значения'
                             ' указанного в range(...), само это значение переменная не принимает. Диапазон значений переменной-итератора'
                             ' от 0 включая и до значения, указанного в range(...), не включая его.' + '\n' +
                             'Range означает «диапазон», то есть for i in range(n) читается как «для (всех) i в диапазоне от 0 (включительно)'
                             ' до n (не включительно)...». Цикл выполняется n раз.', reply_markup=markup)

        elif message.text == 'Множества':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Назад')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             '', reply_markup=markup)


bot.polling(none_stop = True)