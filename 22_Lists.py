marks = [3,5,6,"Harry",True,22,58,41,56,254,"as"]
print(marks)
print(type(marks))
print(marks[0])     #return item of idx 0
print(marks[1])
print(marks[2])     #Positive idx
print(marks[-2])    #Negative idx

if 7 in marks:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#     print("Yes")


print(marks)
print(len(marks))   # total no of items in the list:-11
print(marks[1:-1]) #for converting to pos_idx len(marks)-1:- 11-1=10
print(marks[1:10])
print(marks[1:10:2])    #[start:stop:step] stop is not included

'''
List Comprehension
'''
lst = [i for i in range(10)]
print(lst)
lst = [i for i in range(10) if i%2 == 0]
print(lst)


'''
1.Ordered
2.multiple items in single variable
3.items separated by commas within [] braket
4.Mutable
'''