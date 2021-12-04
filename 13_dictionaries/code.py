friend_ages = {"Emre": 34, "Hatice": 30, "Arda": 15, "Efe": "-"}
friend_ages["Eymen"] = 10 # doesn't exist in dictionary
friend_ages["Emre"] = 40
print(friend_ages)

friends = [
    {"name": "Emre", "age": 34},
    {"name": "Arda", "age": 15},
    {"name": "Efe", "age": 10},    
]
print(friends[1]["name"])