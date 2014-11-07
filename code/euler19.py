## program counts the number of sundays on the first of the month in the 20th century

from datetime import date


start =  date(1901,1,1)
end =  date(2000,12,1)
counts = 0

i =  start.toordinal() # converts to int 
while i <= end.toordinal():
    if date.fromordinal(i).day==1: # if the first of the month
        if date.fromordinal(i).weekday()==6: # if sunday
            counts+=1
    i+=1
print counts