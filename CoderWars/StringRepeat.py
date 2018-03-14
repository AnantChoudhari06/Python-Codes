"""
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat, string):
    return (string*repeat)

print("Enter String")
string=input()
print("Enternumber of times to repeat")
repeat=int(input())
print(repeat_str(repeat,string))
