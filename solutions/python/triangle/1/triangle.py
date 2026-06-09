def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    if a == b and a == c:
        return True
    else:
        return False



def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    if a==b or a==c or b==c:
        return True
    else:
        return False



def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    if a!=b and  b!=c and c!=a:
        return True
    else:
        return False

