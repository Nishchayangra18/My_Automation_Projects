import json

courses = '{"name": "Nishchay Angra", "language": ["Java", "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses['name'])

# Get me the first language

print(dict_courses['language'][0])


# ************* Parse content present in json file *********************

with open('C:\\Users\\Nishchay\\Downloads\\students.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    # ************** Print subject 1 of Student 1 ****************************
    print(data['students']['student1']['subjects'][1]['name'])
    for subjects in data['students']['student1']['subjects']:
        # print(subjects)
        if subjects['name'] == "Physics":
            print(subjects['grade'])

