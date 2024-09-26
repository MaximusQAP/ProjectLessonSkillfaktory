import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Удалить оценку ученика по предмету
        3. Редактировать оценку ученика по предмету
        4. Вывести информацию по всем оценкам для определенного ученика
        5. Вывести средний балл по каждому предмету по определенному ученику
        6. Вывести средний балл по всем предметам по каждому ученику
        7. Вывести все оценки по всем ученикам
        8. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')


    elif command == 2:
        print('2. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            print(students_marks[student])
        else:
            print('Этого ученика в списке нет')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            print(students_marks[student][class_])
        else:
            print('Этого предмета в списке нет')
        end_mark=int(input('Введите оценку, которую хотите удалить: '))
        if end_mark in (students_marks[student][class_]):
            (students_marks[student][class_]).remove(end_mark)
            print(students_marks[student])
        else:
            print('Этой оценки в списке нет')


    elif command == 3:
        print('3. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            print(students_marks[student])
        else:
            print('Этого ученика в списке нет')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            print(students_marks[student][class_])
        else:
            print('Этого предмета в списке нет')
        end_mark = int(input('Введите оценку, которую хотите редактировать: '))
        if end_mark in (students_marks[student][class_]):
            (students_marks[student][class_]).remove(end_mark)
            print(students_marks[student])
        else:
            print('Этой оценки в списке нет')
        mark = int(input('Введите оценку на которую хотите заменить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')


    elif command == 4:
        print('4. Вывести информацию по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        for class_ in classes:
            print(f'\t {class_} - {students_marks[student][class_]}')


    elif command == 5:
        print('5. Вывести средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for class_, marks in students_marks[student].items():
                marks_sum = sum(marks)
                marks_count = len(marks)
                print(f'{class_} - {marks_sum // marks_count}')

    elif command == 6:
        print('7. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 7:
        print('8. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 8:
        print('9. Выход из программы')
        break