"""
Create the Week Object having a list of WeekDay objects each storing the day (i.e
S,M,T,W,Th,..) and the Date (1,2,3..) . The WeekDay objects are stored in a Queue
implemented using Linked List. Further maintain also a Week Object in a Queue to
finally display the Calendar
Note ­ If a particular day has no date then the date is set as empty string and add it
to queue.
Page 12 of 16
"""
# @import statement
from dataStructureProgram.ordered_linkedlist.linklist import OrderedList

# @creating object ob ordered list
ll = OrderedList()

# @ calender class
class Calendar:

    # See if given year is a leap year or not
    def leapYear(self, year):
        if len(year) == 4:
            if int(year) % 400 == 0:
                if int(year) % 100 == 0:
                    if int(year) % 4 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        else:
            return True

        # Find thw number of days in given month

    def month_day(self, month, year):

        if month == 'January' or 'March' or 'May' or 'July' or 'August' \
                or 'October' or 'December':
            number_of_days = 31

        elif month == "April" or 'June' or 'September' or 'November':
            number_of_days = 30
        elif month == 'February':
            if obj.leapYear(year) == True:
                number_of_days = 29
            else:
                number_of_days = 28
        return number_of_days

    # Find wich day it is on 1sst of that month
    def week_day(self, month, year):

        year1 = year - ((14 - month) / 12)
        x = year1 + (year1 / 4) - (year1 / 100) + (year1 / 400)
        month1 = month + 12 * ((14 - month) / 12) - 2
        day1 = (1 + x + (31 * month1) / 12) % 7
        return int(day1)

    # Convert month into coreesponding integer value for calculation
    def month_int(self, month):
        if month == 'January':
            return 1
        if month == 'February':
            return 2
        if month == 'March':
            return 3
        if month == 'April':
            return 4
        if month == 'May':
            return 5
        if month == 'June':
            return 6
        if month == 'July':
            return 7
        if month == 'August':
            return 8
        if month == 'September':
            return 9
        if month == 'October':
            return 10
        if month == 'November':
            return 11
        if month == 'December':
            return 12


# @ driver code
week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
obj = Calendar()

year = int(input("Enter year:"))
month = input("Enter month : ")
number_of_days = obj.month_day(month, year)
print(str(month) + " has " + str(number_of_days) + " number of days" + "coz year is "
      + str(year))
month_i = obj.month_int(month)
day = obj.week_day(month_i, year)
print("Day is : ", week[day])

calender_row = []
print('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')

for month_day in range(1, number_of_days):
    for i in range(day):
        calender_row.append(' ')
    if month_day % 7 == 0:
        ll.add(month_day)
    else:
        ll.add(month_day)
ll.print()
