fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1

addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit) 


#output:-3
#output:-{"Apple":2,"banana":1,"apple":1}