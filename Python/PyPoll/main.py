#Import Packages
import pandas as pd

#Establish Dataframe
df = pd.read_csv("../Pypoll/election_data.csv")

#List of all votes
candidate = df["Candidate"]

#Number of voters
voters = len(df["Voter ID"])

#Establish candidates
khan = 0
otooley = 0
correy = 0
li = 0

#Run a loop for each candidate totalling votes for each
for i in candidate: 
    if i == "Khan":
        khan = khan + 1
    if i == "Li":
        li = li + 1
    if i == "O'Tooley":
        otooley = otooley + 1
    if i == "Correy":
        correy = correy + 1
        
#Percent of vote for each candidate
khan_p = khan / voters *100
otooley_p = otooley / voters *100
correy_p = correy / voters*100
li_p = li / voters*100
khan_p = int(khan_p) 
otooley_p = int(otooley_p)
correy_p = int(correy_p)
li_p = int(li_p)

#Establish a winner
if khan > otooley: 
    ko = khan 
else: 
    ko = otooley
if ko > correy: 
    cko = ko
else: 
    cko = correy
if cko > li: 
    winner = cko 
else: 
    winner = li

if winner == correy:
    name = "Correy"
elif winner == li:
        name = "Li"
elif winner == khan:
        name = "Khan"
else: 
    name = "O'tooley"
    
#Print Results
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(voters))
print("--------------------------------")
print("Khan: " + str(khan_p) + "% (" + str(khan) + ")")
print("Correy: " + str(correy_p) + "% (" + str(correy) + ")")
print("O'Tooley: " + str(otooley_p) + "% (" + str(otooley) + ")")
print("Li: " + str(li_p) + "% (" + str(li) + ")")
print("--------------------------------")
print("Winner: " + name)