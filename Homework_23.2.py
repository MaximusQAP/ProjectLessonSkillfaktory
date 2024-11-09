import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []


url = f'https://www.ivi.ru/movies/boeviki'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

entries = soup.find_all('li', class_='gallery__item gallery__item_virtual')

for entry in entries:
    film_details = entry.find('div', class_='nbl-slimPosterBlock__title')
    film_name = film_details.find('span').text
    rating = entry.find('div', class_='nbl-ratingCompact__valueInteger').text
    info_about_films = entry.find('div', class_='nbl-poster__propertiesInfo').text

    data.append({'Название фильма' : film_name, 'Рейтинг': rating, 'Информация о фильме': info_about_films})

    if len(entries) == 0:
        break


df = pd.DataFrame(data, columns=['Название фильма', 'Рейтинг', 'Информация о фильме'])
df.to_excel('data_Homework_23.xlsx')

print(data)
print(len(entries))
print()