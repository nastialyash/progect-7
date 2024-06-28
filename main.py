mytuple = tuple([1,2, [3,4],5,6,7])
mytuple[2][1]= 8
print (mytuple)

mytuple = tuple([1,2,3,4,5,6,7,8,9])
mytuple2 = []
for i in mytuple:
    if i%2 == 0:
        mytuple2.append(i)  
print(mytuple2)

mytuple = tuple([1,2,3,4,5])
mytuple1 = (1)
mytuple2 = (2)
mytuple3 = [3]
mytuple4 = (4)
mytuple5 = (5)
print(mytuple1)
print(mytuple2)
print(mytuple3)
print(mytuple4)
print(mytuple5)

mytuple = tuple([4,1,23,21,15,78,34,90,12])
out_set = list(mytuple)
out_set.sort()
print(out_set)

list1 = [23,76,5,4]
list2 = [44, 34,12,5]
out_set = set(list1)
out_set2 = set(list2)
print(out_set. intersection(list1))
print(out_set2. intersection(list2))
print(out_set. isdisjoint(list1))
print(out_set2. isdisjoint(list2))
print(out_set. difference(list1))
print(out_set2. difference(list2))
print(out_set. symmetric_difference(list1))
print(out_set2. symmetric_difference(list2))

mytuple = tuple([1,2,3,4,12, 7])
mytuple2 = tuple([2,3,4,1,5,23,7])
out_set = set(mytuple)
out_set2 = set(mytuple2)
out_set.difference(mytuple)
out_set2.difference(mytuple2)
mytuple3 = tuple(out_set)
mytuple4 = tuple(out_set2)
print(out_set)
print(out_set2)
print(mytuple3)
print(mytuple4)

list = [1,2,3,4,5,2,4]
list.sort()
out_set = set(list)
print(out_set)

list = [[1,2,3],
        [4,5,2],
        [3,8]]
out_set = set(list)

print(out_set.isdisjoint(list))

mytuple = tuple([1,4,6, 7])
sum = 0
dob = 1
for i in mytuple:
     sum += i
     dob *= i
     dil = sum/len(mytuple)
print(sum)
print(dob)
print(dil)

mytuple = tuple([
    [1,2,3],
    [4,3,6],
    [7,8,9]
])
mytuple1 = mytuple[0][0]
mytuple2 = mytuple[1][1]
mytuple3 = mytuple[2][2]

print(mytuple1)
print(mytuple2)
print(mytuple3)

list = [1,2,3,4,1,6,2,7,1,3,7,1,3]
out_set = set(list)
list1 ={}
for i in list:
    if i in list1:
        list1[i] += 1
    else:
        list1[i]  = 1



list = [
    [1,2,3],
    [2,5,7],
    
]
out_set = tuple(list)
print(out_set)