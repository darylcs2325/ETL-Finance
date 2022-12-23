from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import timedelta
from datetime import datetime
from requests.exceptions import ConnectionError


class ScrapperFinance():

    def __init__(self, symbol, start_date, end_date, interval='1d'):
        """Obtención de los datos financieros mediante Yahoo Finance

        Args:
            symbol (str): Símbolo de la acción
            start_date (str): Fecha de inicio (dd-mm-yyyy)
            end_date (str): Fecha final (dd-mm-yyyy)
            frequency (str): Frecuencia de muestra (1d, 1wk, 1mo)
        """

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
        self.start_date = int(datetime.strptime(start_date, '%d-%m-%Y').timestamp())
        self.end_date = int(datetime.strptime(end_date, '%d-%m-%Y').timestamp())
        self.url = (
            f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}"
            f"?period1={self.start_date}&period2={self.end_date}&"
            f"interval={interval}&events=history&includeAdjustedClose=true"
            )

    def get_historical_data(self):
        try:
            req = requests.get(self.url, headers=self.headers)
            print(req.text)
        except Exception as e:
            raise e

        return req.text

data = ScrapperFinance('CENN', '25-05-2019', '21-12-2021').get_historical_data()
