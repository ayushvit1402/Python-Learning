#1. Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

#2. Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

#3. Print a multiplication table of a number n
a = int(input("n:"))
i = 1

while i <= 10:
    print(a*i)
    i += 1

#4. Print the elements of the following list using a loop [1, 4, 9, 16.....,100]

sqr = [1,4,9,16,25,36,49,64,81,100]
# traverse
idx = 0

while idx < len(sqr) :
    a = print(sqr[idx])
    idx += 1

#5. Search for a number x in this tuple using loop:
(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx:",i)
        break
    else:
        print("Finding")
    i += 1


