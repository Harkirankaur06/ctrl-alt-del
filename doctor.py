import csv

def login():
    global name
    name=input("name:  ")
    id=input('id:  ')
    dob=input("dob:  ")
    f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_login.csv',"r",newline="")
    r=csv.reader(f)
    l=[name,id,dob]
    for i in r:
        if i==l:
            page()
    else:
        print('error')
    f.close()

def page():
    print('1 for list of Patient \n 2 for appointments \n 3 for Schedule \n')
    z=int(input())
    if z==1:
        list_patients()
    elif z==2:
        appointments()

    elif z==3:
        schedule()
    def list_patients():
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','r',newline='')
        r=csv.reader(f)
        for i in r:
            if i[-1]==name:
                print('name:  ',i[0])
                print('room:  ',i[-2])

    def appointments():
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_appoint.csv','a+',newline='')
        print('1 for schedule new appointment \n 2 for changing the status \n')
        b=int(input())
        if b==1:
            new()
        elif b==2:
            existing()
        def new():
            w=csv.writer(f)
            room=input("enter the patients room no.")
            time=int(input('enter the appointment time'))
            purpose=input('enter the purpose of visit')
            status='pending'
            w.writerow([name,room,time,status,purpose])
        
        def existing():
           room=input('enter the room no:  ')
           f.seek(0)
           r=csv.reader(f)
           for i in r:
               if i[1]==room:
                   i[-2]=input('enter the current status:  ')
        f.close()    


    def schedule():
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_appoint.csv','r',newline='')
        r=csv.reader(f)
        for i in r:
            if i[-2]=='pending':
                print(i[1],'\n',i[2])
        f.close() 

      