#import modules for using csv file
import os
import csv

#define file path for resource data
budget_data_path = os.path.join('Resources','budget_data.csv') 

#create empty lists
months = [] 
profit_loss = []
monthly_change = []

#set running total to 0 to start
running_total = 0 

#loop throuh rows in budget data csv file
with open(budget_data_path, encoding="utf8") as PyBankFile:
    csvreader = csv.reader(PyBankFile, delimiter=',')
    budget_data_header = next(csvreader)
    print(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        running_total += int(row[1])

#initiate while loop to make list of monthly changes
i = 0
while i < len(profit_loss)-1:
    monthly_change.append(profit_loss[i+1]-profit_loss[i])
    i = i + 1

#set result calculations
total_months = len(months) #number of records in list
avg_profit = round((sum(profit_loss)/len(profit_loss)),2) 
avg_change = round((sum(monthly_change)/len(monthly_change)),2) #takes sum of all values in monthly change and divides that by number of values
max_increase = max(monthly_change) #highest value in monthly change list
max_decrease = min(monthly_change) #lowest value in monthly change list
max_increase_index = monthly_change.index(max_increase) + 1 #offset index number to accomodate for no value corresponding to first month
max_decrease_index = monthly_change.index(max_decrease) + 1 

#print results to terminal
print(f'''
    Financial Analysis\n
    Total Months: {len(months)}\n
    Total: ${running_total}\n
    Average Profit/Loss: ${avg_profit}\n
    Average Monthly Change: ${avg_change}\n 
    Greatest Increase: {months[max_increase_index]} (${str(max_increase)})\n
    Greatest Decrease: {months[max_decrease_index]} (${str(max_decrease)})
    ''')

#set up text file for results
output_file = os.path.join("analysis","financial_analysis.txt")

with open(output_file, "w") as datafile:
    datafile.write(f'''Financial Analysis\n
    ----------------------------\n
    Total Months: {str(total_months)}\n
    Total: ${str(profitLossRunningTotal)}\n
    Average Profit/Loss: ${avg_profit}\n
    Average Change: ${str(avg_change)}\n
    Greatest Increase: {months[max_increase_index]} ${str(max_increase)}\n
    Greatest Decrease: {months[max_decrease_index]} ${str(max_decrease)}
    ''')