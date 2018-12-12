my_dict = {
  "first_name": "John",
  "last_name": "Doe",
  "age": 25,
}
print(my_dict)

# dictionary extend or add new dictionary
my_dict_extend = {
  "company_location": "New York",
  "salary": 5000000
}
print(my_dict_extend)
my_dict.update(my_dict_extend)
print(my_dict)

# access single item
print(my_dict["first_name"])

# update item
my_dict["last_name"] = "Smith"
print(my_dict)

# a new key & value added
my_dict_extend["email"] = "js007@gmail.com"
print(my_dict_extend)
my_dict.update(my_dict_extend)
print(my_dict)

# # clear dictionary
# my_dict.clear()
# print(my_dict)

# # delete dictionary
# del my_dict
# print(my_dict)

