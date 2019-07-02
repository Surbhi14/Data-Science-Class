a={}
a1={"name":"ABC"}
print(a1)
print(a1["name"])
a={"name":"ABC","age":27,"address":{"pincode":452001,"city":"Indore"},"hobbies":["football","cricket","music"]}
print(a["address"]["city"])
print(a["hobbies"][2])
a["name"]="xyz"
a["graduation"]="Bachlor"
print(a)
del a["graduation"]
print(a)
del a1
print(a.keys())
print(list(a.keys()))
print(list(a.values()))
b={1:"Shanti",2:"Manti",3:"Kanti"}
a[1]=b[1]
print(a)
a.update(b)
print(a)
#vales=None
b=dict.fromkeys(a,None)
print(b)
print(b.items())
print(b)
