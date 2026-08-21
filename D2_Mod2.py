
'''
8.Check Even or Odd Using Bitwise AND
'''
n = int(input("Enter No:"))
if n & 1 == 1:
    print("ODD")
else:
    print("Even")

'''
9.Complex No.
'''
a = input("Enter Complex No:")
c = complex(a)
r = c.real
i = c.imag

print(f"Real Part: {r}\nImaginary Part: {i}")


'''
10.Swap Last two digits of an integer
'''
n = int(input("Enter No:"))
ld = n%10
sld = (n//10)%10
sn = (n//100)*100+ld*10+sld

print(f"Swapped Number: {sn}")