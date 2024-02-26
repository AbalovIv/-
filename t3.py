from csv import *
with open('/home/student/Рабочий стол/1402/scientist.txt','r' , encoding= 'utf-8') as file:
    data= list(DictReader(file, delimiter='#'))
    day= input()
    while day!='эксперимент':
        for i in data:
            k=i['date'].split('-')
            k = str(k[2]) + '.' + str(k[1]) + '.' + str(k[0]) 
            if day == k:
                print(f'Ученый {i["ScientistName"]} создал препарат: {i["preparation"]} - {k}')
                break
        
        else:
            print('В этот день ученые отдыхали')
        day=input()
