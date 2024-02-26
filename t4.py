import random
from csv import *
def login(s):
    a = s.split()
    return str(a[0]) + '_' + str(a[1][0]) + str(a[2][0])
def parol():
    a = 'qwertyuioplkjhgfdsazxcvbnm'
    a += a.upper()
    a += '0123456789'
    par_ol = ''
    for _ in range(10):
        par_ol += random.choice(a)
    return par_ol


with open('/home/student/Рабочий стол/1402/scientist.txt', 'r', encoding = 'utf-8') as file:
    data= list(DictReader(file, delimiter='#'))
    for i in data:
        i['login'] = login(i['ScientistName'])
        i['password'] = parol()
with open('scientist_password.csv', 'w', encoding = 'utf-8') as file:
    writter = DictWriter(file,delimiter='#', fieldnames=['ScientistName', 'preparation', 'date', 'components', 'login', 'password'])
    writter.writeheader()
    writter.writerows(data)
