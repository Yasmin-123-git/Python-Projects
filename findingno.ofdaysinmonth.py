#basic project on decision making
'''wap to find number of days in a month:'''
print("program will display the no.of days in respective month:")
month=int(input("enter the number of month (1-12)"))
if(month==2):
    year=int(input("enter the year"))
    if(year%4==0 and year%100!=0 and year%400==0):
        print("leap year")
        print("the number of days is:28")
    else:
        print("the number of days is:29")
elif month in (4,6,9,11):
    print("the number of days is:30")
elif month in (1,3,5,7,8,10,12):
    print("the number of days is:31")
else:
    ("print a valid month")