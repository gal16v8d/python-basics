for element in range(10):
    print(element)

data_list = [10, 20, 30, 40, 50]
for element in data_list:
    print(element)

data_tuple = ("rock", "paper", "scissor")
for element in data_tuple:
    print(element)

data_dict = {"name": "shirt", "price": 100, "stock": True}
for key in data_dict:
    print(key, " => ", data_dict[key])
for key, value in data_dict.items():
    print(key, " => ", value)
