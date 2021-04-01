# Modules
import os
import csv

# Set path for file
dirname = os.path.dirname(__file__)
budget_csv = os.path.join(dirname, "Resources", "budget_data.csv")

# Define variables and lists
total_months = 0
net_total = 0
previous_value = 0
total_change = 0
months = []
total_net = []
change_list = []

# Open the CSV
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Define header
    header = next(csv_reader)

# Create loop through csv_reader
    for row in csv_reader:

        # Define current_month, add to list, create a variable for the lenght of the month list
        current_month = (row[0])        
        months.append(current_month)
        months_count = len(months)

        # Define current_net, change_value, add change value to the change_list
        current_net = int(row[1])        
        change_value = int(current_net - previous_value)  
        change_list.append(change_value)
        
        # Reset previous_value
        previous_value = int(row[1]) 
        
        # Add current_net to total_net list and make the sum of that list
        total_net.append(current_net)
        net_total = sum(total_net)

        # Clean change_list and the months list of the first row
        change_list_cleaned = change_list[1:]
        months_cleaned = months[1:]
        
# Define average_change       
average_change = round(sum(change_list_cleaned) / len(change_list_cleaned), 2)

# greatest_increase and greatest_decrease
greatest_increase = max(change_list_cleaned)
greatest_decrease = min(change_list_cleaned)

# find position of greatest_increase and greatest_decrease
max_index = change_list.index(greatest_increase)
max_month = months[max_index]
min_index = change_list.index(greatest_decrease)
min_month = months[min_index]

# Print the results to the terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {months_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})")

# Specify the file to write to
PyBank_results = os.path.join(dirname, "Analysis", "PyBank_Results.txt")

# Write the txt file
with open(PyBank_results, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {months_count}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\n")