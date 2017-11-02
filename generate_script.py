f = open("./output.json")
s= f.read()
import json
root = json.loads(s)
movies = root['Top250Movies']
for movie in movies:
    print(movie['title'])
