"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

def find_it(seq):
    arr_size=len(seq)
    for i in range(0,arr_size):
        count = 0
        for j in range(0, arr_size):
            if seq[i] == seq[j]: 
                count+=1
        if (count % 2 != 0):return seq[i]
         
    return -1 
