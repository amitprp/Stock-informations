from hw6 import *
import pandas as pd

def check_1():
    stock_obj = get_object_single_stock('AAPL', interval="5d", start='2021-09-08', end='2021-10-08')
    if not isinstance(stock_obj, pd.DataFrame):
        print("Error the type is not DataFrame")
    print(stock_obj)


def check_2():
    stocks_obj = get_object_multiple_stock(["AAPL", "MSFT"], start='2021-09-08', end='2021-10-08')
    if not isinstance(stocks_obj, dict):
        print("Error the type is not Dict")
    print(stocks_obj)


def check_3():
    stocks_obj = get_object_multiple_stock_v2(["AAPL", "MSFT"], start='2021-09-08', end='2021-10-08')
    print(stocks_obj)


# ******************************************************PART 1 - info**********************************************
def check_4():
    stock = get_object_single_stock('AAPL', end='2021-10-08', interval="1d")
    print(daily_return(stock))


def check_5():
    print(information_of_stock("BK"))


# ******************************************************PART 2 - plot**********************************************
def check_6():
    stock = get_object_single_stock('AAPL')
    axes = plot_price(stock)
    print(str(type(axes)) == "<class 'matplotlib.axes._subplots.AxesSubplot'>")


# ******************************************************PART 3 - file**********************************************
def check_7():
    import os
    save_dividends("MSFT")
    if not os.path.exists("Dividends.csv"):
        print("Error")


if __name__ == '__main__':
    check_1()
    check_2()
    check_3()
    check_4()
    check_5()
    check_6()
    check_7()
