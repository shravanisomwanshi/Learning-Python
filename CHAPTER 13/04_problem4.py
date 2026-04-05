from functools import reduce
l = [1,2,2,3,25,56,56,7,37]

def greater(a, b):
    if(a>b):
        return a
    return b


print(reduce(greater,l))