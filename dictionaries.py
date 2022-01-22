'''students={
    "sno":12345,
    "sname":"ram",
    "age":24,
    "address":"vizag"
}
print(students)
print(students["sname"])'''

d={
  "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}
print(d.items())
print(d.keys())
print(d.values())
d["price"]=1200000
print(d)
d["price"]=800000
print(d)

d.pop("price")
print(d)