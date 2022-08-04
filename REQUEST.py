import json
import requests

def request(url):
    resp=requests.get(url)
    return resp.json()
url=("https://saral.navgurukul.org/api/courses")
response=requests.get(url)
course=json.loads(response.text)
print(course)

id_list=[]
for i in range(len(course["availableCourses"])):
    course_id=course["availableCourses"][i]["id"]
    course_name=course["availableCourses"][i]["name"]
    print(i," ",course_id,course_name)
    id_list.append(course_id)
num=int(input('ENTER THE NUMBER ='))
print("index name : ",course["availableCourses"][num]["name"])
chalection=course["availableCourses"][num]["id"]
print(chalection)
exercise_json = request("http://saral.navgurukul.org/api/courses/"+chalection+"/exercises")
slug_list = []
for j in range(len(exercise_json["data"])):
    exercise =exercise_json["data"][j]
    exercisename=exercise["name"]
    print(exercisename)
    parent_exercise=exercise["parent_exercise_id"]
    if parent_exercise==None:
        exercise_name=exercise["name"]
        exercise_slug=exercise["slug"]
        slug_list.append(exercise_slug)
        print (str(j)+ ". " + exercise_name)
    elif parent_exercise!=None:
        exercise_name=exercise["name"]
        exercise_slug=exercise["slug"]
        slug_list.append(exercise_slug)
        print ("parentexercises",str(index_1)+ ". " + exercise_name)
