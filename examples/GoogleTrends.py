from pytrends.request import TrendReq
import csv
import pandas as pd

# Login to Google. Only need to run this once, the rest of requests will use the same session
pytrend = TrendReq()


# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['Go Compare','compare the market','confused','moneysupermarket'], timeframe='all', geo='GB')

# Interest Over Time
#interest_over_time_df = pytrend.interest_over_time()
#print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.to_json())

# myFile = open('example2.csv', 'w')
# with myFile:
#    writer = csv.writer(myFile)
#    writer.writerows(interest_by_region_df.to_json())

df = pd.read_json(interest_by_region_df.to_json())
print(df)
df.to_csv('results.csv')

print("CSV complete")

# Related Queries, returns a dictionary of dataframes
#related_queries_dict = pytrend.related_queries()
#print(related_queries_dict)

# Get Google Hot Trends data
#trending_searches_df = pytrend.trending_searches()
#print(trending_searches_df.head())

# Get Google Top Charts
#top_charts_df = pytrend.top_charts(cid='actors', date=201611)
#print(top_charts_df.head())

# Get Google Keyword Suggestions
#suggestions_dict = pytrend.suggestions(keyword='gocompare')
#print(suggestions_dict)