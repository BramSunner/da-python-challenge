# da-python-challenge
Module 3 Challenge for Data Analytics Bootcamp.

# About the Project
This repository contains two separate projects: PyBank and PyPoll.

# PyBank
PyBank is a script designed to be run on a csv file containing data in the following format:
Two Columns: Date | Profits/Losses

Date: the date of the entry.
Profits/Losses: a number representing the delta of our company's cash since the last entry.

The script extracts the data from the csv and then prints out the following data to the terminal and a txtfile:
Our script extracts two lists from the csv: a list for the dates and a list for the profits/losses in the data set.
From these lists, the scipt prints of the following to the terminal and a txtfile:
1: Amount of months the data set spans.
2: Total amount of money at the end of the data set.
3: Average change between entries in the data set.
4: Greatest increase from one entry to another within the data set.
5: Greatest decrease from one entry to another within the data set.

# PyPoll
PyPoll is a script designed to be run on a csv file containing data in the following format:
Three Columns: Voter ID | County | Candidate.

Voter ID: a unique ID representing a 'voter' in the data set.
County: the county in which the 'voter' voted.
Candidate: the person for which the 'voter' voted.

Our scipt extracts the total amount of votes, candidate names and their respective amount of votes.
From those variables, the script then prints out the following to the terminal and a txtfile:
1: Total amount of votes in the election.
2: A full representation of the votes for candidates as follows:
   Candidate Name: Percentage of Votes Won (Total Amount of Votes Won)
3: The winning candidate's name.

# Built In
Python.
Resources for the project as csv files.
Output for the project as text files.

# Acknowledgements
In main.py of PyPoll on line 54 and line 72, the max() function used was something that I grabbed from:\n
Coady, A. (2008, November 11). Comment on _Getting key with maximum value in dictionary?_. [Online forum post]. 
  https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
