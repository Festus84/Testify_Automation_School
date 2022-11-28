# Write a python program to check if a string is a palindrome.Then optionally write a unit test to check
# your program correctness

def isPalindrome(s):
    return s == s[::-1]


s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
