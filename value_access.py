# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result) 

#nested dic value access


# sd1={"class":{"student":{"name":"sara","marks":{"pysics":20,"histry":80}}}}
# print(sd1["class"]["student"]["marks"]["histry"])


person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
print(person['gender'])

print(person[4])

result = person[4]['place']

print(result) 


