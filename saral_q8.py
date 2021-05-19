dic1=[]
dic2=[]
dic={}
i=1
while i<=10:
    student=input("enter the student name: ")
    marks=int(input("enter the marks: "))
    dic1.append(student)
    dic2.append(marks)
    i=i+1
j=0
while j<len(dic1):
    dic[dic1[j]]=dic2[j]
    j=j+1
print(dic)