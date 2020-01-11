#Import Packages
import pandas as pd
import numpy as np

#Establish dataframe
df = pd.read_csv("../Pybank/budget_data.csv")

#Number of Months in dataframe
months = len(df["Date"])

#Total Profit
profit = sum(df["Profit/Losses"])

#Add change in profts for each month to the dataframe
df['diff'] = df['Profit/Losses'].shift(1) - df['Profit/Losses']
diff = df['diff']

#Max and min changes in profits
d = df['Profit/Losses'].diff()
max_profit = df.loc[d.idxmax(),'diff']
min_loss = df.loc[d.idxmin(), 'diff']

#Find the max and min month
max_month = df.loc[d.idxmax(),'Date']
min_month = df.loc[d.idxmin(),'Date']

#Establish total change/months for average change
tot_change = sum(diff[1:months])/months

#Print Results
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(months))
print("Total Profit: " + str(profit))
print("Average Change: " + str(tot_change))
print("Greatest Increase in Profits: "+ str(max_month) + "("+str(max_profit)+")")
print("Greatest Decrease in Profits: "+ str(min_month) + "("+ str(min_loss)+")")