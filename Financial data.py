# Dependencies
import os
import csv
import sys
# CSV read path location
csvpath = os.path.join(sys.path[0],'Data/budget_data.csv')
# Output path location
file3 = open("Financial_Results.txt","w") 
#Reading the csv file using CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    count = 0
    Total_profit_Loss = 0
# Initiating the variables
    previousPnL = 0 #Previous row profit/loss
    profit_loss = 0 #Variable to store difference of previous and current row's profit/loss
    profit_loss1 = 0 #Variable to store running sum of difference of profit/loss
    max_increase_profit = 0 #Variable to store the maximum increase in profit
    min_increase_profit = 0 #Variable to store the minimum increase in profit
    month_max = '' #Variable to store the month of maximum increase in profit
    month_min = '' #Variable to store the month of minimum increase in profit

    # Running a loop in csvreader that reads through all the rows and performs desired calculations
    for row in csvreader:
        #Splitting date column into month and date
        month,date = row[1].split('-')
        #Counter to record the number of rows
        count += 1
        #Condition to skip the first row that doesn't have change in profit_loss
        if previousPnL != 0:
            profit_loss = int(row[0]) - previousPnL
        previousPnL = int(row[0])
        # Summing the total change in profit/loss over time 
        profit_loss1 += profit_loss
        # Calculating maximum and minimum increase in profit/loss
        if profit_loss > max_increase_profit:
            max_increase_profit = profit_loss
            month_max = row[1]
        if profit_loss < min_increase_profit:
            min_increase_profit = profit_loss
            month_min = row[1]
         # Calculating total of profit/loss column
        Total_profit_Loss += int(row[0])
    Average_change = profit_loss1/(count-1)
    #Final Print
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: {}".format(count))
    print("Total: ${}".format(Total_profit_Loss))
    print(f'Average Change: ${Average_change:.2f}')
    print("Greatest Increase in Profits: {} (${})".format(month_max,max_increase_profit))
    print("Greatest Decrease in Profits: {} (${})".format(month_min,min_increase_profit))
str1 = "Financial Analysis\n"
str2 = "-----------------------------------------\n"
str3 = "Total Months: {}\n".format(count)
str4 = "Total: ${}\n".format(Total_profit_Loss)
str5 = f'Average Change: $ {Average_change:.2f}\n'
str6 = "Greatest Increase in Profits: {} (${})\n".format(month_max,max_increase_profit)
str7 = "Greatest Decrease in Profits: {} (${})\n".format(month_min,min_increase_profit)  

L = [str1,str2,str3,str4,str5,str6,str7]

file3.writelines(L)