# dict{"student":["seeta","ram","geeta"],"class":["class1","class2","class3",]}
# count=0
# for i in dict.values():
#     for j in i:
#         count+=1
#     print(count)



dict ={
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2','sub3']}
count=0
for l in dict.values():
   for i in l:
       count += 1
print(count)