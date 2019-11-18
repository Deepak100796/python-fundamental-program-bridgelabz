"""
Regular Expression Demonstration
a. Desc ­> Read in the following message: Hello <<name>>, We have your full
name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx.
Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
Use Regex to replace name, full name, Mobile#, and Date with proper value.
b. I/P ­> read in the Message
c. Logic ­> Use Regex to do the following
i.
ii.
iii.
iv.
Replace <<name>> by first name of the user ( assume you are the user)
replace <<full name>> by user full name.
replace any occurance of mobile number that should be in format
91­xxxxxxxxxx by your contact number.
replace any date in the format XX/XX/XXXX by current date.
d. O/P ­> Print the Modified Message.
"""


"""
    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""
# Import statement
try:
    import re
    import datetime
except ImportError:
    print("import error: ")

"""
regex function is created and re module is used as pattern finder
"""


def regex_replace():

    try:      # try method is used to catch the input error

        # user input is taken for the below details
        name = input("enter your name :")           # input for the user
        fullname = input("enter your full name please")
        mobile_number = int(input("please enter your mobile number in 91xxxxxxxxxx format"))
        now = datetime.datetime.now()
        date = now.strftime("%d/%m/%Y")

        # here number validation is done for number

        mobile = len(str(mobile_number))
        mobilelist = list(str(mobile_number))
        val = mobilelist[0:2]
        if mobile != 12:
            print ("please check the mobile number entered ")
            return
        if val != list(str(91)):
            print(" please check the mobile number entered")
            return

        # data from where file will be replaced
        file = """Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system. 
                your contact number is 91­xxxxxxxxxx.Please,let us know in case of any
                 clarification Thank you BridgeLabz XX/XX/XXXX """

        # regex method is used for the checking the pattern from the data

        namesub = re.compile("<<\w+>>")               # pattern for name
        fullnamesub = re.compile("<<\w+.\w+>>")        # pattern for full name
        numersub = re.compile("\d+.\w+")               # pattern for number.
        datesub = re.compile("\w+/\w+/\w+")

        # here all the pattern catch by the re is substitute in the data

        file=re.sub(namesub, name.upper(), file)
        file=re.sub(fullnamesub, fullname.upper(), file)
        file=re.sub(numersub, str(mobile_number), file)
        file=re.sub(datesub, date, file)

        # now the replaced data is printed
        print(file)

    except:
        print("check the input")

"""
main function is created and reg function is called 
"""

if __name__ == '__main__':

    regex_replace()    # function is called