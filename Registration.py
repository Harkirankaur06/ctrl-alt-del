import csv
def registration():
    f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','a',newline='')
    cw=csv.writer(f)
    N = str(input('Enter the Name of Patient'))
    DOB = str(input('Enter the DOB of Patient'))
    Add = str(input('Enter the Address of Patient'))
    Ct = int(input('Enter the Contact Number of Patient'))
    Gn = str(input('Enter the Name of the Guardian'))
    Gc = int(input('Enter the Contact Number of Guardian'))
    Room = (input('Enter the Room Number of Patient'))
    Doctor = str(input('Enter the Doctor to consult'))
    Age=int(input('enter the patients age'))
    l=[N,DOB,Add,Ct,Gn,Gc,Age,Room,Doctor]
    cw.writerow(l)
    f.close()
    g=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Login.csv','a',newline='')
    f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','r',newline='')
    cr=csv.reader(f)
    l=list(cr)
    Password=l[-1][0]
    ID=l[-1][6]
    m=[Password,ID]
    cw=csv.writer(g)
    cw.writerow(m)
    g.close()
    f.close()

def checkout():
    f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Login.csv','r',newline='')
    g=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','r',newline='')
    h=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\hospital data','a',newline='')
    room=input('enter to room no ')
    cr=csv.reader(g)
    l=[]
    for i in cr:
        l.append(i)
    for i in l:
        if i[-2]==room:
            a=l.index(i)
            l.pop(a)
    g.close()
    g=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','w',newline='')
    cw=csv.writer(g)
    for i in l:
        cw.writerow(i)
    g.close()
    cr=csv.reader(f)
    l=[]
    for i in cr:
        l.append(i)
    for i in l:
        if i[-1]==room:
            a=l.index(i)
            b=l.pop(a)
            r=csv.writer(h)
            r.writerow(b)
    h.close()
    f.close()
    g=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Login.csv','w',newline='')
    cw=csv.writer(g)
    for i in l:
        cw.writerow(i)
    g.close()
