from crypto_scraper import CryptoCurrency
import time
import os


if __name__ == '__main__':
    """crypto1=CryptoCurrency(symbol="btcusd")
    print(CryptoCurrency.all)
    CryptoCurrency.show_prices('yellow')"""
    
    crypto1=CryptoCurrency(symbol="btcusd")
    crypto2=CryptoCurrency(symbol="ethusd")
    while(True):
        crypto1.update_price()
        crypto2.update_price()
        CryptoCurrency.show_prices('yellow')
        time.sleep(3)
        os.system("cls")  #clean the terminal