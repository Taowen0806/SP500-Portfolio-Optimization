# Download recent 5 years of DJIA assets data from Yahoo Finance
# Use the adjusted close price
djia_tickers = ['AAPL', 'AMGN', 'AMZN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'GS', 'HD', 
              'HON', 'IBM', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'NVDA', 'PG',
              'SHW', 'TRV', 'UNH', 'V', 'VZ', 'WMT']
# Note that the start date is inclusive but end date is exclusive
data = yf.download(djia_tickers, start="2020-09-23", end="2025-09-24", auto_adjust=True)['Close']

!mkdir 'yahoo_data'
data.to_csv('yahoo_data/djia_5yrs.csv')
stockFileName = 'yahoo_data/djia_5yrs.csv'
df = pd.read_csv(stockFileName, nrows=rows, index_col=0, parse_dates=True)
df.info()


# Initial setup and storage with TsTables
!pip install git+https://github.com/yhilpisch/tstables.git
# class to use as the table description
# first column must be called 'timestamp' and have type Int64
desc_dict = {'timestamp': tb.Int64Col(pos=0)}
for i, stock in enumerate(stocks, start=1):
    desc_dict[stock] = tb.Float64Col(pos=i)
desc = type('desc', (tb.IsDescription,), desc_dict)
# create a new HDF5 file
h5 = tb.open_file('data/clean_sp500_3yrs.h5ts', 'w')
# create a new time-series data object under the root directory called 'data'
ts = h5.create_ts('/', 'data', desc)
# apped the stocks historical data
ts.append(df)
h5.close()