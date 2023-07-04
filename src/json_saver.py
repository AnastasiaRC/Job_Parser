import json
import os
from operator import itemgetter
from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename, vacancies):
        self.filename = filename
        self.creat_file(vacancies)

    def creat_file(self, vacancies):
        """ Создает файл сразу с созданием экземпляра с названием которое введет пользователь для поиска вакансий"""
        with open(f'{os.getcwd()}/data/{self.filename}.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)

    def get_all(self):
        """ Обрабатывает данные файла и оборачивает в класс Vacansy"""
        with open(f'{os.getcwd()}/data/{self.filename}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return self.wraps_in_class_vacancy(data)

    def wraps_in_class_vacancy(self, data):
        """Оборачивает список в класс Vacancy"""
        class_data = []
        for element in data:
            class_data.append(Vacancy(element))
        return class_data

    def sorted_by_salary_up(self):
        """Сортирует вакансии по ЗП (по убыванию) и выводит в str виде класса Vacancy"""
        vacancy_data = self.get_all()
        sorted_data = []
        for element in vacancy_data:
            sorted_data.append(element.__dict__)
        sorted_data.sort(key=itemgetter('salary_from'), reverse=True)
        return self.wraps_in_class_vacancy(sorted_data)

    def sorted_by_salary_down(self):
        """Сортирует вакансии по ЗП (по возрастанию) и выводит в str виде класса Vacancy"""
        vacancy_data = self.get_all()
        sorted_data = []
        for element in vacancy_data:
            sorted_data.append(element.__dict__)
        sorted_data.sort(key=itemgetter('salary_from'))
        return self.wraps_in_class_vacancy(sorted_data)

    def sorted_by_area(self, user_word):
        """Сортирует вакансии по региону веденному пользователем и выводит в str виде класса Vacancy"""
        vacancy_data = self.get_all()
        sorted_data = []
        for element in vacancy_data:
            sorted_data.append(element.__dict__)
        new_list = []
        for element in sorted_data:
            if user_word.lower() == element["area"].lower():
                new_list.append(element)
        return self.wraps_in_class_vacancy(new_list)

    def sorted_by_employment(self, user_word):
        """Сортирует вакансии по занятости веденной пользователем и выводит в str виде класса Vacancy"""
        vacancy_data = self.get_all()
        sorted_data = []
        for element in vacancy_data:
            sorted_data.append(element.__dict__)
        new_list = []
        for element in sorted_data:
            if user_word.lower() == element["employment"].lower():
                new_list.append(element)
        return self.wraps_in_class_vacancy(new_list)

    def add_list_in_file(self, sorted_list):
        """
        Обрабатывает файл и сохраняет его содержимое в список, (переводит передаваемый список класса в словарь)
        добавляет передаваемый список к списку с содержимым в файле, открывает файл на запись и переводит все данные
        в json фармат и сохраняет в файле
        """
        with open(f'{os.getcwd()}/data/{self.filename}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for x in sorted_list:
                data.append(x.__dict__)
        with open(f'{os.getcwd()}/data/{self.filename}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def clear_file(self):
        """Очищает содержимое файла"""
        with open(f'{os.getcwd()}/data/{self.filename}.json', 'w', encoding='utf-8') as f:
            pass

    def sorted_by_salary_user(self, user_word):
        """
        Сортирует вакансии по нижней границе ЗП веденной пользователем (по убыванию) и выводит в
        str виде класса Vacancy
        """
        vacancy_data = self.get_all()
        sorted_data = []
        for element in vacancy_data:
            sorted_data.append(element.__dict__)
        sorted_data.sort(key=itemgetter('salary_from'), reverse=True)
        new_list = []
        for row in sorted_data:
            if row['salary_from'] >= user_word:
                new_list.append(row)
        return self.wraps_in_class_vacancy(new_list)





