moudle6-Dictionaries 
 Module 6 - Dictionaries
student = {"name": "Sophia", "age": 19}

print(student["name"])
student["grade"] = "A"
print(student)

for key, value in student.items():
    print(f"{key}: {value}")
student["course"] = "Data Science"
print(f"{student['name']} is studying {student['course']}")
