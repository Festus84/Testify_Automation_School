# Create a function that accepts two numbers, 
# add the numbers and prints out the result in the console.

def add(num1 = 20, num2 = 25):
    result = num1 + num2

    print("Result", result)

add()
add(5)
add(5, 5)

# Create a function that return the string value "Testify Python"

def subject_name(school="Testify Python"):
    return school
print(subject_name())

subject_name()