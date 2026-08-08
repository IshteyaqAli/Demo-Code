Email = input("Enter your email")
Password = int(input("Enter your password"))

remail = input("Re-enter your email")
rpassword = int(input("Re-enter your password"))
if Email == remail and Password == rpassword:
    print("Login successful")
elif Email == remail and Password != rpassword:
    print("Incorrect password")
elif Email != remail and Password == rpassword:
    print("Incorrect email")
else:
    print("Incorrect email and password")

