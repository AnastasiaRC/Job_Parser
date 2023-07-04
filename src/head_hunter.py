import requests
from src.api_requests import ApiRequests


class HeadHunterAPI(ApiRequests):

    def get_format_vacancies(self):
        format_vacancies = []
        for vacanci in self.get_request()[0]['items']:
            if not vacanci['salary'] or not vacanci['salary']['currency']:
                format_vacancies.append({
                    "name": vacanci['name'],                          # название
                    "experience": vacanci['experience']['name'],      # опыт
                    "employment": vacanci['employment']['name'],      # занятость
                    "area": vacanci['area']['name'],                  # город
                    "salary_from": 0,                                 # зп от
                    "salary_to": 0,                                   # зп до
                    "currency": 'не указано',                         # валюта
                    "responsibility": vacanci['snippet']['requirement'],  # обязанности
                    "url": vacanci['url']                             # ссылка
                })
            else:
                format_vacancies.append({
                    "name": vacanci['name'],                        # название ['items'][0]
                    "experience": vacanci['experience']['name'],    # опыт
                    "employment": vacanci['employment']['name'],    # занятость
                    "area": vacanci['area']['name'],                # город
                    "salary_from": vacanci['salary']['from'],       # зп от
                    "salary_to": vacanci['salary']['to'],           # зп до
                    "currency": vacanci['salary']['currency'],      # валюта
                    "responsibility": vacanci['snippet']['requirement'],  # обязанности
                    "url": vacanci['url']                           # ссылка
                })
        return format_vacancies

    def get_request(self, keyword='python'):
        response = []
        for page in range(10):
            url = 'https://api.hh.ru/vacancies/'
            params = {
                'per_page': 2,
                'page': page,
                'keyword': keyword,
                'archive': False,
            }
            response.append(requests.get(url, params=params).json())
        return response



