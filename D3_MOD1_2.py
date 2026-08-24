"""
1. Leap Year with Short-Circuit Logic
"""
y = int(input("Enter Year:"))

print("Leap" if y%4 == 0 and y%100 != 0 or y%400 == 0 else "Not Leap")

"""
2.Bitwise Power of 2 Check
"""
n = int(input("Enter Number:"))
print(f"{n} is a Power of 2" if ( n > 0 and n & n-1 == 0) else f"{n} is NOT Power of 2")

'''
3.Triangle Validity & Type CLassifier
'''
a, b, c = map(int, input("Enter Sides:").split())
if (a+b > c) and (b+c > a) and (c+a > b):
    if a == b == c:
        print("Valid Triangle: Equilateral")
    elif a == b or b == c or c ==a:
        print("Valid Triangle: Isoceles")
    else:
        print("Valid Triangle: Scalene")
else:
    print("Not Valid Triangle")