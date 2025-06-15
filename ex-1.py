USERNAME= "admin"
PAASSWORD = "12345"
isLogin = False
while not isLogin:
    userName=input("Enter username:")
    password = input("Enter your password:")
    if userName == USERNAME and password == password:
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")