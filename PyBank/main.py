#import modules for using csv file
import os
import csv

#define file path for resource data
budget_data_path = os.path.join('Resources','budget_data.csv') 

#create empty lists
months = [] 
profit_loss = []
monthlyChange = []

#set running total to 0 to start
profitLossRunningTotal = 0 

#loop throuh rows in budget data csv file
with open(budget_data_path, encoding="utf8") as PyBankFile:
    csvreader = csv.reader(PyBankFile, delimiter=',')
    budget_data_header = next(csvreader)
    print(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        profitLossRunningTotal += int(row[1])

#initiate while loop to make list of monthly changes
i = 0
while i < len(profit_loss)-1:
    monthlyChange.append(profit_loss[i+1]-profit_loss[i])
    i = i + 1

#set result calculations
Total_Months = len(months) #number of records in list
Average_Change = round((sum(monthlyChange)/len(monthlyChange)),2) #takes sum of all values in monthly change and divides that by number of values
Greatest_Increase = max(monthlyChange) #highest value in monthly change list
Greatest_Decrease = min(monthlyChange) #lowest value in monthly change list
Greatest_Increase_Index = monthlyChange.index(Greatest_Increase)+1 #offset index number to accomodate for no value corresponding to first month
Greatest_Decrease_Index = monthlyChange.index(Greatest_Decrease)+1 

#print results to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: $" + str(profitLossRunningTotal))
print("Average Change: $" + str(Average_Change))
print("Greatest Increase: " + months[Greatest_Increase_Index] + " ($" + str(Greatest_Increase) + ")")
print("Greatest Decrease: " + months[Greatest_Decrease_Index] + " ($" + str(Greatest_Decrease) +")")

#set up text file for results
output_file = os.path.join("analysis","financial_analysis.txt")

#enter results into text file
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis \n")
    datafile.write("----------------------------\n")
    datafile.write("Total Months: " + str(Total_Months)+ "\n")
    datafile.write("Total: $" + str(profitLossRunningTotal)+ "\n" )
    datafile.write("Average Change: $" + str(Average_Change)+ "\n")
    datafile.write("Greatest Increase: " + months[Greatest_Increase_Index] + " $" + str(Greatest_Increase)+ "\n")
    datafile.write("Greatest Decrease: " + months[Greatest_Decrease_Index] + " $" + str(Greatest_Decrease))


