# input 
string = "PyNaTive"

# expected output
# yaivePNT

s1 = ""
s2 = ""

smallLetter = "qwertyuiopasdfghjklzcxvbnm"

for i in range(len(string)) :
    flag = True
    for j in range(len(smallLetter)) :
        if(string[i] == smallLetter[j] ) :
            flag = False
            s1 += string[i];
            break;
        
    if(flag):
        s2 += string[i];
        
print(s1+s2);
        
        