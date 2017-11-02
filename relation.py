f = open("./cast.json")
s= f.read()
import json
root = json.loads(s)
file = open("./script2.txt", "w")

movies = root['Movies']

for movie in movies:

    # print("CREATE (RMD:TEAM {title:'Real Madrid', stadium:'Santiago Bernabeu'})")

    for actor in movie['actors']:
        #file.write("MERGE (:ACTOR {title:'" + str(actor['name']).replace("'","-") + "'})\n")
        print("MATCH (actor:ACTOR {title:'"+  str(actor['name']).replace("'","-") + "'}),(movie:MOVIE {title:'" + str(movie['title']).replace("'","-") + "'})")
        print("MERGE (actor)-[r:ACTED_IN]->(movie)")
# MATCH (charlie:Person { name: 'Charlie Sheen' }),(wallStreet:Movie { title: 'Wall Street' })
# MERGE (charlie)-[r:ACTED_IN]->(wallStreet)
