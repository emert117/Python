numbers = [1, 3, 5]
doubled = []
new_doubled = [num * 2 for num in numbers] # a cool way

for num in numbers:
    doubled.append(num *2)

print(doubled)
print(new_doubled)

friends = ["Rolf", "Sam", "Samantha", "Jen"]
starts_with_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_with_s.append(friend)

print(starts_with_s)

new_starts_with_s = [friend for friend in friends if friend.startswith("S")] # a cool way - list comprehension
print(new_starts_with_s)

print("friends:", id(friends), "starts_wtih_S:", id(starts_with_s)) # id -> memory address