from statistics import mean
import os
import datetime

def time_to_num(time): # Используется в расчётё 1, 2
    if ':' in time:
        arr = time.split(':')
        return round(int(arr[0]) + int(arr[1]) / 60, 2)
    else:
        return round(int(time), 2)

def num_to_time(num): # Используется в расчётё 1, 2
    hours = int(num // 1)
    mins = int(num % 1 * 60)
    if mins == 0:
        return str(hours) + ':' + '00'
    else:
        return str(hours) + ':' + str(mins)

def diff_time(tup):   # Используется в расчете 2
    num1 = time_to_num(tup[0]) + 24
    num2 = time_to_num(tup[1])
    if 0 <= num2 <= 12:
        num2 += 24
    return num1 - num2


def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        return [i.strip() for i in content]

def read_md_data(start_date, n, folder_path):
    global _start_date_native, _start_date_obj, _end_date_obj, year, month, day, data_dict
    n = int(n)
    result = {'sleep_down': [], 'sleep_up': [], 'sleep_time': [], 'food_morn': [], 'food_even': []}    
    
    if datetime.datetime.strptime(start_date, "%Y-%m-%d").date() < datetime.datetime.strptime('2023-09-26', "%Y-%m-%d").date():
        start_date = '2023-09-26'
    # Парсим datetime object из переданной строки start_date
    _start_date_native = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    _start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    _end_date_obj = _start_date_obj + datetime.timedelta(days=n)
    
    # переменная для подсчёта сколько дней было считано
    count = 0
    
    # Считываем контент прошлого дня перед первой датой и вытягиваем оттуда вечерний приём пищи
    # Вместо этой херни плохоработающей нужно реализовать просто парсин datetme object в str yyyy-mm-dd. вот и всё!
    _first_date_one_day_before = f'{_start_date_native.year}-{_start_date_native.month if _start_date_native.month >= 10 else "0" + str(_start_date_native.month)}-{_start_date_native.day - 1 if _start_date_native.day >= 11 else "0" + str(_start_date_native.day - 1)}.md'
    print(_first_date_one_day_before)
    markdown_content = read_markdown_file(os.path.join(folder_path, _first_date_one_day_before))
    for row in markdown_content:
        if row == '*ПРИМЕМЫ ПИЩИ:*':
            result['food_even'].append(markdown_content[markdown_content.index(row) + 2])
        
    # основной алгоритм считывания данных
    for filename in os.listdir(folder_path):
        file_date_obj = datetime.datetime.strptime(filename[:10], "%Y-%m-%d").date()
        if _start_date_native <= file_date_obj < _end_date_obj:
            count += 1
            file_path = os.path.join(folder_path, filename)
            markdown_content = read_markdown_file(file_path)
            for row in markdown_content:
                if row.startswith('Уснул --- '):
                    result['sleep_down'].append(row[10:])
                if row.startswith('Проснулся --- '):
                    result['sleep_up'].append(row[14:])
                if row.startswith('Спал --- '):
                    result['sleep_time'].append(row[9:])
                if row == '*ПРИМЕМЫ ПИЩИ:*':
                    result['food_morn'].append(markdown_content[markdown_content.index(row) + 1])
                    result['food_even'].append(markdown_content[markdown_content.index(row) + 2])
                    
    print(f'\nСчитана информация за период {_start_date_native.year}-{_start_date_native.month}-{_start_date_native.day} -- {_end_date_obj.year}-{_end_date_obj.month}-{_end_date_obj.day}')
    print(f'\n\n было считано {count}/{n} дней')
    return result

print('-----------------------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('Привет! Я скрипт для работы с DailyNote`ами Obsidian \n')
ans = None
data = None
folder_path = 'C://obsidian_vaults//DAILY RITUALS//daily notes//'
_start_date_native, _start_date_obj, _end_date_obj, year, month, day, data_dict = None, None, None, None, None, None, None

while ans != "0":
    
    print('Папка, в которой происходит поиск DailyNote-заметок по умолчанию:\nC://obsidian_vaults//DAILY RITUALS//daily notes//\n')

    ans = input('''Вы в основном меню!
    \t1 --- автоматически считать данные
    \t2 --- рассчитать все параметры автоматически
    \t3 --- показать данные
    \t4 --- в меню отрисовки графиков ->
    \t5 --- инструкция
    \t6 --- Изменить папку 
    \t0 --- Закончить работу
    Ваш ответ: ''')

    if ans == '1':
        print('-----------------------------------------------------------------')
        # сделать здесь некоторый луп для считывания и исправления инфы
        data = read_md_data(input("Введи название DailyNote в формате ГГГГ-ММ-ДД: "), input('Сколько дней считываем: '), folder_path)
        print('-----------------------------------------------------------------')
        continue

            
    elif ans == '2':
        if data:
            tmp = []
            sleep_time = num_to_time(mean(map(time_to_num, data['sleep_time'])))
            sleep_down = num_to_time(mean(map(lambda x: time_to_num(x) if time_to_num(x) > 12 else time_to_num(x) + 24, data['sleep_down'])))
            sleep_up = num_to_time(mean(map(time_to_num, data['sleep_up'])))
            
            for i in zip(data['food_morn'], data['food_even']):
                tmp.append(i)

            food_pause = num_to_time(mean(map(diff_time, tmp)))
            
            avg_morn_meal = num_to_time(mean(map(time_to_num, data['food_morn'])))
            avg_even_meal = num_to_time(mean(map(time_to_num, data['food_even'])))
            print('-----------------------------------------------------------------')
            print(f"Среднее время сна: {sleep_time}\nСреднее время засыпания: {sleep_down}\nСреднее время подъема: {sleep_up}")
            print(f"\nСредняя пищевая пауза: {food_pause}")
            print(f'\nСреднее время завтрака: {avg_morn_meal}')
            print(f'\nСреднее время ужина: {avg_even_meal}')
            print('-----------------------------------------------------------------')
            tmp = 0
            
            
        else:
            print('Данные ещё не считаны!\n')
            
    elif ans == '3':
        if data:
            print('-----------------------------------------------------------------')
            for key, value in data.items():
                print(key, " : ", value)
            print('-----------------------------------------------------------------')
        else:
            print('Данные ещё не считаны!\n')
            
    elif ans == '4':
        ans2 = None
        if data:
            import matplotlib.pyplot as plt
            import seaborn as sns
            sns.set_style(style="dark")
            
            while ans2 != '0':
                print('-----------------------------------------------------------------')
                ans2 = input('Вы в меню отрисовки графиков!\n\t1 --- График времени сна ("Спал --- ")\n\t2 --- График времени подьъема, засыпания\n\t3 --- инструкция\n\t0 --- Назад\n\t')
                print('-----------------------------------------------------------------')
                if ans2 == '1': # 1 --- График времени сна ("Спал --- ")
                    current_date = _start_date_native
                    s_t_temp = data['sleep_time']
                    x = []
                    y = []
                    
                    while current_date < _end_date_obj:
                        x.append(current_date)
                        y.append(time_to_num(s_t_temp.pop(0)))
                        current_date += datetime.timedelta(days=1)

                    # Создание графика с помощью seaborn
                    plt.figure(figsize=(8, 8))
                    sns.lineplot(x=x, y=y, marker='o')

                    # Настройка осей и заголовка
                    plt.xlabel('Дата')
                    plt.ylabel('Время сна')
                    plt.title('График времени сна')
                    plt.xticks(rotation=45)
                    plt.grid(True)
                    plt.ylim(6, 12.5)
                    
                    sns.despine()

                    plt.show()
                
                if ans2 == '2': # 2 --- График времени подьъема, засыпания
                    current_date = _start_date_native
                    s_u_temp = data['sleep_up']
                    s_d_temp = data['sleep_down']
                    x = []
                    y1 = []
                    y2 = []
                    
                    
                    while current_date < _end_date_obj:
                        x.append(current_date)
                        y1.append(time_to_num(s_u_temp.pop(0)))
                        s_d_time_temp = s_d_temp.pop(0)
                        if time_to_num(s_d_time_temp) < 8:
                            y2.append(time_to_num(s_d_time_temp) + 24)
                        else:
                            y2.append(time_to_num(s_d_time_temp))
                        
                        current_date += datetime.timedelta(days=1)

                    # Создание графика с помощью seaborn
                    plt.figure(figsize=(12, 6))
                    sns.lineplot(x=x, y=y1, label='Sleep Up')
                    sns.lineplot(x=x, y=y2, label='Sleep Down')
                    
                    # Настройка осей и заголовка
                    plt.xlabel('Дата')
                    plt.ylabel('Время сна')
                    plt.title('График времени сна')
                    plt.xticks(rotation=45)
                    plt.grid(True)
                    #plt.ylim(6, 12.5)
                    
                    sns.despine()

                    plt.show()
        else:
            print('Данные ещё не считаны!\n')
    
    
    
    elif ans == '5':
        print('-----------------------------------------------------------------')
        print('''
        Инструкция и напоминания:
        - Нельзя переименовывать строчки "Уснул --- ", "Проснулся --- ", "Спал --- ", "ПРИМЕМЫ ПИЩИ:"
        - Нельзя добавлять лишние пробелы, а также не ставить проблемы после "---"
        - После строчки "ПРИМЕМЫ ПИЩИ:" обязаны идти 2 строки: время завтрака и время ужина
        ''')
        print('-----------------------------------------------------------------')
    
    elif ans == '6':
        print('-----------------------------------------------------------------\n\n')
        folder_path = input('Введите директорию в таком виде C://x//x//x:\n')
        print('\n-----------------------------------------------------------------')
 














 
    elif ans == '_1': # среднее время по значениям

        if data is None:
            print('Данные не считаны, включен ручной ввод данных\n')
            for i in range(int(input("Введите количество дней:\n"))):
                l.append(input(f'Введите значение времени № {i + 1}:\n'))

            l = map(time_to_num, l)
            tim = num_to_time(mean(l))

            print('Your time:', tim, '\n')
            l = []
            tim = 0
    elif ans == '_2':           

        for i in range(int(input("Введите количество дней:\n"))):
            l.append((input(f'Введите время завтрака:\n'), input(f'Введите время ужина прошлого дня:\n')))

        l = map(diff_time, l)
        tim = num_to_time(mean(l))

        print('Your time:', tim, '\n')
        
        l = []
        tim = 0
        # чел будет вводить время завтрака и время ужина поочередно. Мы высчитываем разницу. Потом берем среднюю разниц
        
    elif ans == '_3':
        data = read_md_data(input("Введи название Daily note в формате ГГГГ-ММ-ДД: "), input('Сколько дней считываем: '), folder_path)