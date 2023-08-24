with open("my_math2.py", "w") as f:
    f.writelines(
        """def my_pow(x, y):
    return x ** y
if __name__ == " __main__":
    x, y, exp = 2, 5, 32
    ans = my_pow(x, y)
    print("Teat my_pow({},{}) -> {}, exp: {} ---- ".format(x, y, ans,exp),end="")
    if nas == exp:
        print("Test OK")
    else:
    print("Test Fail")\n"""
    )

import my_math2

my_math2.my_pow(2, 5)
