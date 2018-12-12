#################################################
          # Python 3: String Formatting
#################################################

# Example 01
my_name = input("Enter a Name Here: ")
my_age = int(input("Enter Age Here: "))
print("Hello {}, you are now {} years old..".format(my_name, my_age))

# Example 02
my_name = input("Enter a Name Here: ")
my_age = int(input("Enter Age Here: "))
print("Hello.", my_name, "Your age is", my_age)

# Example 03
my_number = int(input("Enter a Number Here: "))
another_number = int(input("Enter another Number Here: "))
result = my_number / another_number
print("The Result is {r:1.3f}".format(r = result))

