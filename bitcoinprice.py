import requests
import os.path as path
from openpyxl import Workbook, load_workbook


BITCOIN_PRICE_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
excel_file = 'bitcoinprice.xlsx'


def Check_For_Workbook(book):
    if path.isfile(book):
        wb = load_workbook(book)
        ws = wb.active
        ws.append([123])
        return wb
    else:
        wb = Workbook()
        ws = wb.active
        ws.append([1, '\n', 2, '\n', 3])
        return wb
        

Check_For_Workbook(excel_file).save(excel_file)


def main():
    pass


def Get_Bitcoin_Price(url):
    response = requests.get(BITCOIN_PRICE_URL)
    response_json = response.json()
    bitcoin_price_str = response_json[0]['price_usd']
    bitcoin_price_round_float = round(float(bitcoin_price_str), 2)
    return bitcoin_price_round_float


#  def Write_Excel_Cell(price):




#  print(Get_Bitcoin_Price(BITCOIN_PRICE_URL))

if __name__ == "__main__":
    main()
