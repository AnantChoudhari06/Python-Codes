"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""

def getCount(inputStr):
    num_vowels = 0
    vows=['a','e','i','o','u']
    # your code here
    for i in inputStr:
        if i.lower() in vows:
            num_vowels=num_vowels+1
    return num_vowels
  
 print("Enter the string")
 str=input()
 print(getCount(str))
