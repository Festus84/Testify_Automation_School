# Create a function that converts any string  value to a sentence case, then
# write a unit test that check the function's correctness

def sentencecase(string):
    new = string.capitalize()
    print(new)
    return new


sentencecase('house')
