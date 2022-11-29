from crypto_scraper import CryptoCurrency
import time
import os


if __name__=='__main__':
    while(True):
        crypto1=CryptoCurrency(symbol="btcusd")
        crypto2=CryptoCurrency(symbol="ethusd")
        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.clean_prices()
        os.system("cls")  #clean the terminal