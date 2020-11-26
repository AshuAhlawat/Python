#module
import datetime as dt
#https://www.w3schools.com/python/python_datetime.asp

#function
def curall():
    cur = dt.datetime.now()
    print(cur)
def curdate():
    cur = dt.datetime.now()
    print(cur.date())
def curmonth():
    cur = dt.date.now()
    print(cur.month)
def curyear():
    cur = dt.datetime.now()
    print(cur.year)
def curhour():
    cur = dt.datetime.now()
    print(cur.hour)
def curday():
    cur = dt.datetime.now()
    print(cur.strftime("%A"))



#main

curall()
curdate()
curyear()
curday()