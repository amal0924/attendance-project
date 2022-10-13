f=open('file.txt','w')
data_base={1:'Amaljith',2:'Vipin'}
for id in data_base:
    print(data_base[id])
    f.write(str(id)+'.'+data_base[id]+'\n')
f.close()