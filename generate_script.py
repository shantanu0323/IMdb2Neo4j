f = open("./cast.json")
s= f.read()
import json
root = json.loads(s)
file = open("./script1.txt", "w")

movies = root['Movies']

for movie in movies:

    # print("CREATE (RMD:TEAM {title:'Real Madrid', stadium:'Santiago Bernabeu'})")

    for actor in movie['actors']:

        file.write("MERGE (:ACTOR {title:'" + str(actor['name']).replace("'","-") + "'})\n")
