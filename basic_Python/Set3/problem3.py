# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"
numbers = [2, 7, 11, 15]
target = 9

i = 0
j = len(numbers) - 1

while i < j:
    total = numbers[i] + numbers[j]
    if total == target:
        print(i, j)
        break
    elif total > target:
        j -= 1
    else:
        i += 1

