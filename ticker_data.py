import yfinance as yf

import matplotlib.pyplot as plt
# %matplotlib inline

# Set the start and end date
start_date = '2022-05-10'
end_date = '2023-05-10'

# Set the ticker
ticker = 'SPY'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
firstFive = data.tail()

print(firstFive)

# Plot adjusted close price data
data['Adj Close'].plot()
plt.savefig(ticker+'.png')