import os
import platform
import mysql.connector
import datetime
global z
mydb=mysql.connector.connect(user='root',password='Your Password Here',host='localhost',database='Your Database Name')
mycursor=mydb.cursor()

def registercust():
    L=[]
    name=input('Enter name:')
    L.append(name)
    addr=input('Enter address:')
    L.append(addr)
    jr_date=input('Enter date of journey:')
    L.append(jr_date)
    source=input('Enter source:')
    L.append(source)
    destination=input('Enter destination:')
    L.append(destination)
    cust=(L)
    sql='insert into pdata(custname,addr,jrdate,source,destination) values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,cust)
    mydb.commit()


def ticketprice():
    global b

    print('We have the following rooms for you:-')
    print('1. type First class--->rs 6000 PN\-')
    print('2. type Business class--->rs 4000 PN\-')
    print('3. type Economy class--->rs 2000 PN\-')
    x=int(input('Enter your choice:'))
    n=int(input('Enter No. of Passengers:'))
    if x==1:
        print('you have opted First class.')
        b=6000*n
    elif x==2:
        print('you have opted Business class.')
        b=4000*n
    elif x==3:
        print('you have opted Economy class.')
        b=2000*n
    else:
        print('Please select a class type.')
    print('your ticket amount is =',b,'\n')

def menuview():
    print('Do you want to see menu available? Enter 1 for yes:')
    ch=int(input('Enter your choice:'))
    if ch==1:
        sql='select * from food'
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

def orderitem():
    global s
    print('Do you want to see food menu available? Enter 1 for yes:')
    ch=int(input('Enter your choice:'))
    if ch==1:
        sql='select * from food'
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
        print('What do you want to purchase from above list? Enter your choice.')
        d=int(input('Your choice:'))
        if d==1:
            print('You have ordered Tea.')
            a=int(input('Enter quantity:'))
            s=10*a
            print('Your amount for Tea is:',s,'\n')
        elif d==2:
            print('You have ordered Coffee.')
            a=int(input('Enter quantity:'))
            s=10*a
            print('Your amount for Coffee is:',s,'\n')
        elif d==3:
            print('You have ordered Colddrink.')
            a=int(input('Enter quantity:'))
            s=20*a
            print('Your amount for Colddrink is:',s,'\n')
        elif d==4:
            print('You have ordered Samosa.')
            a=int(input('Enter quantity:'))
            s=10*a
            print('Your amount for Samosa is:',s,'\n')
        elif d==5:
            print('You have ordered Sandwich.')
            a=int(input('Enter quantity:'))
            s=50*a
            print('Your amount for Sandwich is:',s,'\n')
        elif d==6:
            print('You have ordered Dhokla.')
            a=int(input('Enter quantity:'))
            s=30*a
            print('Your amount for Dhokla is:',s,'\n')
        elif d==7:
            print('You have ordered Kachori.')
            a=int(input('Enter quantity:'))
            s=10*a
            print('Your amount for Kachori is:',s,'\n')
        elif d==8:
            print('You have ordered Milk.')
            a=int(input('Enter quantity:'))
            s=20*a
            print('Your amount for Milk is:',s,'\n')
        elif d==9:
            print('You have ordered Noodles.')
            a=int(input('Enter quantity:'))
            s=50*a
            print('Your amount for Noodles is:',s,'\n')
        elif d==10:
            print('You have ordered Pasta.')
            a=int(input('Enter quantity:'))
            s=50*a
            print('Your amount for Pasta is:',s,'\n')
        else:
            print('Please enter your choice from the menu.')

def luggagebill():
    global z
    print('Do you want to see rate for luggage? Enter 1 for yes:')
    ch=int(input('Enter your choice:'))
    if ch==1:
        sql='select * from luggage'
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input('Enter your weight,of extra luggage:'))
    z=y*100
    print('Your luggage bill:',z,'\n')
    return z

def ticketamount():
    a=input('Enter customer name:')
    print('Customer name:',a,'\n')
    print('Luggage bill:',z)
    print('Food bill:',s)
    print("complete amount is:",z+s+b)

def Menuset():
    print('Enter 1: To enter customer data.')
    print('Enter 2: For ticketamount.')
    print('Enter 3: For viewing food menu.')
    print('Enter 4: For food bill.')
    print('Enter 5: For luggage bill.')
    print('Enter 6: For complete amount.')
    print('Enter 7: Exit.')
    '''try:
        #userinput=int(input('Please select an above option.')
    except ValueError:
        exit("\nHi, that's not a number.")'''

    userinput=int(input('Enter your choice:'))
    if userinput==1:
        registercust()
    elif userinput==2:
        ticketprice()
    elif userinput==3:
        menuview()
    elif userinput==4:
        orderitem()
    elif userinput==5:
        luggagebill()
    elif userinput==6:
        ticketamount()
    elif userinput==7:
        quit()
    else:
        print('Enter correct choice.')

Menuset()
def runagain():
    runagn=input('\nWant to run again? y/n:')
    while runagn=='y':
        if platform.system=='windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input('\nWant to run again? y/n:')
runagain()


    
    
        

