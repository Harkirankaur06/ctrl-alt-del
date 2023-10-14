import csv


def nurses():
    def login():
        floor=input("floor:  ")
        passw=input("password:  ")
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\nurse_login.csv',"r",newline="")
        r=csv.reader(f)
        l=[floor,passw]
        for i in r:
            if i==l:
                page()
        else:
            print('error')
        f.close()
    
    def page():
        print('1 for query box \n 2 for changing the status \n')
        b=int(input())
        if b==1:
            querybox()
        elif b==2:
            solved()
        def querybox():
            f=open("C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\query.csv",'a+',newline="")
            r=csv.reader(f)
            for i in r:
                if i[-1]=='pending':
                    print(i[0],' has \n',i[1])
            f.close()
        def solved():
            f=open("C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\query.csv",'a+',newline="")
            w=csv.writer(f)
            r=csv.reader(f)
            room=input('the the room: ')
            for i in r:
                if i[0]==room:
                    i[-1]=input('enter the current status')        
            f.close()


def labs():
    def login():
        global lab
        lab=input("lab:  ")
        passw=input("password:  ")
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\lab_login.csv',"r",newline="")
        r=csv.reader(f)
        l=[lab,passw]
        for i in r:
            if i==l:
                page()
        else:
            print('error')
        f.close()

    def page():
        print('1 for check the appointment \n 2 for changing the status \n')
        s=int(input())
        if s==1:
            appoint()
        elif s==2:
            done()
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\report.csv','a+',newline='')
        def appoint():
            r=csv.reader(f)
            for i in r:
                if i[0]==lab and i[-1]=='pending':
                    print(i[0],' - ',i[-1])
        def done():
            global lab
            w=csv.writer(f)
            r=csv.reader(f)
            for i in r:
                if i[0]==lab:
                    room=input('enter the room no')
                    if i[1]==room:
                        i[-1]=input('enter the report link:  ')