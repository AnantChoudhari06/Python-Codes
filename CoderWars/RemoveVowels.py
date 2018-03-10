"""
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

"""

def disemvowel(string):
    vows=['a','e','i','o','u']
    chars=[]
    for i in string:
        if i.lower() not in vows:
            chars.append(i)
    return "".join(chars)
