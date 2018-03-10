"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides 
of given length and false in any other case.
"""

def is_triangle(a, b, c):
    if a+b>c:
        if b+c>a:
            if c+a>b:
                return True
    return False
