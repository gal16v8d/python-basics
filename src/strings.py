text = "She knows python"
# get some pos
print(text[0])
# get string size
print(len(text))
# get position from last pos
print(text[-1])
# slicing
# (similar to java substring), extract from 0 to 3
print(text[0:3])
# if omitted first then assumes zero
print(text[:3])
# if omitted last then assumes end of string
print(text[4:])
# both can be ommitted
print(text[:])
# substring plus jump over the string
print(text[10:16:2])
# upper, lower and swap case
print(text.upper())
print(text.lower())
print(text.swapcase())
# count how many of certain char in the string
print(text.count("h"))

# error when pos is out of range
print(text[999])
