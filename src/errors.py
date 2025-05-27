# can define one or multiple errors
# can add else to define a block of code to be executed if no errors were raised
# can add finally it will be executed regardless if the try block raises an error or not.
try:
    print("Hello")
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Finished")

# except raise
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
