import requests
import os
from prettytable import PrettyTable
import pandas as pd
import numpy as np

api_key=os.environ.get("api_key")

class CryptoCurrency:
    all = []
    base_url="https://cloud.iexapis.com/stable/crypto"
    #prices=[]
    #prev_prices=[]
    colors= {
    'red' :"\033[91m",
    'green' :"\033[92m",
    'yellow' :"\033[93m",
    'blue' :"\033[94m",
    'pink': "\033[95m",
    'base': "\033[0m"
    }

    def __init__(self, symbol):
        assert symbol in ["btcusd", "ethusd"], "Uncorrect symbol. Try again."
        self.symbol=symbol
        self.price=self.price_pull()
        self.prev_price=self.price
        
        CryptoCurrency.all.append(self)
        #self.price=self.price() #האם זה תקין???
        #self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"
    
    def price_pull(self):
        req = requests.get(self.complete_url).json() #Convert the JSON data to a python dictionary
        return float(req.get('price'))    
    
    def update_price(self):
        self.prev_price=self.price
        self.price=self.price_pull()
    
    def change_value_calc(self):
        return self.price-self.prev_price
    
    @staticmethod
    def rows_prepare():
        rows_to_return=[]
        for c in CryptoCurrency.all:
            rows_to_return.append(
                [c.symbol, c.price, c.change_value_calc() ]
            )
        return rows_to_return
    
    @staticmethod
    def prices_table(col='base'):
        pt=PrettyTable([f"{CryptoCurrency.colors[col]}Crypto Name{CryptoCurrency.colors['base']}",
                        f"{CryptoCurrency.colors[col]}Price{CryptoCurrency.colors['base']}",
                        f"{CryptoCurrency.colors[col]}Change value{CryptoCurrency.colors['base']}"
                        ])
        rows=CryptoCurrency.rows_prepare()
        pt.add_rows(rows)
        return pt
    
    @staticmethod
    def show_prices(col='base'):
        assert col in CryptoCurrency.colors.keys()
        print(CryptoCurrency.prices_table(col=col))
    
    
    
    
   