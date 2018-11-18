import os
import csv

py_bank = os.path.join(r"C:\Users\khanh\Desktop\UCIRV201810DATA4\Homeworks\HW03-Python\PyBank", "Resources", "budget_data.csv")
row_count = 0
months = 0
total_Profit_Loss = 0
change1 = change2 = 0
average_change = 0
total_change = 0
original = 0
recent = 0
max_increase = 0
max_decrease = 0

with open(py_bank, 'r') as csvfile:
   py_bank = csv.reader(csvfile, delimiter=',')
   next(py_bank)

   for row in py_bank:
       months += 1
       total_Profit_Loss += float(row[1])
       recent = float(row[1])

       if original != 0 and recent != 0:
           change2 = recent - original
           if(change2 >= change1):
               if(change2 >= max_increase):
                   GI_row = row[0]
                   max_increase = change2
           elif(change2 < change1):
               if(change2 < max_decrease):
                   max_decrease = change2
                   GD_row = row[0]


       change1 = change2
       total_change += change2
       print(f"{row[0]}:  {change2}")
       original = int(row[1])

   average_change = total_change/(months - 1)


print("Total Months", months)
print("Total Profits", total_Profit_Loss)
print("Average Change", round(average_change, 2))
print(f"Max Increase in Profits: {GI_row} ${max_increase}")
print(f"Max Decrease in Profits: {GD_row} ${max_decrease}")