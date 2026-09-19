l = [11,45,1,2,4,6,1,1]
l.append(7)   #Add 7 to the last in the list
l.sort()      #Sort the in ascending order  
l.sort(reverse=True)    #Sort in desc. order
l.reverse()    #reverse the list
print(l.index(1))   #return the index of first occur
print(l.count(1))   #count occur of 1 in the list
m=l.copy()    #copy the original list
l.insert(1,899) #insert 899 at index 1
l.extend(m)   #for insert more than one value at the last in the list

m = [900, 1000, 1100]
k = l+m     #Concatenation
print(k)
print(l)