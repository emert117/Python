from lib2to3.pytree import Base


def divide(dividend, divisor):
    raise BaseException("I am bored")
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0 (zero)")

    return dividend / divisor

grades = []
try:
    average = divide(sum(grades) / len(grades))
except ZeroDivisionError as e:
    print("There are no grades in your list")
except BaseException as e:
    print(f"Unknown error", e)
else:
    print(f"The average is {average}") # run if there ia no errors
finally:
    print("The end") # always runs

