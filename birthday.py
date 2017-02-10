"""
birthday.py
Author: Abby Feyrer
Credit: Emma
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
monthrn = month_name[todaymonth]

name=input("Hello, what is your name? ")
month=input("Hi "+name+", what was the name of the month you were born in? ").lower()
year=input("And what year were you born in, "+name+"? ")
day=input("And the day? ")

if int(day)==31 and month==("october"):
    print("You were born on Halloween!")
if int(day)==todaydate and month==monthrn:
    print("Happy birthday!")
    
if month==("december") or month==("january") or month==("february"):
    season="winter"
if month==("march") or month==("april") or month==("may"):
    season="spring"
if month==("june") or month==("july") or month==("august"):
    season="Summer"  
if month==("september") or month==("october") or month==("november"):
    season="fall"
if int(year)<=1989 and int(year)>=1980:
    timeperiod="eighties"
if int(year)<1980:
    timeperiod="Stone Age"
if int(year)<=1999 and int(year)>=1990:
    timeperiod="nineties"
if int(year)>=2000:
    timeperiod="two thousands"
    
print(""+name+", you are a "+season+" baby of the "+timeperiod+".")
