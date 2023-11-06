#import csv for banking data
import os
import csv
#set the path and read the csv
budget_file = os.path.join('Resources','budget_data.csv')
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(budget_file, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
#declare columns
Date = []
Profit = []
#declare future values
total_months = 0
total_profit = 0
Average_change = 0
Greatest_increase = 0
Greatest_decrease = 0

#find the total number of months in the data set
#find the net amount of profits/losses over the entire period
#find the average change
#find the greatest increase in profits with date and amount
#find the greatest decrease in profits with date and amount
#print and export into a text file
print("Financial Analysis")
print("----------------------------")
