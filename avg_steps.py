#using the file steps.csv, calculate the average steps taken each month. 
#Each row represents one day. 
#Output should have the name of the month and the corresponding average steps for that month. 

#open and read csv file
#import calendar

import csv
import calendar

infile = open('steps.csv', 'r')

csv_obj = csv.reader(infile) 

header = next(csv_obj)

#use multiple lists from the csv data
months = []
total = []
count = []

#use functions to differentiate the tasks
#use the for loop and if-else statements to append the data
#convert numbers to months
#use the index function to differentiate between the months by month names
#count how many months there are (should be 12)
def append_lists():
    for rec in csv_obj:
        month = int(rec[0])
        step = float(rec[1])
        name = calendar.month_name[month]

        if name in months:
            value = months.index(name)
            total[value] += step
            count[value] += 1

        else:
            months.append(name)
            total.append(step)
            count.append(1)

#display the average steps per month
def avg_steps_display(): 
    for i in range(len(months)):
        average = total[i] / count[i]
        print(f"{months[i]} - {average:,.2f}")

#call the functions
append_lists()
avg_steps_display()

