# Iterate number

print("\nloop to iterate")
number = 11
for i in range(number):
    print("number: ", i)

    print("\ncontinue")
    number = 11
    for i in range(number):
        if i == 2:
            continue
            print("number: ", i)
