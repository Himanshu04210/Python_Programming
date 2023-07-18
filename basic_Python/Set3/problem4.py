# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


string = "madaman";

reveredString = string[::-1]


if string == reveredString :
    print("The word", string, "is a palindrome.")
else : print("The word", string, "is not a palindrome.")