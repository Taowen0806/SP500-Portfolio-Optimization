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