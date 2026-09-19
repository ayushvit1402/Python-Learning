tup1 = (1,2,76,342,32,"Green")
# tup1[0] = 0     #not allowed (Immutable)
print(type(tup1),tup1)
print(len(tup1),tup1)
print(tup1[0])
print(tup1[-1])
print(tup1[-2])
# print(tup1[32])     #idx out of range

if 342 in tup1:
    print("Yes 342 is present in this tuple")

tup2 = tup1[1:4]
print(tup2)

tup3 = (1,)     #comma is needed for single element
print(tup3)

