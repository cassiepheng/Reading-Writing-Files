#program that reads the employee_data.csv file and prints out details of each employee

import csv

infile = open('employee_data.csv', 'r')

csv_obj = csv.reader(infile) 

header = next(csv_obj) 

#printing the details of every employee in the infile
#calculate the total pay from multiplying salary and bonus

for rec in csv_obj:
    #display salary
    Salary = float(rec[3])

    print(f"Name: {rec[1]}")
    print(f"Salary: $ {Salary:,.2f}")

    #display bonus after mutliplying the rate by the Salary
    rate = float(rec[7])
    Bonus = float(Salary * rate)
    print(f"Bonus:  $  {Bonus:,.2f}")

    #display the 
    Total_Pay = Bonus + Salary
    print(f"Pay:    $ {Total_Pay:,.2f}")
    print("                   ")
