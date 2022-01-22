student={
    "sno":123,
    "sname":"ram",
    "age":24,
    "marks":98

}
'''print(student)
student["address"]="vizag"
print(student)
print(student.items())
print(student.keys())
print(student.values())
student["marks"]=99
print(student)
student["mobile no"]=9495894598
print(student)

x=student.pop("mobile no")
print(x)
print(student)

del student["address"]
print(student)

cars={
    "brand":"ford",
    "model":"mustang",
    "year":1964

}
print(cars)'''
print(student["age"])

