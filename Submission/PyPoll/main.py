# PyPoll
# 


import csv

# Declare a variable to store a path to our csvfile
# This is the full path to our desired file:    C:\Users\emteb\Desktop\msu_data\homework\da-python-challenge\Submission\PyPoll\Resources\election_data.csv
file = "Submission\\PyPoll\\Resources\\election_data.csv"

# Declare variables for our program: vote, elecRes.
# vote: a counter for the amount of votes for the election.
# elecRes: a dictionary containing candidate names with the amount of votes they received.
vote = 0
elecRes = {}

# We need to open our csvfile and read it.
# We skip the first row and begin grabbing our information.
# 1:    increment the vote count.
# 2:    if we have seen the candidate... increment their votes.
# 3:    if we haven't seen the candidate... add them in with a '1' as their votes.
with open(file) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)

    for row in reader:
        vote += 1

        if row[2] in elecRes.keys():
            elecRes[row[2]] += 1
        
        else:
            elecRes[row[2]] = 1

# Let's start printing out the results.
# 1:    a header for the results.
#
# 2:    total votes with our 'vote' variable.
#
# 3:    print out our list of candidates with the following format
#           name: percentage of votes recieved (total votes received)
#
# 4:    winner of the election using max() on the elecRes dict.
#
print(f"\nElection Results")
print(f"------------------------------")
print(f"Total Votes: {vote:,}")
print(f"------------------------------")

for key in elecRes.keys():
    print(f"{key}: {elecRes[key]/vote:,.2%} ({elecRes[key]:,})")

print(f"------------------------------")
print(f"Winner: {max(elecRes, key = elecRes.get)}")

# This is the path to our new text file for analysis.
txtfile = "Submission\\PyPoll\\analysis\\election_data.txt"

# Open up the file... and write to it. Same stuff as above but different format.
# Note: we use str.format() to mimic most of our fstring things from above.
f = open(txtfile, "w")

f.write("Election Results\n")
f.write("------------------------------\n")
f.write("Total Votes: {:,}\n".format(vote))
f.write("------------------------------\n")

for key in elecRes.keys():
    f.write("{}: {:,.2%} ({:,})\n".format(key, elecRes[key]/vote, elecRes[key]))

f.write("------------------------------\n")
f.write("Winner: {}\n".format(max(elecRes, key = elecRes.get)))
