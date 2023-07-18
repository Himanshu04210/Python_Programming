# input


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# expected output
# ['My', 'name', 'is', 'Kelly']

mainList = [];

for i in range(len(list1)):
    mainList.append(list1[i] + list2[i]);
    
print(mainList);