# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dict4={**dic1,**dic2,**dic3}
# print(dict4)


# #########

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4=[]
# dic4.append(dic1)
# dic4.append(dic2)
# dic4.append(dic3)
# print(dic4)

# ########

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# ############

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4=()
# dic4=dic4+(dic1,)
# dic4=dic4+(dic1,)
# dic4=dic4+(dic1,)
# print(dic4)


#############

dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4) 
#1#6

# saral_q1