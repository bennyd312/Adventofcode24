def MullItOver(text):
    form = ['m','u','l','(',',',')']
    i = 0
    j = 0
    muls = []
    temp1 = str()
    temp2 = str()
    while i<len(text):
        if j==5 and text[i]==form[j] and temp2!='':
            muls.append(int(temp1)*int(temp2))
            j=0
            temp1 = str()
            temp2 = str()
            i+=1
        elif text[i] == form[j]:
            j+=1
            i+=1
        elif j==4 and (text[i].isnumeric()):
            temp1 += text[i]
            i+=1
        elif j==5 and (text[i].isnumeric()):
            temp2 += text[i]
            i+=1
        elif j==4 and text[i]==form[j] and temp1!='':
            j+=1
            i+=1
        
        else:
            temp1, temp2 = str(), str()
            j=0
            i+=1
    return muls

total = 0


f = open('input.txt','r')
for line in f:
    total += sum(MullItOver(line))
f.close()

print(total)