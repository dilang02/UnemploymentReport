from getpass import getpass
import json
API_KEY = getpass("Please input your AlphaVantage API Key: ")

import requests
import json

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
print(type(parsed_response))
data = parsed_response["data"]

# Challenge A
print("-----------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{data[0]['value']}%","as of",data[0]["date"])

# Challenge B

from statistics import mean

this_year = [d for d in data if "2022-" in d["date"]]
rates_this_year = [float(d["value"]) for d in this_year]
print("---------------------")
print("AVG. UNEMPLOYMENT THIS YEAR:",f"{mean(rates_this_year)}%")
print("NO MONTHS:",len(this_year))

# Challenge C
from plotly.express import line
dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]
fig = line(x=dates,y=rates,title="United States Unemployment Rate over Time",labels={"x":"Month","y":"Unemployment Rate"})
fig.show()

# CSV A-C

from pandas import read_csv
request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"
df = read_csv(request_url)
print(df.head())
print(df.columns)
print(len(df))

print("----------------------")
print("LATEST UNEMPLOYMENT RATE:")
first_row = df.iloc[0]
print(f"{first_row['value']}%","as of",first_row["timestamp"])

this_year_df = df[df["timestamp"].str.contains("2022-")]
print(this_year_df)
print("-------------------")
print("AVG. UNEMPLOYMENT THIS YEAR:",f"{this_year_df['value'].mean()}%")
print("NO MONTHS:",len(this_year_df))

from plotly.express import line
fig = line(x=df["timestamp"],y=df["value"],title="United States Unemployment Rate over time",labels={"x":"Month","y":"Unemployment Rate"})
fig.show()