'''
12. Write a Python program to print the calendar of a given month and year.
'''
import calendar # for the calendar display
import datetime as dt 

# enter the year and month value

y = int(input('Enter the year : '))
m = int(input('Enter the month : '))

# if month value is invalid setting it to 0 because no checking the calendar
# month function

if y < 1 :
    #setting the current year 
    print('# info year is less than 1 , Setting it to current year')
    y = dt.datetime.now().year

if m >12 or m < 1:
    print('# info month is out of the range 1 to 12 , Setting it to current month ')
    m = dt.datetime.now().month
    
print(calendar.month(y,m))
