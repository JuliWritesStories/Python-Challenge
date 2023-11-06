#import the csv for Poll data
import os
import csv
#read the csv
Poll_file = os.path.join('Resources','election_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(Poll_file, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
#dataset has three columns: Voter ID, County, and Candidate
#find the total number of votes cast
#create a complete list of candidates who recieved votes
#find the percentage of votes each candidate won
#find the total number of votes each candidate won
#find the winner of the election based on popular vote
#Print results in terminal and export to text file