import os
import csv

votes = 0
election_data = os.path.join(r"C:\Users\khanh\Desktop\UCIRV201810DATA4\Homeworks\HW03-Python\PyPoll\Resources\election_data.csv")
Khan = Correy = Li = Tooley = 0
percentage_Khan = percentage_Correy = percentage_Li = percentage_Tooley = 0

with open(election_data, "r") as csvfile:
   py_poll = csv.reader(csvfile, delimiter=',')
   next(py_poll)

   for row in py_poll:
       votes += 1
       if row[2] == "Khan":
           Khan += 1
       elif row[2] == "Correy":
           Correy += 1
       elif row[2] == "Li":
           Li += 1
       elif row[2] == "O'Tooley":
           Tooley += 1

percentage_Khan = (Khan / votes) * 100
percentage_Correy = (Correy / votes) * 100
percentage_Li = (Li / votes) * 100
percentage_Tooley = (Tooley / votes) * 100

print("Election Results")
print(f"Total votes: ({votes})")

winner = max(Khan, Correy, Li, Tooley)

if(winner == Khan):
    print(f"Winner: Khan ({winner})")
if (winner == Correy):
    print(f"Winner: Correy ({winner})")
if (winner == Li):
    print(f"Winner: Li ({winner})")
if (winner == Tooley):
    print(f"Winner: O'Tooley ({winner})")

print(f"Khan: {round(percentage_Khan,3)}% ({Khan})")
print(f"Correy: {round(percentage_Correy,3)}%  ({Correy})")
print(f"Li: {round(percentage_Li,3)}%  ({Li})")
print(f"O'Tooley: {round(percentage_Tooley,3)}%   ({Tooley})")


