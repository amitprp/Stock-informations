# *************** HOMEWORK 6 ***************
# TODO: GOOD LUCK!
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt


# ****************************************************** Start **********************************************

def get_object_single_stock(name_stock, start='1980-01-01', end=date.today(), interval='5d'):
    name_stock = yf.Ticker(name_stock)
    stock_historical = name_stock.history(start=start, end=end, interval=interval)
    return stock_historical


def get_object_multiple_stock(list_stocks, start='1980-01-01', end=date.today(), interval='5d'):
    for stock in list_stocks:
        stock_df_dict = {list: get_object_single_stock(stock, start, end, interval)}
    return stock_df_dict


def get_object_multiple_stock_v2(list_stocks, start='1980-01-01', end=date.today(), interval='5d'):
    multiple_stocks_df = yf.download(' '.join(list_stocks[::-1]), start=start, end=end, interval=interval,
                                     group_by='ticker')
    return multiple_stocks_df


# ******************************************************PART 1 - info**********************************************
def daily_return(stock):
    daily_return_for_stock = stock[['Close']].pct_change() * 100
    std = daily_return_for_stock.std()['Close']
    dr_sum = 0
    dr_counter = 0
    daily_return_for_stock.dropna(inplace=True)
    for dr in daily_return_for_stock['Close']:
        dr_counter += 1
        dr_sum += dr
    avg = dr_sum / dr_counter

    return avg, std


def information_of_stock(name_stock):
    stock_div = yf.Ticker(name_stock)
    return stock_div.info['dividendRate'], stock_div.info['website']


# ******************************************************PART 2 - plot**********************************************
def plot_price(stock):
    close_price = stock['Close']
    fig, stk_plot = plt.subplots()
    stk_plot.plot(close_price, color='#444454')
    stk_plot.set_xlabel('Years')
    stk_plot.set_ylabel('Close Price')
    stk_plot.set_title('Close Price for Date')
    return stk_plot


# ******************************************************PART 3 - file**********************************************
def save_dividends(name_stock):
    stock = yf.Ticker(name_stock)
    stk_div = stock.dividends
    div_med = stk_div.median()
    with open('Dividends.csv', 'w') as div_csv:
        div_csv.write(f"Date,Dividends\n")
        for index, div in stk_div.iteritems():
            if div >= div_med:
                div_csv.write(f"{index},{div}\n")

