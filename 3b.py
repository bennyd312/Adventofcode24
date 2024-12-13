def RemoveRedundant(text):
    updated = str()
    temp = text
    seeking = 0
    first = True
    while True:
        if first==True:
            index = text.find("don\'t()")
            if index!=-1:
                updated += text[:index]
                temp = text[index:]
                first = False
                seeking = 1
            else:
                updated = text
                break
        elif seeking == 1:
            index = temp.find("do()")
            if index!=-1:
                temp = temp[index+4:]
                seeking = 0
            else:
                break
        elif seeking == 0:
            index = temp.find("don\'t()")
            if index!=-1:
                updated += temp[:index]
                temp = temp[index+6:]
                seeking=1
            else:
                updated += temp
                break


    return updated


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



text = str()

f = open('input.txt','r')
for line in f:
    text += line
f.close()

print(sum(MullItOver(RemoveRedundant(text))))
