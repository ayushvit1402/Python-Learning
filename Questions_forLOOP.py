#1. print the elements of the following list using a loop;
#[1,4,6,9,16,25,36,49,67,81,100]

nums = [1,4,6,9,16,25,36,49,67,81,100]

for el in nums:
    print(el)

# 2. Search for a number x in this tuple using loop:
(1,4,6,9,16,25,36,49,67,81,100)

tup = (1,4,6,9,16,25,36,49,67,81,100,49)
x = 49

idx = 0
for i in tup:
    if (i == x):
        print("number found at idx", idx)
        break
    idx +=1


