f = open("./cast.json")
s= f.read()
import json

file = open("./script.txt", "w")

root = json.loads(s)
movies = root['Movies']
for movie in movies:
    # print("CREATE (RMD:TEAM {title:'Real Madrid', stadium:'Santiago Bernabeu'})")
    file.write("CREATE (:MOVIE {title:'" + str(movie['title']).replace("'","-") + "'})\n")
    for actor in movie['actors']:
        print(actor['name'])
    print('***********************')
    print()