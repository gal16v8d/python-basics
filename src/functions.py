# no args
def say_hello():
    print('Hello from a function')

# with args
def say_hello_custom(name):
    print(f'Hello {name} from a function')

# arbitrary args
def say_hello_more(*values):
    print(f'Hello just to second arg -> {values[1]} from a function')

# nested
def multiplyBy(x):
    def tmp(n):
        return x*n
    return tmp

say_hello()
say_hello_custom('Juan')
say_hello_more('Juan', 'Pepe', 'Zara')
print(multiplyBy(3)(5))