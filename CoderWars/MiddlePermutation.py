"""
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term.
(If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".
"""

from itertools import permutations
def middle_permutation(string):
    #your code here
    perms=[]
    string = ''.join(sorted(string))
    perms = [''.join(p) for p in permutations(string)]
    print(perms)
    i=(len(perms)-1)//2
    return(perms[i])
