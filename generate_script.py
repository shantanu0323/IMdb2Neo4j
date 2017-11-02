f = open("./output.json")
s= f.read()
import json
root = json.loads(s)
file = open("./script1.txt", "w")

movies = root['Top250Movies']

for movie in movies:

    # print("CREATE (RMD:TEAM {title:'Real Madrid', stadium:'Santiago Bernabeu'})")

    for actor in movie['actors']:

        file.write("MERGE (:MOVIE {title:'" + str(actor['name']).replace("'","-") + "'})\n")
