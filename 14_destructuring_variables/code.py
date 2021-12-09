x, y = 5, 11
print(x, y)

people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for name, age, profession in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
name, _, profession = person # _ ignore/discard value

print(name, profession)  # Bob Mechanic

head, *others = [1, 2, 3, 4, 5]
print(head)  # 1
print(others)  # [2, 3, 4, 5]

*head, last = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(last)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5