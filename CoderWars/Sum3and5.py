"""
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
"""

def find(n):
    # Code here
    sum=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            sum=sum+i
    return(sum)

print("Enter value of n")
n=int(input())
print(find(n))
