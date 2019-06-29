#Import dependencies
import os
import csv

#Create the csv path
budget_data = os.path.join("PyBank/budget-data.csv")

#Open and read the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip the header row
    csv_header = next(csvreader) 

    #Create starter lists
    total_months = []
    total_profit = []
    profit_change = []

    #Go through the rows and add the months and profits to lists
    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Go through the total profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the differences from month to month and append to profit change list
        profit_change.append(total_profit[i+1]-total_profit[i])
        
#Get the greatest changes by using max and min from the profit change list
greatest_increase = max(profit_change)
greatest_decrease = min(profit_change)

#Get the corresponding month for greatest changes
greatest_increase_month = profit_change.index(greatest_increase) + 1
greatest_decrease_month = profit_change.index(greatest_decrease) + 1 

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

#Create the txt output path
output_file = os.path.join("/Users/allison/Desktop/python-challenge/PyBank/output.txt")

#Write to output file
with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
