def add_num(x, y):
    result = int(x) + int(y)
    return result
def min_num(x, y):
    result = int(x) - int(y)
    return result
x = input(print("give your x number... "))
y = input(print("give your y number... "))
print(f"the sum of {x} and {y} is {add_num(x, y)}")
print(f"the substraction of {x} and {y} is {min_num(x, y)}")