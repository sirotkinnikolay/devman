import requests

site_url = "http://wttr.in//"

locations = [
    'London?n?M?qTqu&lang=ru',
    'svo?n?M?qTqu&lang=ru',
    'Череповец?n?M?qTqu&lang=ru'
]


def script(urls, site):
    for url in urls:
        try:
            response = requests.get(f'{site}{url}')
            if response.ok:
                print(response.text)
                print('-' * 63)
            else:
                return None
        except requests.exceptions.ConnectionError as connect:
            print(connect)
            break


if __name__ == '__main__':
    script(locations, site_url)
