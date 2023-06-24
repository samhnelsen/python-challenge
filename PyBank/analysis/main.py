# import the os and csv modules
import os
import csv
import sys

# create a path to the csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# set up the lists we want to create
date = []
month_of_change = []
net_change_list = []


# set counted variables to 0 and strings to ""
total_months = 0
prev_net = 0
net_change = 0
net_monthly_avg = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""


# open and read the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # define first row as the header
    csv_header = next(csvreader)
    
    # make the next row the first row and extract so as not to append the for loop below
    first_row = next(csvreader)
    total_months += 1
    total_net = int(first_row[1])
    prev_net = int(first_row[1])
    #loop through csv
    for row in csvreader:
            
        # tracking the totals
        total_months += 1
        total_net += int(row[1])   
        
        # tracking the net change    
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #find greatest increase
        if net_change > greatest_increase:
            greatest_increase_month = row[0]
            greatest_increase = net_change
            
        #find greatest decrease    
        if net_change < greatest_decrease:
            greatest_decrease_month = row[0]
            greatest_decrease = net_change
#calculate net monthly average
net_monthly_avg = sum(net_change_list) / len(net_change_list)
#start printing           
print("Financial Analysis")   
print("----------------------------")        
#The total number of months, total net, average change, greatest increase, and greatest decrease included in the dataset
print(f'Total Months: {total_months}')        
print(f'Total: ${total_net}')
print(f'Average Change: {format(net_monthly_avg,".2f")}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
#write to txt file
with open('pybank_read_me_export.txt','w') as f:
    f.write("Financial Analysis\n")   
    f.write("----------------------------\n")        

    f.write(f'Total Months: {total_months}\n')        
    f.write(f'Total: ${total_net}\n')
    f.write(f'Average Change: {format(net_monthly_avg,".2f")}\n')
    f.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    f.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
