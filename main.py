import openpyxl
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl.styles import PatternFill

url = "https://www.kabum.com.br/busca/rtx"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

span_price = soup.find_all("span", class_="sc-3b515ca1-2 gABrIj priceCard")

product_name = soup.find_all("span", class_="sc-d79c9c3f-0 hkwBHG sc-d55b419d-16 kaRfLk nameCard")

workbook = openpyxl.load_workbook("preços.xlsx")

columns_data = []

worksheet = workbook["Shell"]
cel

products_names = []
for products in product_name:
    product_append = products.text
    products_names.append(product_append)


span_prices = []
for span in span_price:
    span_append = span.text
    span_prices.append(span_append)

#print (products_list)
columns_data={"Nome": products_names, "Preço": span_prices}
df = pd.DataFrame(columns_data)




