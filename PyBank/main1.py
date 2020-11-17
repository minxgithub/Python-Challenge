import os
import csv

# Path to collect data from the Resources folder
bank_csv_path = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(bank_csv_path, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    # Read the header row
    header = next(budget_data)
    
    # Creat an empty list for Date, Profit/Loss, and Profit/Loss changes
    Date = []
    Profit_Loss = []
    Profit_Loss_Change = []
    
    for row in budget_data:
        # Append to update the Date list
        Date.append(row[0])
        Total_Months = len(Date)
        # Append to update the Profit/Loss list
        Profit_Loss.append(int(row[1]))
        # Calculate the Net total from the final Profit/Loss list
        Net_Total = sum(Profit_Loss)
    
    # Use the final Profit/Loss list to generate/update the list for Profit/Loss changes
    for i in range(1, len(Profit_Loss)):
        Profit_Loss_Change.append(Profit_Loss[i] - Profit_Loss[i-1])
        
        # Calculate the average change of the Profit/Loss changes
        Average_Change = round(sum(Profit_Loss_Change)/len(Profit_Loss_Change), 2)

        # Determine the date and amount of the greatest increase in profits
        Greatest_Inc_Amount = max(Profit_Loss_Change)
        Greatest_Inc_Date = Date[Profit_Loss_Change.index(Greatest_Inc_Amount)+1]

        # Determine the date and amount of the greatest decrease in losses
        Greatest_Dec_Amount = min(Profit_Loss_Change)
        Greatest_Dec_Date = Date[Profit_Loss_Change.index(Greatest_Dec_Amount)+1]

# Print results to terminal        
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {Total_Months}')
print(f'Total: ${Net_Total}')
print(f'Average Change: ${Average_Change}')
print(f'Greatest Increase in Profits: {Greatest_Inc_Date} (${Greatest_Inc_Amount})')
print(f'Greatest Decrease in Profits: {Greatest_Dec_Date} (${Greatest_Dec_Amount})')

# Set output variable to hold the result info
output = ("Financial Analysis\n"
"----------------------------\n"
f'Total Months: {Total_Months}\n'
f'Total: ${Net_Total}\n'
f'Average Change: ${Average_Change}\n'
f'Greatest Increase in Profits: {Greatest_Inc_Date} (${Greatest_Inc_Amount})\n'
f'Greatest Decrease in Profits: {Greatest_Dec_Date} (${Greatest_Dec_Amount})')

# Specify the path and name of the output file to write to
output_file = os.path.join('Analysis', 'Result1.txt')

# Open the output file using "write" mode
with open(output_file, 'w') as resultfile:
    # Write output content to the output file
    resultfile.write(output)