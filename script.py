import requests

urls = ['https://wttr.in//London?n?M?qTqu&lang=ru', 'https://wttr.in//svo?n?M?qTqu&lang=ru',
        'https://wttr.in//Череповец?n?M?qTqu&lang=ru'
        ]
for url in urls:
    response = requests.get(url)
    print(response.text)
    print('-' * 63)
