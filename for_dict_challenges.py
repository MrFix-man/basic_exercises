# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 12
# Маша: 2
# Петя: 2

def lesson_1(students_1, dupl):
    for name_1 in students_1:
        dupl.append(name_1['first_name'])

    res = {i: dupl.count(i) for i in dupl}

    return res


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
# ???


def lesson_2(students_2, key):
    tmp = []
    dp = []

    for name_2 in students_2:
        if name_2[key] not in tmp:
            tmp.append(name_2[key])
        else:
            dp.append(name_2[key])
    return dp


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
# ???


def lesson_3(shool_students, key):
    tmp = []
    dp = []
    cnt = 0
    for cl in shool_students:
        cnt += 1
        for stud in cl:
            if stud[key] not in tmp:
                tmp.append(stud[key])
            else:
                dp.append(stud[key])
    return dp


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2
# ???

def lesson_4(school_4, is_male_4):
    cl_names = {}
    full_male = []
    for i in school_4:
        names = []
        for j in i['students']:
            names.append(j.get('first_name'))
        cl_names[i.get('class')] = names

    for k, v in cl_names.items():
        cnt_ml = 0
        cnt_fm = 0
        cnt_sh_male = []
        for name in v:
            if not is_male_4.get(name):
                cnt_fm += 1
            else:
                cnt_ml += 1
        cnt_sh_male.append(f'Класс {k}: девочки {cnt_fm}, мальчики {cnt_ml}')
        full_male.append(cnt_sh_male)
    return full_male


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


def lesson_5(school_5, is_male_5):
    cl_names = {}
    full_male = []
    for i in school_5:
        names = []
        for j in i['students']:
            names.append(j.get('first_name'))
        cl_names[i.get('class')] = names

    for k, v in cl_names.items():
        cnt_ml = 0
        cnt_fm = 0
        cnt_sh_male = []
        for name in v:
            if not is_male_5.get(name):
                cnt_fm += 1
            else:
                cnt_ml += 1
        if cnt_fm > cnt_ml:
            cnt_sh_male.append(f'Больше девочек в классе {k}')
        else:
            cnt_sh_male.append(f'Больше мальчиков в классе {k}')
        full_male.append(cnt_sh_male)
    return full_male


def main():
    students_1 = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
    ]
    print('Задание 1')
    for i in lesson_1(students_1, []):
        print(f"{i}: {lesson_1(students_1, [])[i]}")

    students_2 = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
    print('\nЗадание 2')
    print(*lesson_2(students_2, 'first_name'))

    school_students = [
        [  # это – первый класс
            {'first_name': 'Вася'},
            {'first_name': 'Вася'},
        ],
        [  # это – второй класс
            {'first_name': 'Маша'},
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ], [  # это – третий класс
            {'first_name': 'Женя'},
            {'first_name': 'Петя'},
            {'first_name': 'Женя'},
            {'first_name': 'Саша'},
        ],
    ]

    print('\nЗадание 3')

    for i in range(len(school_students)):
        print(f"Самое частое имя в классе {i + 1}: {lesson_3(school_students, 'first_name')[i]}")

    print("\nЗадание 4")

    school_4 = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
        {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
    ]
    is_male_4 = {
        'Олег': True,
        'Маша': False,
        'Оля': False,
        'Миша': True,
        'Даша': False,
    }

    for male in lesson_4(school_4, is_male_4):
        print(*male)

    print("\nЗадание 5")

    school_5 = [
        {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    ]
    is_male_5 = {
        'Маша': False,
        'Оля': False,
        'Олег': True,
        'Миша': True,
    }

    for male in lesson_5(school_5, is_male_5):
        print(*male)


if __name__ == '__main__':
    main()
