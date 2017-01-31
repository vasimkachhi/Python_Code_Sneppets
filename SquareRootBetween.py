"""
    This program print numbers who's square lies between given limits
"""

import math
bottom = input("Min number\n")
top = input("Max number\n") + 1

print range(int(math.ceil(math.sqrt(bottom))), int(math.ceil(math.sqrt(top))))


a = [n*n for n in range(1, 11)]
b = map(math.sqrt, filter(lambda x: x if bottom < x < top else '', a))
print b

a = [math.sqrt(i) for i in range(bottom, top)]
b = filter(lambda x: x if x - int(x) == 0 else "", a)
print b
