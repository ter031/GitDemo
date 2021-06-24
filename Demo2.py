a = [12,'deepak',23.5,True]

print(a[-1])
print(a[1:4])
a.insert(2,543)
print(a)
a.append("thakur")
print(a)
a[1] = "DEEPAK"
print(a)
del a[0]
print(a)

b = (12,34.5,"deepak",True)
print(b[0:4])

c = {"name":"deepak","designation":"SQA","Age":28}
print(c["Age"])

c["hometown"]="bilaspur"
print(c)

c["name"]="sunny"
print(c)