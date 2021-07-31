from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")



all_films = soup.findAll(name="div", class_="jsx-4245974604 listicle-item-image")

all_films_str = ''.join(str(elem) for elem in all_films)

all_films_str = BeautifulSoup(all_films_str, "html.parser")

film = all_films_str.findAll("img")

print(all_films)
print(film)

reverse_list_of_move = []
number = 100
for n in range(99):
    reverse_list_of_move.append(f'{number}. {film[n].get("alt")}')
    number -= 1

print(reverse_list_of_move)
# print(all_films.get_text())

# print(film.get("alt"))

