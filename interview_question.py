d={1:"sristhi",3:"anzum",2:"megha"}
key_=[]
value_=[]
for key in d:
    key_.append(key)
    value_.append(d[key])
print(key_)
print(value_)
i=0
while i<len(key_):
    j=0
    while j<len(key_):
        if key_[i]<key_[j]:
            key_[i],key_[j]=key_[j],key_[i]
            value_[i],value_[j]=value_[j],value_[i]
        j+=1
    i+=1
print(key_)
print(value_)
dict={}
k=0
while k<len(key_):
    dict[key_[k]]=value_[k]
    k+=1
print(dict)


