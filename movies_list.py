from bs4 import BeautifulSoup
import requests

# ---------
print("\n")
# ---------

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movie_title_tags = soup.select(".jsx-3821216435.listicle-item img")
# print(len(movie_title_tags))
# print(movie_title_tags[0].get("alt"))

movies_list = []
for tag in movie_title_tags:
    movies_list.append(tag.get("alt"))

count = 100
for movie in movies_list:
    with open("movies_list.txt", "a") as file:
        file.write(f"{count}) {movie}\n")
    count -= 1

print("done writing to file")

# ---------
print("\n")
# ---------
