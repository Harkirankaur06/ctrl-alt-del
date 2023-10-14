import Registration
import Patient
import doctor
import staff

while True:
    print('1- for new registrartion or check out\n2- for patient portal\n3- for doctor portal\n4- for staff portal\n')
    x=int(input())
    if x==1:
        print('1- for new registration\n2- for checkout of the patient\n')
        y=int(input())
        if y==1:
            Registration.registration()
            break
        elif y==2:
            registration.checkout()
            break
    elif x==2:
        Patient.login()
        break
    elif x==3:
        doctor.login()
        break
    elif x==4:
        print('1 for nurse login \n 2 for lab login \n')
        c = int(input())
        if c==1:
            staff.nurses.login()
            break
        elif c==2:
            staff.labs.login()
            break
