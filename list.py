product_list = ["onion", 12, 12.98]
print(product_list)

# Show only first item
print(product_list[0].upper())

# Show first two item
print(product_list[0:2])

# Update item with index number or replace
product_list[1] = "bread"
product_list[2] = "rice"
print(product_list)

# Add item in last position
product_list.append("milk")
print(product_list)

# Add item in desired position
product_list.insert(0, "eggs")
print(product_list)

# Add multiple item
product_list.extend(["peanut", "chocolate"])
print(product_list)

# Reverse item
product_list.reverse()
print(product_list)

# Remove item with name
product_list.remove("milk")
product_list.remove("eggs")
print(product_list)

# Remove item with index number
del product_list[0]
print(product_list)

# Remove last item
product_list.pop()
print(product_list)

# List length and count
print(len(product_list))

print(product_list.count("peanut"))

# List Sort by Number
number = [5, 2, 4, 1, 3]
number.sort()
print(number)

# List Sort by Alphabetically
alphabet = ["d", "a", "c", "e", "b"]
alphabet.sort()
print(alphabet)

