# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

def named(name, age):
    print(name, age)

details = {"name":"Bob", "age":25}
named(**details)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="emre", surname="mert")