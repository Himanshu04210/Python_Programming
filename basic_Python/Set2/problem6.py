# input
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# expected output

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

mainList = [];

for i in range(len(list1)) :
    for j in range(len(list2)) :
        mainList.append(list1[i] +" "+ list2[j]);
        
print(mainList);