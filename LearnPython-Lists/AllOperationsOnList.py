"""1. lists are mutable
2. slicig operation on list
3. change or adding elements to list(append, extend)
4. concatenation of lists
5. insertion at desired location
6. deletion of element or entire list
7. sort reverse and copy
8. List comprehension : elegant way to create list.
9. List membership test.
10. Iterating through a list.
11. Build in functions in list.
"""
#ways of instantiating list
neww = list() # another way to create list
neww.append(["first","second","third",12,3]) #append takes only one object , so it is one list now
list=[] #way 1
list.append(input("Enter the first element of list"))
print list
list=[1,2,3]
print list
list[0]=9  #lists are mutable
print list
list.append(8)
list.append([1,2,12])
print list
slicedList = list[2:3]
print "Sliced List"
print list
list =["f",1.1,"string"] #list can contain multiple data types
print list
print neww
print list[-1] #negative indexing on list
list.append(1)
list.append(7)
list.append(9)
list.append(23)
list.append(77)
print "Before slicing"
print list
print "Sliced List:"
print list[2:5] #value till inded of 4=5-1
print"Effect of extend method"
print list.extend([1,3,4,5,2,4,8])
print"---------------------------"
#print list.extend(1,2,3,2,2) -- extend only takes in single argument.
print list
print"====Combining two lists===="
print list+[88,85,83,97]
print"------Repeating a single character------"
print("re "*7)
print"------Slicing operation for mutation-------"
list[0:4]=[1,2,3]
print list
print"-------Removing particular element fron list--------"
list.remove(1) #value to be removed from the list is passed as the argument.
print list
print"------Deletion by assigning null list--------"
list[0:2]=[]
print list
print "--------Colon Operator----------------------"
print"1.with no bound"
print list[:]
print"2.with only left bound"
print list[1:]
print "3.with only rigth bound"
print list[:3]
print "4.with only left negative"
print list[-3:]
print"5.with only right negative"
print list[:-2]
print"6.with right and left combined"
print list [1:-1]
print "7.with right and left combined inverted"
print list[-1:1]   #tricky one
print"---------End of colon operator----------------"
print"__---____---List Member ship test---___---___---_-"
print (23 in list)
print"----------End of list membership----------------"
print"--------List comprehension: Elegant way of generating list--------"
power2 = [2**x for x in range(1,10)]
print power2
print"1.with condition Appended"
power2 = [2**x for x in range(1,10) if x > 5]
print power2
print "2.string multiply and concat"
print([x+y for x in ["Python ", "C "] for y in ["Programming","Language"]])
print"---------------***************--------------"


"""Lists can be deleted by :
1. del list
2. list.clear()"""

"""Python list mehtods :
1. append() -- append the input argument to the list
2. extend() -- extend the the elements of the list
3. insert() -- insert an item at the defined index
4. remove() -- removes an item form the list
5. pop()    -- removes and returns an element at the given index
6. clear()  -- removes all items from list
7. index()  -- at what index does the argument is present at
8. count()  -- count of occurance of the input argument
9. sort()      -- sort the list in ascending order
10. reverse()  -- reverse the list
11. copy()      -- returns shallow copy of list
"""