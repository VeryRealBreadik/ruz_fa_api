from datetime import datetime
import requests


class RuzFaAPI:
    HOST = "https://ruz.fa.ru/"

    def __current_date(self):
        return datetime.now().strftime("%Y.%m.%d")

    def __request(self, sub_url: str):
        response = requests.get(self.HOST + sub_url)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        raise Exception(f"Error, RUZ answered with code: {response.status_code}")
    
    def get_group(self, group_name: str):
        response = self.__request(f"api/search?term={group_name}&type=group")
        print(response)
        return response # TODO: maybe make it so it returns only one, desired group, not all of them (requires filtering)
    
    def get_group_schedule(self, group_name: str, start_date: str = None, end_date: str = None):
        if start_date is None or end_date is None:
            start_date = self.__current_date()
            end_date = start_date
        group = self.get_group(group_name)["id"]
        print(f"www.ruz.fa.ru/api/schedule/group/{group}?start={start_date}&finish={end_date}&lng=1")
        response = self.__request(f"api/schedule/group/{group}?start={start_date}&finish={end_date}&lng=1")
        return response # TODO: return less information, remove useless info