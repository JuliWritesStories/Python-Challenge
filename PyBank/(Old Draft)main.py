#import csv for banking data
import os
import csv
#declare columns
Date = []
Profit = []
#declare future values
total_months = 0
total_profit = 0
ending_profit = 0
Average_change = 0
Greatest_increase = 0
Greatest_decrease = 0
#set the path and read the csv
budget_file = os.path.join('Resources','budget_data.csv')
#troubleshooting path
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(budget_file, encoding='UTF-8') as csvfile:
    #read the csv
    csvreader = csv.reader(csvfile,delimiter=",")
    #account for headers
    csv_header = next(csvfile)
    for row in budget_file:
#find the total number of months in the data set
        total_months +=1
#find the net amount of profits/losses over the entire period
        
#find the average change
#find the greatest increase in profits with date and amount
#find the greatest decrease in profits with date and amount
#print the name
print("Financial Analysis")
print("----------------------------")
#print the total months
print(f"Total Months: {total_months}")
print(f"Total: {ending_profit}")
