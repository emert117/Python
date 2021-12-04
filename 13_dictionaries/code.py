friend_ages = {"Emre": 34, "Hatice": 30, "Arda": 15, "Efe": "-"}
friend_ages["Eymen"] = 10 # doesn't exist in dictionary
friend_ages["Emre"] = 40
print(friend_ages)
for friend in friend_ages:
    print(f"{friend}: {friend_ages[friend]}") # key access

for name, age in friend_ages.items(): # destructing
    print(f"{name}: age: {age}")

friends = [
    {"name": "Emre", "age": 34},
    {"name": "Arda", "age": 15},
    {"name": "Efe", "age": 10},    
]
print(friends[1]["name"])

# in keyword 