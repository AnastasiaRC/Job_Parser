class Vacancy:
    def __init__(self, vacancies):
        self.name = vacancies["name"]
        self.experience = vacancies["experience"]
        self.employment = vacancies["employment"]
        self.area = vacancies["area"]
        self.salary_from = vacancies["salary_from"]
        self.salary_to = vacancies["salary_to"]
        self.currency = vacancies["currency"]
        self.responsibility = vacancies["responsibility"]
        self.url = vacancies["url"]

    def __gt__(self, other):
        return self.salary_from > other.selary_from

    def __str__(self):
        if self.salary_from is None:
            self.salary_from = 0
        if self.salary_to is None:
            self.salary_to = 0
        if self.responsibility is None:
            self.responsibility = "не указано"
        return f"""
        Название вакансии: {self.name}
        Место нахождения: {self.area}
        Требуемый опыт: {self.experience}
        Занятость: {self.employment}
        Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}
        Описание: {self.responsibility[:50]}...
        Ссылка: {self.url}   
        """

