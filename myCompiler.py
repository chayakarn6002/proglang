import string
line_num=[i for i in range(1,1001,1)]
id=list(string.ascii_uppercase)
#ans=[]
while(True):
    s=input().split()
    ans=[]
    #print(len(s))
    if (int(s[0]) in line_num):
        ans.append(10)
        ans.append(int(s[0]))
    if(s[1]=="STOP"):
        ans.append(16)
        ans.append(0)
        break;
    elif(s[1] in id): 
        ans.append(11)
        ans.append(id.index(s[1])+1)
        #asgmt
        if (s[2]=='='):
            ans.append(17)
            ans.append(4)
            #exp=>term
            if (len(s)==4):
                ans.append(12)
                ans.append(int(s[3]))
            #exp=>term+term
            elif (len(s)==6 and s[4]=='+'):
                #id
                if (s[3] in id):
                    ans.append(11)
                    ans.append(id.index(s[3])+1)
                #constant
                else:
                    ans.append(12)
                    ans.append(int(s[3]))
                ans.append(17)
                ans.append(1)
                #id
                if (s[5] in id):
                    ans.append(11)
                    ans.append(id.index(s[5])+1)
                #constant
                else:
                    ans.append(12)
                    ans.append(int(s[5]))
            #exp=>term-term
            elif (len(s)==6 and s[4]=='-'):
                #id
                if (s[3] in id):
                    ans.append(11)
                    ans.append(id.index(s[3])+1)
                #constant
                else:
                    ans.append(12)
                    ans.append(int(s[3]))
                ans.append(17)
                ans.append(2)
                #id
                if (s[5] in id):
                    ans.append(11)
                    ans.append(id.index(s[5])+1)
                #constant
                else:
                    ans.append(12)
                    ans.append(int(s[5]))
    #IF
    elif (s[1]=='IF'):
        ans.append(13)
        ans.append(0)
        #cond=>term<term
        if (s[3]=='<'):
            #id
            if (s[2] in id):
                ans.append(11)
                ans.append(id.index(s[2])+1)
            #constant
            else:
                ans.append(12)
                ans.append(int(s[2]))
            ans.append(17)
            ans.append(3)
            #id
            if (s[4] in id):
                ans.append(11)
                ans.append(id.index(s[4])+1)
            #constant
            else:
                ans.append(12)
                ans.append(int(s[4]))
        #cond=>term=term
        elif (s[3]=='='):
            #id
            if (s[2] in id):
                ans.append(11)
                ans.append(id.index(s[2])+1)
            #constant
            else:
                ans.append(12)
                ans.append(int(s[2]))
            ans.append(17)
            ans.append(4)
            #id
            if (s[4] in id):
                ans.append(11)
                ans.append(id.index(s[4])+1)
            #constant
            else:
                ans.append(12)
                ans.append(int(s[4]))
        ans.append(14)
        ans.append(int(s[5]))
    #PRINT
    elif (s[1]=='PRINT'):
        ans.append(15)
        ans.append(0)
        ans.append(11)
        ans.append(id.index(s[2])+1)
    #GOTO
    elif (s[1]=='GOTO'):
        ans.append(14)
        ans.append(int(s[2]))
    out=""
    for i in ans:
        out+=str(i)
        out+=" "
    print(out)
out=""
for i in ans:
    out+=str(i)
    out+=" "
print(out)
print(0)
