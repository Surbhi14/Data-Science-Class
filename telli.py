list1=[]
list2=[1,2,3]
list3=["a","b","c"]
list4=["a",1,"b","2","c",3]
list5=[1,"Hello",["A","B","C"]]
print(list1)
print(list5)
print(list2[1])
print(list3[2])
print(list2[1:])
list2[1]=4
print(list2)
list4[1:3]=67,43,29
print(list4)
print(list4.index("2"))
list2.append(2)
print(list2)
list2.insert(2,5)
print(list2)
list2.insert(4,[8,9])
print(list2)
print(list3+list5)
print(list5+list3)
list3.extend(list5)
print(list3)
a=[1,2,3,4,7,8,7,7,7]
del a[1]
print(a)
print(a.pop(2))
print(a)
a.remove(8)
print(a)
print(a.index(7))
print(a.count(7))


