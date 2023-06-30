 
s1 = "Ault"
s2 = "Kelly"

finalString = "";

for i in range(len(s1)) :
    if(len(s1)//2 == i): finalString += s2;
    
    finalString += s1[i]
    
print(finalString)