def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0 (zero)")

    return dividend / divisor

grades = []
try:
    average = divide(sum(grades) / len(grades))
    print(f"The average is {average}")
except ZeroDivisionError as e:
    print("There are no grades in your list")
