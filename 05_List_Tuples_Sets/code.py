myList = ["apple", "banana"]
myTuple = ("apple", "banana")
mySet = {"apple", "banana"}

print(myList)
myList.append("grape")
myList.remove("apple")
print(myList)

print(myTuple) # cant add or remove anything
print(myTuple.count)

print(mySet) # set doesnt have duplicate items
mySet.add("apple")
# set doesnt have any order. so you cant access elements with indexer
print(mySet)