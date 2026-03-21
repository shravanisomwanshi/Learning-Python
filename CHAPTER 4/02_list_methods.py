friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1 ,34, 62, 2, 6, 11]
# l1.sort() # it's not a 11 it's an L1 
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
l1.remove(62)
value =l1.pop(3)
print(value)
print(l1)