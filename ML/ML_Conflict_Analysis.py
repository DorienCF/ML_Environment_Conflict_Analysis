#This will be the data collection and organization 
import pandas
df = pandas.read_csv("MLData.csv", header=None)
#headers = ["Country A Civil Liberties",	"Country B Civil Liberties",	"Country C Civil Liberties",	"Country D Civil Liberties",	"Country E Civil Liberties",	"Country F Civil Liberties",	"Country A Military Spending",	"Country B Military Spending",	"Country C Military Spending",	"Country D Military Spending",	"Country E Military Spending",	"Country F Military Spending", "Country A GDP", 	"Country B GDP",	"Country C GDP",	"Country D GDP",	"Country E GDP",	"Country F GDP",	"Conflict Confidence Ratting" ]
print(df)

