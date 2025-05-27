# float comp
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

# should compare using tolerance diff
print(abs(x - y) < 0.0001)

# numeric operands
# sum
print(10 + 10)
# dif
print(10 - 5)
# multiply
print(10 * 2)
# div
print(10 / 3)
# mod
print(10 % 2)
# int div
print(10 // 3)
# pow
print(2**3)
# op order (left to right), then
# P - paren
# E - exp/pow
# M - multiply
# D - div
# A - sum/add
# S - subs/dif
print(2**3 + 3 - 7 / 1 // 4)
