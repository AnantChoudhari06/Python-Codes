from sys import stdout

def factorial(n):
    fact = 1
    if n==0:
        
        return fact
    
    for i in range(1,n+1):
        fact = fact * i
        #i = i+1

    return fact

print("Developed by Anant and Shreyas\n\n")
print("Enter number of levels")
level = int(input())
#level = 6
#level = level - 1
if level == 0:
    print("Please enter a number greater than 0")
    print("")

if level < 0:
    print("Enter Positive Numbers")

if level > 11:
    print("Restricting to 10 levels. Remove this 'if' if your screen permits")
    exit()
for i in range (0,level):
    for k in range(0,level-i):
            print ("\t",end=" ")
    for j in range (0,i+1):
        num = int((factorial(i)/(factorial(i - j)*factorial(j))))
        for l in range(0,2):
            print ("\t",end=" ")
        print (num, end =" ")

    print("\n")
    
