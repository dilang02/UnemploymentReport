import json
import os
import requests
from dotenv import dotenv

load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

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
