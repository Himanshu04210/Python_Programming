# input

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# expected output

# 10 400
# 20 300
# 30 200
# 40 100

for i in range(len(list1)) :
    print(list1[i], list2[len(list2)-i-1]);