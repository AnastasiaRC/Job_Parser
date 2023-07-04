from src.head_hunter import HeadHunterAPI
from src.json_saver import JSONSaver
from src.super_job import SuperJobAPI


def user_interaction():

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    keyword = input('Введите слово для поиска: ')

    vacancies = []
    for row in (hh_api, superjob_api):
        vacancies.extend(row.get_format_vacancies())
    json_saver = JSONSaver(keyword, vacancies)

    while True:
        num = input('''Введите цифру действия:
        (все вакансии сохраняются в файл)
        1. Вывести все
        2. Отсортировать ЗП от (по убыванию)
        3. Отсортировать ЗП от (по возрастанию)
        4. Отсортировать ЗП от веденной суммы
        5. Отсортировать по месту нахождения работы
        6. Отсортировать по занятости
        7. Очистить файл
        8. Выход\n''')
        if not num in '12345678':
            print('Выберите цифру от 1 до 8')
            continue
        else:
            if num == '1':
                user_vacancies = json_saver.get_all()
                for row in user_vacancies:
                    print(row)
            elif num == '2':
                user_vacancies = json_saver.sorted_by_salary_up()
                json_saver.add_list_in_file(user_vacancies)
                for row in user_vacancies:
                    print(row)
            elif num == '3':
                user_vacancies = json_saver.sorted_by_salary_down()
                json_saver.add_list_in_file(user_vacancies)
                for row in user_vacancies:
                    print(row)
            elif num == '4':
                user_input = int(input('Ведите сумму нижней границы ЗП (по убыванию):\n'))
                if 5000 <= user_input <= 900000:
                    user_vacancies = json_saver.sorted_by_salary_user(user_input)
                    json_saver.add_list_in_file(user_vacancies)
                    if not user_vacancies:
                        print('Подходящих вакансий не найдено')
                        continue
                    else:
                        for row in user_vacancies:
                            print(row)
                else:
                    print('Сумма указана не корректно (пример: 15000, 20000)')
                    continue
            elif num == '5':
                user_input = input('Ведите регион:\n')
                result = json_saver.sorted_by_area(user_input)
                if not result:
                    print('Такой регион не найден')
                    continue
                else:
                    json_saver.add_list_in_file(result)
                    for row in result:
                        print(row)
            elif num == '6':
                user_input = input('''Выберите цифру с необходимым типом занятости:
                1. Полная занятость
                2. Частичная занятость
                3. Проектная работа\n''')
                if not user_input in '123':
                    print('Выберите цифру от 1 до 3')
                    continue
                else:
                    d = {'1': "Полная занятость", '2': 'Частичная занятость', '3': 'Проектная работа'}
                    word = d[user_input]
                    result = json_saver.sorted_by_employment(word)
                    if not result:
                        print('Вакансий с такой занятостью не найдено')
                        continue
                    else:
                        for row in result:
                            print(row)
            elif num == '7':
                json_saver.clear_file()
            elif num == '8':
                 break


if __name__ == "__main__":
    user_interaction()
