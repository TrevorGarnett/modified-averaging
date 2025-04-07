import yfinance as yf
import pandas as pd


SCHD = yf.Ticker("SCHD")

history = SCHD.history(start = "2012-01-01",        # Get data from 2012-01-01
                        end = "2024-12-31",         # to 2024-12-31
                        interval="1d")              # Get daily data

history = history.resample('W-MON').first()

print((SCHD.dividends)) # Print the dividends

print("Data from 2012-01-01 to 2024-12-31")

num_shares = 0
for year in (history.index.year.unique()):
    yearly_spend = 7000
    current_year = history[history.index.year == year]
    current_year.reset_index(drop=False, inplace=True) # Reset the index to get week number
    for week_num, week in current_year.iterrows():
        weekly_spend = yearly_spend / (len(current_year) - week_num) # Calculate weekly spend
        num_shares += weekly_spend / week["Open"]   # Calculate number of shares bought this week
        yearly_spend -= weekly_spend                                    # Decrease yearly spend by weekly spend

print("Total Amount Spent: ", f"${7000 * len(history.index.year.unique()):,.2f}") # Print the total amount spent
print("Total Shares Bought: ", num_shares) # Print the total number of shares bought

total_amount = num_shares * SCHD.history().iloc[-1]['Close'] # Calculate the total dollar amount of shares bought
print(f"\nTotal value: ${total_amount:,.2f}") # Print the total value of the shares bought