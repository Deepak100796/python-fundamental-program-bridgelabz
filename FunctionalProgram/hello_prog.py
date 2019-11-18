# User Input and Replace String Template “Hello <<UserName>>, How are you?”
# I/P -> Take User Name as Input. Ensure UserName has min 3 char
# Logic -> Replace <<UserName>> with the proper name
# O/P -> Print the String with User Name

def hello(msg):
    if 3>=len(z):
        print("**plz enter name more than 3 char** ")
    else:
        print("Hello {} ,how are you".format(z))
z=str(input("enter your name : "))
hello(z)