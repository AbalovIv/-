from csv import *
def hash(s):
    s=s.split()
    s=s[0] + str(s[1]) + str(s[2])
    a=[chr(x) for x in range(2000)]
    b=[int(x) for x in range(1024)]
    p=0
    r=0
    for i in s:
        r=a.index(i)
        r=r%1024
        p+=b[r]
    return  str(r%2024)
with open('/home/student/Рабочий стол/1402/scientist.txt','r' , encoding= 'utf-8') as file:
    data= list(DictReader(file, delimiter='#'))
    for i in data:
        list(i).insert(0,hash(i['ScientistName']))
with open('scientist _with_hash.csv','w' , encoding='utf-8') as file:
    writter = DictWriter(file,delimiter='#', fieldnames=['hash','ScientistName', 'preparation', 'date', 'components'])
    writter.writeheader()
    writter.writerows(data)       
