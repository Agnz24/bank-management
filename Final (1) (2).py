
import random
import csv
from tkinter import *
#from tkinter.ttk import *
import mysql.connector as c
import datetime
from datetime import date 


customerPins=[]
customerNames=[]
customergNames=[]
money=[]
count=0



password=8240

def calculateAge(birthDate): 

    days_in_year = 365.2425    

    age = int((date.today() - birthDate).days / days_in_year)
    
    

    return age 


def createmajAccount():
    print('welcome to people bank!!')

    print('Please fill the following details for your account creation:')

    y=date.today()
    
    a=str(y)
    
    
    name = input("Enter the account holder First name in small letters : ")
    customerNames.append(name)
    year = int(input('Enter birth year'))
    month = int(input('Enter birth month 01/02/03/04/05/06/07/08/09/10/11/12'))
    day = int(input('Enter birth date'))
    date1 = datetime.date(year, month, day)
    age =calculateAge(date1)
    address=input("Enter your resdiential address")
    

    
    

    
    
    city=input('enter your city:')

    country=input('enter your country:')

    nationality=input('enter your nationality:')

    language=input('enter your mother tongue:')
    mobno=input('enter a valid mobile number:')

    if len(mobno)==10:
        mobileno=mobno
    else:
        print('invalid number!!')
    email=input('enter your email ID')
    
    
    print('female press f')
    print('male   press m')
    print('other  press o')
    ag=input('enter your gender:')

    if ag=='f':
        gender='female'
    elif ag=='m':
        gender='male'
    elif ag=='o':
        gender='other'
    else:
        print("Invalid!!")

    print('marital status:')
    print('married press m')
    print('single  press s')
    marista=input('enter your marital status:')


    if marista=='m':
        maritalstatus='married'
    elif marista=='s':
        maritalstatus='single'
    else:
        print("Invalid choice")


    print('customer types:')
    print('-> individiual press 1')
    print('-> corporate   press 2')
    print('-> bank        press 3')

    custype=input('enter customer type:')


    if custype=='1':
        custometype='individual'
    elif custype=='2':
        custometype='corporate'
    elif custype=='3':
        custometype='bank'
    else:
        print('invalid choice!!')
    
    
    
    pin= random.randint(10000000000,999999999999)
    customerPins.append(pin)
    aadhno=input('Enter your Aadhar card number:')
    aadh=list(aadhno)
    if len(aadh)==12:
        desk=customerPins.index(pin)
        
        acctype = input("Enter the type of account [C/S] : ")
        deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        money.append(deposit)
        if acctype=='c'and deposit>=500:
            
            root = Tk()
            Label(root, text = 'Account holder photo', font =('Verdana', 15)).pack(side = TOP, pady = 10)
            Label(root, text = 'Aadhar Scanned', font =('Verdana', 15)).pack(side = TOP, pady = 10)

            
            
            
            accounttype='current'

            print("\n\n\nAccount Created")
            
            person={'pin number':pin,'name':customerNames[desk],'account type':acctype,'amount':money[desk]}
            
        elif acctype=='s'and deposit>=1000:
            root = Tk()
            Label(root, text = 'Account holder photo', font =('Verdana', 15)).pack(side = TOP, pady = 10)
            Label(root, text = 'Aadhar Scanned', font =('Verdana', 15)).pack(side = TOP, pady = 10)

            
            
        
            accounttype='savings'

            print("\n\n\nAccount Created")
            
            person={'pin number':pin,'name':customerNames[desk],'account type':acctype,'amount':money[desk]}
            
        else:
            print("Your chosen account type balance not sufficient")
    else:
        print("Wrong Aadhar Card Number")

    info=name+'\t'+str(age)+'\t'+city+'\t'+country+'\t'+nationality+'\t'+language+'\t'+str(mobileno)+'\t'+email+'\t'+gender+'\t'+maritalstatus+'\t'+custometype+'\t'+str(pin)+'\t'+str(aadhno)+'\t'+accounttype+'\t'+str(deposit)+'rs'+'\n'

    f=open('account.txt', 'a+')

    rec=f.write(info)

    print(rec)

    db=c.connect(host='localhost',database='bank',user='root',password='computer')

    mc=db.cursor()


    query="insert into members(name,age,address,city,country,nationality,language,mobileno,email,gender,maritalstatus,customertype,pin,aadharno,accounttype,accountbalance,datesvisited) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values=(name,age,address,city,country,nationality,language,mobileno,email,gender,maritalstatus,custometype,pin,aadhno,accounttype,deposit,a)

    mc.execute(query,values)

    db.commit()
    

    
    

        
def createminAccount():
    
    print('welcome to people bank!!')

    print('Please fill the following details for your account creation:')

    name = input("Enter the account holder Fullname in small letters : ")
    customerNames.append(name)

    y=date.today()
    
    a=str(y)

    
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date1 = datetime.date(year, month, day)
    age =calculateAge(date1)

    
    address=input("Enter your resdiential address")
    
    gname=input("Enter Guardian Name:")
    customergNames.append(gname)
    rel=input("What's the relation between Guardian and accountholder")
    
    
    city=input('enter your city:')
    country=input('enter your country:')
    nationality=input('enter your nationality:')
    language=input('enter your mother tongue:')

    mobno=input('enter a valid Guardian mobile number:')
    if len(mobno)==10:
        mobileno=mobno
    else:
        print('invalid number!!')
    email=input('enter your email ID')

    maritalstatus='nil'
    
    
    print('female press f')
    print('male   press m')
    print('other  press o')
    ag=input('enter your gender:')


    if ag=='f':
        gender='female'
    elif ag=='m':
        gender='male'
    elif ag=='o':
        gender='other'
    else:
        print("Invalid!!")


    pin= random.randint(10000000000,999999999999)
    customerPins.append(pin)
    aadhno=input('Enter your Aadhar card number:')
    aadhgno=input('Enter Guardian Aadhar card number:')
    aadh=list(aadhno)
    aadhg=list(aadhgno)
    if len(aadh)==12 and len(aadhg)==12:
        desk=customerPins.index(pin)
        
        acctype = input("Enter the type of account [C/S] : ")
        deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        money.append(deposit)
        if acctype=='c'and deposit>=500:
            
            root = Tk()
            Label(root, text = 'Account holder photo', font =('Verdana', 15)).pack(side = TOP, pady = 10)
            Label(root, text = 'Aadhar Scanned', font =('Verdana', 15)).pack(side = TOP, pady = 10)

            
            
            accounttype='current' 

            print("\n\n\nAccount Created")
            
            person={'pin number':pin,'name':customerNames[desk],'account type':acctype,'amount':money[desk]}
            
        elif acctype=='s'and deposit>=1000:
            root = Tk()
            
            Label(root, text = 'Account holder photo', font =('Verdana', 15)).pack(side = TOP, pady = 10)
            Label(root, text = 'Aadhar Scanned', font =('Verdana', 15)).pack(side = TOP, pady = 10)

            
            accounttype='savings'

            print("\n\n\nAccount Created")
            
            person={'pin number':pin,'name':customerNames[desk],'account type':acctype,'amount':money[desk]}
            
        else:
            print("Your chosen account type balance not sufficient or might be type error \nPlease try again ")
    else:
        print("Wrong Aadhar Card Number")



    info=name+'\t'+str(age)+'\t'+city+'\t'+country+'\t'+nationality+'\t'+language+'\t'+str(mobileno)+'\t'+email+'\t'+gender+'\t'+maritalstatus+'\t'+custometype+'\t'+str(pin)+'\t'+str(aadhno)+'\t'+accounttype+'\t'+str(deposit)+'rs'+'\n'

    f=open('account.txt', 'a+')

    rec=f.write(info)

    print(rec)

    db=c.connect(host='localhost',database='bank',user='root',password='computer')

    mc=db.cursor()

    query="insert into members(name,age,address,city,country,nationality,language,mobileno,email,gender,maritalstatus,customertype,pin,aadharno,accounttype,accountbalance,datesvisited) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values=(name,age,address,city,country,nationality,language,mobileno,email,gender,maritalstatus,custometype,pin,aadhno,accounttype,deposit,a)

    mc.execute(query,values)

    db.commit()
            
    
        

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tWelcome TO PEOPLE'S BANK")
    print("\t\t\t\t**********************")
    input()

    
def writeaccount():
    print("To create Major account\n Please press number 1")
    print("To create Minor account\n Please press number 2")
    
    maomi=input("Enter Major/Minor:")

    if maomi=='1':

        age=int(input("Enter your Age:"))
        if age>18:
            createmajAccount()
        else:
            print("Under Age!!")
    elif maomi=='2':

        age=int(input("Enter your Age:"))
        if age<=18:
            createminAccount()
        else:
            print("Please type correct age")
            
    else:
        print("INVALID CHOICE")
        
        


def deposit():

    num = int(input("Enter The account No. : "))
    depositamount=int(input('enter the amount to be deposited:'))
    db=c.connect(host='localhost',database='bank',user='root',password='computer')
    mc=db.cursor()
    mc.execute('select*from members')

    for i in mc:
        sohap=list(i)
        if sohap[12]==num:
            k=sohap[14]
            sohap[14]=k+depositamount
            j=sohap[14]
            print('amount deposited successfully')
            print('current amount in your account is',j)
            query="update members set accountbalance='%s' where pin='%s'"
            value=(j,num)
            mc.execute(query,value)
            db.commit()

        else:
            print('no such account exists !! please try again')

def withdraw():

    num = int(input("Enter The account No. : "))
    withd=int(input('enter the amount to be withdrawed:'))
    acctype = input("Enter the type of account [C/S] : ")
    db=c.connect(host='localhost',database='bank',user='root',password='computer')
    mc=db.cursor()
    mc.execute('select*from members')

    for i in mc:
        sohap=list(i)

        if sohap[11]==num:
            mon=sohap[14]

            if withd>mon:
                print('not enough money in your account')
            else:

                left=mon-withd
                sohap[14]=left
                print('money withdrawed successfully')
                query="update members set accountbalance='%s' where pin='%s'"
                
                value=(left,num)
                mc.execute(query,value)
                db.commit()
                
        
                if acctype=='c' and left<500:

                    print("BALANCE UNDER THE MINIMUM BALANCE ,\n Fine RS.10")
                    left=left-10
                    query="update members set accountbalance='%s' where pin='%s'"
                    value=(left,num)
                    mc.execute(query,value)
                    db.commit()
                    print('your current balance is',left,'-/Rs') 
                
                elif acctype=='s' and left<1000:

                    print("BALANCE UNDER THE MINIMUM BALANCE ,\n Fine RS.10")
                    left=left-10
                    query="update members set accountbalance='%s' where pin='%s'"
                    value=(left,num)
                    mc.execute(query,value)
                    db.commit()
                    print('your current balance is',left,'-/Rs')
                
                else:
                    print("Balance",left,'-/Rs')
        

def displaySp():

    num=int(input('Enter The account No. : '))
    db=c.connect(host='localhost',database='bank',user='root',password='computer')
    mc=db.cursor()
    mc.execute('select*from members')
    for i in mc:
        sohap=list(i)
        if sohap[12]==num:
            mon=sohap[14]
            print('your account balance is',mon,'-/Rs')
        else:
            print('no such account exists!!')



    

               

        
        
    
def deleteacc(num):

    
    db=c.connect(host='localhost',database='bank',user='root',password='computer')
    mc=db.cursor()
    mc.execute('select*from members')

    for i in mc:
        sohap=list(i)
        print(sohap)
        if sohap[11]==num:
            delname=str(sohap[0])
            delaccno=sohap[11]
            que="insert into table delacc(name,accno)values(%f,%f)"
            val=(delname,delaccno)
            mc.execute(que,val)
            db.commit
            
            
            
            query="DELETE FROM members WHERE pin='%s'"
            value=(num)
            mc.execute(query,value)
            db.commit()
            
            print("Your account has successfully been deleted from people bank")
    
        else:
            print('no such account exists')




          
def modifyacc(num):
    db=c.connect(host='localhost',database='bank',user='root',password='computer')
    mc=db.cursor()
    mc.execute('select*from members')

    print("Press 1 to change Mobile number")
    print("Prees 2 to change Residential Address")
    print("Prees 3 to change Email Address")
    
    
    aka=input("Enter your choice")
    
    if aka=='1':
        for i in mc:
            sohap=list(i)
            if sohap[12]==num:
                newmobno=int(input("Enter your new mobile number"))
                query="update members set mobileno='%s' where pin='%s'"
            
                value=(newmobno,num)
                mc.execute(query,value)
                db.commit()
                print("Your mobile number has been changed successfully")
            else:
                print("NO SUCH PIN NUMBER")

    elif aka=='2':
        for i in mc:
            sohap=list(i)
            if sohap[12]==num:
                newadd=input("Enter your new address")
                query="update members set address=%s where pin='%s'"
                value=(newadd,num)
                mc.execute(query,value)
                db.commit()
                print("Your residential address  has been changed successfully")
            else:
                print("NO SUCH PIN NUMBER")


    elif aka=='3':
        for i in mc:
            sohap=list(i)
            if sohap[12]==num:
                newid=input("Enter your new email address")
                query="update members set email=%s where pin='%s'"
                value=(newid,num)
                mc.execute(query,value)
                db.commit()
                print("Your email address  has been changed successfully")
            else:
                print("NO SUCH PIN NUMBER")
    else:
        print("YOU PRESSED SOMETHING NOT DEFINED ,\nPLEASE CHECK AGAIN")
            
        
    
            
            
        
        
        
    
            
# start of the program
ch=''
num=0
intro()

while ch != 8:
    print("======================================")
    print("=<< 1. NEW ACCOUNT                 >>=")
    print("=<< 2. DEPOSIT AMOUNT              >>=")
    print("=<< 3. WITHDRAW AMOUNT             >>=")
    print("=<< 4. BALANCE ENQUIRY             >>=")
    print("=<< 5. ALL ACCOUNT HOLDER LIST     >>=")
    print("=<< 6. CLOSE AN ACCOUNT            >>=")
    print("=<< 7. MODIFY ACCOUNT              >>=")
    print("=<< 8. DELETED ACCOUNTS            >>=")
    print("=<< 9. EXIT                        >>=")
    print("======================================")
    print("\tSelect Your Option (1-9) ")

    ch = input()
        
    if ch == '1':
        writeaccount()

    elif ch =='2':
        deposit()

    elif ch =='3':
        withdraw()

    elif ch=='4':
        displaySp()

    elif ch=='5':
        
        
        p=int(input('enter the bank security code:'))
        if p==password:
            print("                     ****Account Holder List displayed ***                          ")
            import csv
            reader=csv.reader(open(r"C:\Users\HOME-PC\Desktop\account.txt","r"))#replace it w\ your loc
            data=[]
            for row in reader:
                data.append(row)

            #print(data)

            class Table: 
            
                def __init__(self,root): 
                        
                        # code for creating table 
                        for i in range(total_rows): 
                                for j in range(total_columns): 
                                        
                                        self.e = Entry(root, width=120, fg='blue', 
                                                                font=('Arial',16,'bold')) 
                                        
                                        self.e.grid(row=i, column=j) 
                                        self.e.insert(END, data[i][j])
            total_rows = len(data) 
 
            total_columns = len(data[0]) 

            root = Tk() 
            t = Table(root) 
            root.mainloop()
            
        else:
            print('ERROR!! security alert')


    elif ch=='6':
        
        num=int(input('Enter The account No. : '))
        count+=1
        a=date.today()
        delete={"Pin number":"Date of deletion"}
        deleteacc(num)

    elif ch=='7':
        num=int(input("Enter your pin number:"))
        modifyacc()

    elif ch=='8':
        db=c.connect(host='localhost',database='bank',user='root',password='computer')
        mc=db.cursor()
        mc.execute('select*from delacc')
        p=int(input('enter the bank security code:'))
        if p==password:

            for i in mc:
                print(('name','account no'))
                print(i)
        else:
            print('BANK SECURITY ALERT!!')
        
        
    

    elif ch=='9':
        print("Thank you for using our banking system!")
        print("We hope you are serviced well\n Thank you")
        print("\n")
        print("Come again")
        print("Bye bye")
        break

    else :
        print("Invalid choice")



