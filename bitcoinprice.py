import requests
import datetime
import accesskey  # I import url+accesskey to get conversion rate to euro
import os.path as path
from openpyxl import Workbook, load_workbook


BITCOIN_PRICE_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
excel_file = 'bitcoinprice.xlsx'


def main():
    CheckForWorkbook(excel_file).save(excel_file)


#  This function will be changed into parts
def CheckForWorkbook(book):
    if path.isfile(book):
        wb = load_workbook(book)
        ws = wb.active
        ws.append([datetime.datetime.now().strftime("%m-%w-%Y"),
        datetime.datetime.now().strftime("%H:%M")])
        return wb
    else:
        wb = Workbook()
        ws = wb.active
        ws.append(["Ημερομηνία", "Ώρα", "Τιμή σε Δολάριο", "Τιμή σε Ευρώ"])
        return wb


#  The price in Dollar of Bitcoin
def GetBitcoinPrice(url):
    response = requests.get(BITCOIN_PRICE_URL)
    response_json = response.json()
    bitcoin_price_str = response_json[0]['price_usd']
    bitcoin_price_round_float = round(float(bitcoin_price_str), 2)
    return bitcoin_price_round_float


def GetDollarToEuroConversionRate(url):
    response = requests.get(url)
    response_json = response.json()
    return response_json['quotes']['USDEUR']


if __name__ == "__main__":
    GetDollarToEuroConversionRate(accesskey.AccessKey())

