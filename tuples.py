'''t=(10,20,30,40)
print(t)
for x in t:
    print(x)
t=('cse',7.5,84,(20,30))
print(t)'''

'''courses=("CSE","IT","ECE","EEE")'''
'''print(courses[2])
print(courses)
t=("abhiram")
print(t)'''

'''print(courses[1:3])'''

'''t1=(10,20,30)
t2=(20,30,40)
t3=t1+t2
print(t3)

print("CSE"*4)'''

#print(courses*2)

#print((0,1,20000)<(0,2,3))

#we can't use append, extend and sort on tuples because tuples are immutable, so we have to convert tuples into lists then we should apply those methods and convert them back to tuples.

#append method by converting tuple into list and convert back from list to tuple
'''courses=("CSE","IT","ECE","EEE")
x=list(courses)
x.append("MECH")
courses=tuple(x)
print(courses)

#extend method by converting tuple into list and convert back from list to tuple
t1=('a','b','c')
t2=('c','d','e')
x1=list(t1)
x2=list(t2)
x1.extend(x2)
t1=tuple(x1)
print(t1)

#sort method

t=('a','x', 'n', 'p')
x=list(t)
x.sort()
t=tuple(x)
print(t)'''

#removing elements from a tuple
#pop():

'''t=('a','b','c','d')
x=list(t)
y=x.pop(1)
t=tuple(x)
print(y)
print(t)'''

#del:
'''t=('a','b','c','d')
x=list(t)
del x[1]
t=tuple(x)
print(t)'''

#remove:
'''t=('a','b','c','d')
x=list(t)
x.remove('b')
t=tuple(x)
print(t)'''

#removing part of elements in a list using del:
'''t=('a','e','i','o','u')
x=list(t)
del x[1:3]
t=tuple(x)
print(t)'''

#functions in tuples
'''marks=(89,92,98,87,95,96)
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))
print(sum(marks)/len(marks))'''

















