import requests


class MyError(Exception):
    def __init__(self, text=''):
        self.text = text


class Product:
    name = 'NO NAME'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name


class Catalog:
    __api_ulr = 'https://5ka.ru/api/v2/special_offers/'
    __headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    def __init__(self):
        self.products = []

    def parse(self):
        url = self.__api_ulr
        while url:
            response = requests.get(url, headers=self.__headers)
            data = response.json()
            url = data.get('next')
            self.products.extend([Product(**itm) for itm in data['results']])


if __name__ == '__main__':
    catalog = Catalog()
    catalog.parse()
    print(1)
