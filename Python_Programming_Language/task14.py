# Some strings Operations
# upper --> convert a string to upper case
name = "bequalified"
upper_value = name.upper()
print("upper", upper_value)

# len ----> to get the size of a string
size = len(name)
print("size", size)

# lower ----> to convert a string to lower case
lower_value = name.lower()
print("lower", lower_value)

# Capitalized----> use to convert the first letter to upper case
capitalize_value = name.capitalize()
print("capitalize", capitalize_value)

# Count----> count the occurrence of a value in a string

bequalified_count = name.count("bequalified")
print("bequalified count:", bequalified_count)

e_count = name.count("e")
print("e count:", e_count)