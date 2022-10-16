import re

#Registration Function
def register():
    db = open("database.txt",'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    # Email/Username Validation
    name = input("Enter Email/Username:")
    pattern1 = "[\w._%-+]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}"
    result1 = re.findall(pattern1,name)
    if name in d:
        print("Username Already Exists!\nPlease Try Again\n")
        register()
    elif result1:
        pass
    else:
        print("Invalid Email/Username\n Condition for Email/Username \n1)Should contain @ followed by .\n2)Must not start with number or special character\n3)For Example sherlock@gmail.com \nPlease Try Again!\n")
        register()

    #Password Validation
    pw = input("Enter Password:")
    pattern2 = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@?#$%^&+=]).*$"
    result2 = re.findall(pattern2,pw)
    if result2:
        db = open("database.txt","a")
        db.write(name+", "+pw+"\n")
        print("Registered Successfully!!")
        exit()
    else:
        print("Condition for Password \n1)Password should have minimum length 5 and maximum length 16  \n2)Must contain at least ONE SPECIAL CHARACTER \n3)Must contain at least ONE NUMBER \n4)Must contain at least ONE UPPERCASE character \n5)Must contain at least ONE LOWERCASE character\n")
        register()


#Function for login for user
def login():
    db = open("database.txt",'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
        username = input("Enter your Username/Email-id: ")
        if username in d:
            password = input("Enter your Password: ")
            if password == data[username]:
                print("Login success")
                exit()
            else:
                print("Password incorrect")
                forget()
        else:
            print("Username doesn't exist\n Please Register!\n")
            register()

#Function for forget password or update new password
def forget():
    db = open("database.txt", 'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    n = int(input(" Do you wish to retrieve your old password or create new password?\n1) Retrieve\n2)Create new password\n"))
    if n == 1:
        uname = input("Enter your username: ")
        if uname in d:
            print("Hi! "+uname+"\nYour Password is "+data[uname]+"\n")
            print("Thank you")
        else:
            print(uname+" doesn't exist!\n Please Register!")
            register()

    elif n == 2:
        un = input("Enter your Username: ")
        if un in d:
            pw = input("Enter your new password: ")
            pattern2 = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$"
            result2 = re.findall(pattern2, pw)
            if result2:
                data[un] = pw
                db = open("database.txt", "w")
                for i, j in data.items():
                    db.write(i + ", " + j + "\n")
                print("Password Changed Successfully!")
                exit()
            else:
                print("Condition for Password \n1)Password should have minimum length 5 and maximum length 16  \n2)Must contain at least ONE SPECIAL CHARACTER \n3)Must contain at least ONE NUMBER \n4)Must contain at least ONE UPPERCASE character \n5)Must contain at least ONE LOWERCASE character\n")
                forget()
        else:
            print(un+" doesn't exist!\nRegister First!")
            register()

#Function for Home Page
def home():
    A=int(input("$$$$$$$$$$$ Registration and Login system $$$$$$$$$$$ \n1. Login\n2. Registration\n3. Exit\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"))
    if A==1:
        login()
    elif A==2:
        register()
    elif A==3:
        exit()
home()