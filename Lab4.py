from collections import Counter
nUsers = int(input("Enter number of users:"))
dict = {}

for x in range(nUsers):
    name = input("Enter username:")
    nItems = int(input("How many items?"))
    itemList = []
    for y in range(nItems):
        print("ITEM ", (y+1) , ":")
        itemList.append(input())
    itemSet = set(itemList)
    itemList = list(itemSet)
    dict[name] = itemList

print()
print("USER DATA:")
for key in dict.keys():
    print(key , "--> " ,dict.get(key))
print()


listCounter = []
for key in dict.keys():
    for item in dict.get(key):
        listCounter.append(item)
dictCount = Counter(listCounter)


print("COMMON ITEMS:")
for key in dictCount.keys():
    if dictCount.get(key) > 1:
        print(key)
print()


print("UNIQUE ITEMS: ")
for key in dictCount.keys():
    if dictCount.get(key) == 1:
        print(key)
print()

sortedDict = sorted(dictCount.values(), reverse=True)

print("MOST POPULAR ITEM:")
for key in dictCount.keys():
    if dictCount.get(key) == sortedDict[0]:
        print(key)