def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,2345,2435,57856,56,7457767,436567]

f = list(filter(divisible5, a))
print(f)