import sqlite3  
conn=sqlite3.connect('suryasql.db')

def insertdata(name,age,city):
    qry="insert into data(name,age,city) values (?,?,?); "
    conn.execute(qry,(name,age,city))
    conn.commit()
    print("successfully insert")
print('''
1=insert
2=update
3=delete
4=select
''')
a=1
while a==1:
    c=int(input("enter the number 1-4 :"))
    if c==1 :
        print("insert new record")
        name=input("enter the name: ")
        age=input("enter the age :")
        city=input("enter the city :")  
        insertdata(name,age,city)
    elif c==2 :
        print("update a record")
    elif c==3 :
        print("delete a record")
    elif c==4 :
        print("select a record")
    else:
        print("enter a correct number")
    a=int(input("enter 1 to continue :"))
else:
    print("thank you")