# (1) Load necessary libraries
import pandas as pd
import pandas_datareader.data as web
import os


# (1) Save stock_data to csv-files
def save_stock_data( source, tickers, start_date, end_date ):
    
    # (0) prepare folder in which we save the data
    if not os.path.exists('stockdata'):
        os.makedirs('stockdata')

    # (1) download data for the tickers and save it in this folder
    print( 'Download started' )
    print( 'Tickers of interest: ' + str( tickers ) + '\n' )
    for ticker in tickers:
        try:
            data = web.DataReader( ticker, 'yahoo', start_date, end_date )
            print( 'Download finished for ' + str( ticker ) )
        except Exception as e:
            print( e, 'error' )
        
        # (2) prepare the data
        
        # 2.1: We work with the opening values
        # 2.1: We work with the opening values
        data_selected = data['Open']
        
        # 2.2 Index the data by all working days between start and end
        # 2.2 Whenever the corresponding data is not present, we will in the missing value.
        # 2.2 For this we use the latest available price
        all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
        data_selected = data_selected.reindex(all_weekdays)
        data_selected = data_selected.fillna(method='ffill')

        # 2.3 Save selected data to csv-file
        data_selected.to_csv('stockdata/'+ticker+'.csv')
        
        # 2.4 Inform about status
        print( 'Data saved to stockdata/' + str( ticker ) + '.csv \n' )



# (2) Get stock_data
def get_stock_data( source, tickers, start_date, end_date ):
    
    # (1) download data of the tickers
    print( 'Download started' )
    print( 'Tickers of interest: ' + str( tickers ) )
    try:
        data = web.DataReader( tickers, 'yahoo', start_date, end_date )
        print( 'Download finished \n' )
    except Exception as e:
        print( e, 'error' )
    
    # (2) prepare the data
    
    # 2.1: We work with the opening values
    # 2.1: We work with the opening values
    data_selected = data['Open']

    # 2.2 Index the data by all working days between start and end
    # 2.2 Whenever the corresponding data is not present, we will in the missing value.
    # 2.2 For this we use the latest available price
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    data_selected = data_selected.reindex(all_weekdays)
    data_selected = data_selected.fillna(method='ffill')

    # 2.3 Extract data for each ticker
    data_selected_split = []
    for ticker in tickers:
        data_selected_split.append( data_selected.loc[:, ticker] )
    
    # now return the data
    return data_selected_split
