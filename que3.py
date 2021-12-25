lista=["eye","dead","1221","abc","aaa"]
y=0
for i in lista:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            y=y+1
print(y)