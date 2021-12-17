def multiply(*args):
    print(args)

multiply(1, 3, 5)


def add(x, y):
    return x+y

nums = {"x": 15, "y": 25}
print(add(**nums)) #  nums["x"], nums["y"]

# -----------
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    else:
        return "unknown operator"

print(apply(1, 3, 6, 7, operator="*"))