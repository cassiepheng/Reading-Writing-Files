#program that reads the file customers.csv and produces a new file containing the customer name and country they are from

import csv

infile = open('customers.csv', 'r')

csv_obj = csv.reader(infile)

header = next(csv_obj)  #this skips the first row

#count the number of customers
def count():
    infile = open('customers.csv', 'r')
    counter = 0
    for line in infile:
        counter += 1
    return counter


#writing to a new file
def write_cust():
    outfile = open('customer_country.csv', 'w')
    #print the full name and country
    outfile.write("Full Name,Country\n")
    for rec in csv_obj:
        outfile.write(f"{rec[1]} {rec[2]},{rec[4]}\n" )
    #counter for the number of customers listed
    counter = count()
    print(f"The total number of customers is: {counter-1}")
    outfile.close()

write_cust()