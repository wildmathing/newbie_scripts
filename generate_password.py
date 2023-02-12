from numpy.random import randint


symbols = [chr(num) for num in randint(40, 122, 16)]
password = "".join(symbols)
print(password)