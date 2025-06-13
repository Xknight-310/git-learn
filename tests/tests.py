import calculator as c
def test_add_num():
    print("Testing add_num...")
    x, y = 2313, 5435
    add_result = c.add_num(x, y)
    if add_result == (x+y):
        print("add_num passed test")
    else : print(f"add_num failed test! \nOutput: {add_result}")
def test_min_num():
    print("Testing min_num...")
    x, y = 2313, 5435
    min_result = c.min_num(x, y)
    if min_result == (x-y):
        print("add_num passed test")
    else : print(f"add_num failed test \nOutput: {min_result}")

test_add_num()
test_min_num