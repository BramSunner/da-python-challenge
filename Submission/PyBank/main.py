# PyBank



import csv

# Declare a variable to store a path to our csvfile
# This is the full path to our desired file:    C:\Users\emteb\Desktop\msu_data\homework\da-python-challenge\Submission\PyBank\Resources\budget_data.csv
file = 'Submission\\PyBank\\Resources\\budget_data.csv'

# Declare two variables to store data from the csvfile
# budgetDate:   a list of all the entries within the first column of the csvfile titled "Date"
# budgetAmt:    a list of all the entries within the second column of the csvfile titled "Profits/Losses"
#               Note: these values are integers reflecting a delta of $ for the specific date paired with them.
budgetDate = []
budgetAmt = []

# Let's do a couple things here.
# 1:    Open our csvfile
# 2:    Read the csvfile and output our data to our local lists declared above.
with open(file) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        budgetDate.append(row[0])
        budgetAmt.append(row[1])

# Let's begin to print some things.
#
# 1:    Header of our analysis and a separator between it and the data.
#
# 2:    Total Months: this is equal to the length of one of our lists (minus one: we don't want to include the header).
#
# 3:    Total: this is the sum of all of the data in our budgetAmt list (minus the header).
#
# 4:    Average Change: this is the sum of the delta between all values in the budgetAmt list (minus the header).
#                           So: we loop the list from the second index and gather the delta values
#                               and then we take the sum of that divided by the length of the list 
#                               (minus two: no header and the delta values contain one less value).
#
# 5:    Greatest Increase in Profits: this is the greatest delta value between entries on our budgetAmt list.
#                                       ... We loop through the list and collect the delta values
#                                           and then we take the max() of those values.
#                                           Also: we save the index of the highest change for use in grabbing the date from budgetDate.
#
# 6:    Greatest Decrease in Profits: this is the lowest delta value between entries on our budgetAmt list.
#                                       ... this is the same as #5 but we take the min() instead. Not gonna write that again...
#
print(f"\nFinancial Analysis")
print(f"------------------------------")
print(f"Total Months: {len(budgetDate) - 1}")
print(f"Total: ${sum(int(x) for x in budgetAmt[1:]):,.2f}")

print(f"Average Change: ${(sum(int(x) - int(budgetAmt[budgetAmt.index(x)-1]) for x in budgetAmt[2:])/(len(budgetAmt)-2)):,.2f}")

# ?:    We were having trouble getting the index for the date inside of the fstring (it makes sense... trying to do too much in there.)
#       So: we made a loop to find our greatest increase and decrease and the indices associated with those values.
#       We declare two variables: inc and dec ... and then we fill them with the values that we need.
#       inc: a list of two values where the first is to be the greatest inc value and the second is the associated date from budgetDate for that value.
#       dec: a list of two values where the first is to be the greatest dec value and the second is the associated date from budgetDate for that value.
inc = [0, 0]
dec = [0, 0]

for x in budgetAmt[2:]:
    amt = int(x) - int(budgetAmt[budgetAmt.index(x)-1])
    if amt > inc[0]:
        inc[0] = amt
        inc[1] = budgetDate[budgetAmt.index(x)]

    elif amt < dec[0]:
        dec[0] = amt
        dec[1] = budgetDate[budgetAmt.index(x)]

print(f"Greatest Increase in Profits: {inc[1]} ${inc[0]:,.2f}")
print(f"Greatest Decrease in Profits: {dec[1]} ${dec[0]:,.2f}")

# This is the filepath to print our analysis data to.
txtfile = "Submission\\PyBank\\analysis\\budget_data.txt"

# Open the file and write all the information to it.
# This is about the same as the print statements above but using str.format() instead of fstrings.
f = open(txtfile, "w")
f.write("Financial Analysis\n")
f.write("-----------------------------\n")
f.write("Total Months: {}\n".format(len(budgetDate)-1))
f.write("Total: ${:,.2f}\n".format(sum(int(x) for x in budgetAmt[1:])))
f.write("Average Change: ${:,.2f}\n".format((sum(int(x) - int(budgetAmt[budgetAmt.index(x)-1]) for x in budgetAmt[2:])/(len(budgetAmt)-2))))
f.write("Greatest Increase in Profits: {} ${:,.2f}\n".format(inc[1], inc[0]))
f.write("Greatest Decrease in Profits: {} ${:,.2f}\n".format(dec[1], dec[0]))