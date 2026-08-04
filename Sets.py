#Sets in Python 
#Sets is the collection of the unordered items.
#Each element in the set must be unique & immutatble 

collection = {1,2,3,4, "hello","world"}

print(collection)
print(len(collection)) #total number of items

a = {} #empty dictionary
b = set() #empty set; syntax 

#Set Methods
sets = set()
sets.add(1) #adds ana element
sets.add(2) 
sets.add(2)
sets.add("ayush")
sets.add((1,2,3,4))
sets.remove(1) #removes the element
# sets.clear() #empties the set
print(sets.pop()) #remove a random values
print(len(sets))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2)) #combines both set values & returns new {1,2,3,4,5,6,7,8}
print(set1.intersection(set2)) #combine common values & returns new {4,5}

