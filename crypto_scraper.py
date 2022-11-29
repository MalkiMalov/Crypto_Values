import requests
import os
from prettytable import PrettyTable

api_key="pk_01d923271ccc49379073ef43f8a054ba"
#api_key=os.environ.get("api_key")

class CryptoCurrency:
    base_url="https://cloud.iexapis.com/stable/crypto"
    prices=[]
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
        self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"
    
    @property
    def price(self):
        req = requests.get(self.complete_url).json() #Convert the JSON data to a python dictionary
        return float(req.get('price'))
     
    def add_prices_to_list(self):
        CryptoCurrency.prices.append(
            [self.symbol, self.price]
        )

    @staticmethod
    def prices_table(col='base'):
        pt=PrettyTable([f"{CryptoCurrency.colors[col]}Crypto Name{CryptoCurrency.colors['base']}",
                        f"{CryptoCurrency.colors[col]}Price{CryptoCurrency.colors['base']}"
                        ])
        pt.add_rows(CryptoCurrency.prices)
        return pt
    
    @staticmethod
    def clean_prices():
        CryptoCurrency.prices.clear()

        
    @staticmethod
    def show_prices(col='base'):
        assert col in CryptoCurrency.colors.keys()
        print(CryptoCurrency.prices_table(col=col))
        