#hello() # doesn't run

def hello():
    print("hello")

hello()

def do_nothing():
    pass

def add(x, y):
    result = x + y
    print(result)
    return result

add(3, 5)

def say_hello(name, surname):
    print(f"hello {name} {surname}")

say_hello(surname="mert", name="emre")
