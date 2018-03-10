"""
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

def get_sum(a,b):
    
    sum=0
    if a==b:
        return a
    else:
        if a>b:
          a,b=b,a
    for i in range(a,b+1):
        sum=sum+i 
    return(sum)
