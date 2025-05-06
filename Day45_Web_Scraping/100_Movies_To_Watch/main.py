import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL, verify=False)

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

# Find all movie titles
movies = soup.find_all(name="h3", class_="title")

movie_titles = []

for movie in movies:
    title = movie.getText()
    movie_titles.append(title)
    
movie_titles.reverse()    
    
# Create a new file and write the movie titles to it
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")



