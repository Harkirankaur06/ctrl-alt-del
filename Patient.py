import csv

def login():
    global id
    id=input("id:  ")
    passw=input("password:  ")
    f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Login.csv',"r",newline="")
    r=csv.reader(f)
    l=[passw,id]
    for i in r:
        if i==l:
            page()
    else:
        print('error')
    f.close()

def page():
    print('1 for BP heart rate\n 2 for test results \n 3 for appointments \n 4 for prescription \n 5 for progress \n 6 for query box \n 7 for doctor details\n')
    z=int(input())
    if z==1:
        bp_hr()
    elif z==2:
        test()
    elif z==3:
        appointments()
    elif z==4:
        prescription()
    elif z==5:
        progress()
    elif z==6:
        querybox()
    elif z==7:
        doc_det()
    def bp_hr():
        bp=int(input('enter the latest blood pressure'))
        hr=int(input('enter the latest heartrate reading'))
        print('bp= ',bp,'Hgmm\n')
        print('hr= ',hr,'bpm')

    def test():
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\report.csv','r',newline='')
        room=input('enter the room no:  ')
        r=csv.reader(f)
        for i in f:
            if i[1]==room:
                print(i[-1])
        f.close()

    def appointments():
        global id
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_appoint.csv','r',newline='')
        r=csv.reader(f)
        for i in r:
            if i[1]==id:
                print(i[0],' at ',i[2])
        else:
            print('no appointments')
        f.close()

    def prescription():
        link=input('the cloud link for presciption')
        print(link)

    def progress():
        global id
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_appoint.csv','r',newline='')
        r=csv.reader(f)
        for i in r:
            if i[1]==id:
                print(i[-2])
        else:
            print('not updated')
        f.close()

    def querybox():
        global id
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\query.csv','a+',newline='')
        f.seek(0)
        r=csv.reader(f)
        for i in r:
            if i[0]==id:
                i[1]=input('enter the query')

    def doc_det():
        global id
        f=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\doc_detail.csv','r',newline='')
        g=open('C:\\Users\\Harkiran\\Desktop\\cyber cup\\data\\Patient_Details.csv','r',newline='')
        cr=csv.reader(f)
        r=csv.reader(g)
        for i in r:
            if i[-2]==id:
                doc=i[-1]
        for i in cr:
            if i[0]==doc:
                print('doctor name: ',i[0],'\nqualification: ',i[1],'\nspeciality: ',i[2],'\ncontact: ',i[3])