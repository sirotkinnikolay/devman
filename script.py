import requests

site = "https://wttr.in//"

urls = [
    'London?n?M?qTqu&lang=ru',
    'svo?n?M?qTqu&lang=ru',
    'Череповец?n?M?qTqu&lang=ru'
        ]
for url in urls:
    response = requests.get(f'{site}{url}')
    print(response.text)
    print('-' * 63)
