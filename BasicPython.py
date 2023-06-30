print("Hello world")

intCharacter = 10

booleanCharacter = True

floatCharacter = 9.99

stringCharacter = "Himanshu"

normalCharacter = 'h'

print(type(intCharacter))
print(type(stringCharacter))


myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

myList.append(10)
myList.remove(0)

print(myList)

sum = sum(myList)
count = len(myList)

aver = sum / count

print(sum)
print(aver)


string = "Python"
reversed_string = string[::-1]
print(reversed_string)


number = 13
count = 0
for i in range(1, number):
    if number % i == 0:
        count+=1

if count > 2:
    print(number, "Not a prime number")
else :
    print(number, "is a prime number")    



def fibbo(num):
    if num == 1 or num == 0:
        return num
    
    return fibbo(num - 1) + fibbo(num - 2)

ans = fibbo(5)

print(ans)