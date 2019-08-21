x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))
print(country_counter)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update(country_counter)
print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)
print(y)

fruits = {"apple", "banana", "cherry"}
fruits.update({"apple1","apple2","apple3"})
print(fruits)
