# no args
def say_hello():
    print("Hello from a function")


# with args
def say_hello_custom(name):
    print(f"Hello {name} from a function")


# arbitrary args
def say_hello_more(*values):
    print(f"Hello just to second arg -> {values[1]} from a function")


# nested
def multiplyBy(x):
    def tmp(n):
        return x * n

    return tmp


# defaults
def find_volume(lenght, width, depth=1):
    return lenght * width * depth


def sum(a=1, b=0):
    return a + b


# multiple return
def multi_result():
    return 0, False, "bad"


# HOF
def increment(x):
    return x + 1


def high_ord_fun(x, fun):
    return x + fun(x)


say_hello()
say_hello_custom("Juan")
say_hello_more("Juan", "Pepe", "Zara")
print(multiplyBy(3)(5))
print(find_volume(2, 3))
# call using first def arg
print(sum(b=5))

num, flag, txt = multi_result()
print(num)
print(flag)
print(txt)

print(high_ord_fun(2, increment))
print(high_ord_fun(2, lambda x: x + 1))
