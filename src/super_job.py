import time
import requests
from src.api_requests import ApiRequests


class SuperJobAPI(ApiRequests):

    def get_format_vacancies(self):
        format_vacancies = []
        for vacancy in self.get_request()[0]['objects']:
            format_vacancies.append({
                "name": vacancy["profession"],                    # название
                "experience": vacancy["experience"]["title"],     # опыт
                "employment": vacancy["type_of_work"]["title"],   # занятость
                "area": vacancy["client"]["town"]["title"],       # город
                "salary_from": vacancy['payment_from'],           # зп от
                "salary_to": vacancy['payment_to'],               # зп до
                "currency": vacancy['currency'],                  # валюта
                "responsibility": vacancy["candidat"],            # обязанности
                "url": vacancy["link"]                            # ссылка
            })
        return format_vacancies

    def get_request(self, keyword='python'):
        response = []
        for page in range(10):
            time.sleep(1)
            url = 'https://api.superjob.ru/2.0/vacancies/'
            params = {
                'count': 2,
                'page': page,
                'keyword': keyword,
                'archive': False,
            }
            headers = {'X-Api-App-Id': 'v3.r.137651211.a699c64b0c6371cdb2d419242538e6e4c683aee4.bef7a264a839dd059470f10bf1c142769d61c385'}
            response.append(requests.get(url, headers=headers, params=params).json())
        return response


