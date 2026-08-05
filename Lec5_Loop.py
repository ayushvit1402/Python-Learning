#Loops
#While Loop 
count = 1   #Iterator
while count <= 5:
    print("hello", count)  #Looping = iteration
    count += 1

print(count)

#Print numbers from 1 to 5
i = 1

while i <= 5:
    print(i)
    i += 1

print("Loop Ended")

#Print numbers from 5 to 1
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Loop Ended")

#Break & Continue
#Break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i +=1

print("End of Loop")

#Continue
i = 0
while i <= 10:
    if(i%2 == 0):
        i+=1
        continue #Skip
    print(i)
    i +=1

print("End of Loop")

#For Loop
nums = [1,2,3,4,"Potato"]
tup = (1,1,7,8,6,3,7)
str = "Ayush"

for char in str:
    print(char)
else:
    print("END")



