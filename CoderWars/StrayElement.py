"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Implement the method stray which accepts such array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples:

[1, 1, 2] => 2

[17, 17, 3, 17, 17, 17, 17] => 3
"""

def stray(arr):
    i=0
    while i<= len(arr):
        if arr.count(arr[i]) <2:
            return(arr[i])
        i=i+1
