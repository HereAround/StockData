# how to download stock data for free in 2019

def get_stock_data():
    tickers = ['TSLA', 'MCD', 'AAPL', 'GOOGL', 'XOM' ]
    #tickers = ['MCD', 'AAPL', 'GOOGL', 'XOM' ] # capitalize tickers
    
    start = dt.datetime(2015,3,5) # can import 5 years max with iex
    end = dt.datetime.today()
    
    if not os.path.exists('stockdata'):
        os.makedirs('stockdata')
        
    for ticker in tickers:
        print (ticker)
        try:
            df = web.DataReader(ticker, 'yahoo', start, end )
            print(df.head())
            df.to_csv('stockdata/'+ticker+'.csv')
            print(ticker,'downloaded')
            print('\n')
        except Exception as e:
            print( e, 'error' )


