#import modules for using csv file
import os
import csv

budget_data_path = os.path.join('..','Resources', 'budget_data.csv') #needs to be in ../PyBank/Resources directory to access 
#create empty lists
months = [] 
profit_loss = []
#set running total to 0 to start
profitLossRunningTotal = 0 

with open(budget_data_path, encoding="utf8") as PyBankFile:
    csvreader = csv.reader(PyBankFile, delimiter=',')
    print(csvreader)
    budget_data_header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        profitLossRunningTotal += int(row[1])

Total_Months = len(months)
Average_Change = round((profitLossRunningTotal / Total_Months), 2)
Greatest_Increase = max(profit_loss)
Greatest_Decrease = min(profit_loss)
Greatest_Increase_Index = profit_loss.index(Greatest_Increase)
Greatest_Decrease_Index = profit_loss.index(Greatest_Decrease)



print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: $" + str(profitLossRunningTotal))
print("Average Change: $" + str(Average_Change))
print("Greatest Increase: " + months[Greatest_Increase_Index] + " $" + str(Greatest_Increase))
print("Greatest Decrease: " + months[Greatest_Decrease_Index] + " $" + str(Greatest_Decrease))


