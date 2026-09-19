t1 = (1,2,3,4)
t2 = ("a" ,"b" ,"c")
t = t1 + t2   #Concatenation
print(t)

tuple1 = (0,1,2,3,2,31,1,3,2,3)
res = tuple1.count(3)           
res = tuple.index(3)            #return idx of 3
res = tuple1.index(3, 4, 8)     #return idx of 3 in [4:8]
print(res)