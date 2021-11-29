user_input = input("EWould you like to play? (Y/n) ")

while user_input != "n":
    print("Hello stranger")
    user_input = input("EWould you like to play? (Y/n) ")

fruits = ["apple", "banana", "grape"]

for fruit in fruits:
    print(f"{fruit} is delicious")

for i in range(4):
    print(f"{i}n")

for i in range(10):
    for j in range(i):
        print("*" * j)