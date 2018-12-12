fruit_set = {"pineaple", "cantaloup", "orange"}
print(fruit_set)
print(type(fruit_set))

# Add single Item
fruit_set.add("grape")
print(fruit_set)

# Add multiple item
fruit_set.update({"banana", "pear"})
print(fruit_set)

# remove item
fruit_set.remove("pear")
print(fruit_set)

# remove item using discard
fruit_set.discard("date")
print(fruit_set)

# remove first item

# clear set

# union - add two set
a = {"egg", "milk"}
b = {"peanut", "bread"}
c = a.union(b)
print("The New List are:", c)

# intersection - take only common item between two set
a = {"shoe", "sandal", "t-shirt", "jeans"}
b = {"shoe", "jeans", "coat", "tie"}
c = a.intersection(b)
print(c)

# difference
a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 8}
c = a.difference(b)
print(c)

