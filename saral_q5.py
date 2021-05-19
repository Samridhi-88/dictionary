list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
d1={}
i=0
while i<len(list1):
    d1[list1[i]]=list2[i]
    i+=1
print(d1)
