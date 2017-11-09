import json
import numpy

import Columns
from trading.trader_interface import Portfolio, SharesOfCompany, StockMarketData


def read_portfolio(name: str = 'portfolio') -> Portfolio:
    file = open("../json/" + name + ".json")
    json_data = file.read()
    data = json.loads(json_data)
    file.close()

    shares_list = list()
    for share in data['shares']:
        shares_list.append(SharesOfCompany(share['name'], share['amount']))

    # pprint(shares_list[0].companyName)
    # pprint(shares_list[0].amountOfShares)
    # pprint(data['cash'])
    return Portfolio(data['cash'], shares_list)


def read_stock_market_data(name: str = 'AAPL', path: str = '../datasets/') -> StockMarketData:
    na_portfolio = numpy.loadtxt(path + name + '.csv', dtype='|S15,f8,f8,f8,f8,f8,i8',
                                 delimiter=',', comments="#", skiprows=1)
    alist = list()
    for day in na_portfolio:
        alist.append((day[Columns.DATE], day[Columns.ADJ_CLOSE]))

    data = {name: alist}

    return StockMarketData(data)