import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyfiglet


def generate_ascii_art(text, font="slant"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

print(generate_ascii_art("Kabum Searcher"))

text_input = input("insira o produto que deseja buscar: ")
price_input = int(input("insira o valor: "))
page_input = int(input("insira a quantidade de páginas que você quer buscar: "))

list_price = []
list_name = []
list_name_filtered = []

page = 0

for page in range(1, page_input + 1):
    url = "https://www.kabum.com.br/busca/" + text_input + "?page_number=" + str(page)
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.text, "html.parser")
    all_products = soup.find_all("span", class_ = "sc-d79c9c3f-0 hkwBHG sc-d55b419d-16 kaRfLk nameCard")
    all_prices = soup.find_all("span", class_ = "sc-3b515ca1-2 gABrIj priceCard")

    for product in all_products:
        product_name_filtered = product.text[:50]

    for price in all_prices:
        price_value = float(price.text.replace("R$", "").replace(".", "").replace(",", "."))
        list_price.append(price_value)

    list_price_filter = [price for price in list_price if price <= price_input]

    if list_price_filter and "placa de vídeo" in get_url.text:
        print("\n" + f"Mostrando resultados da página: {page} com valores menores ou iguais a {price_input} reais")
        columns_data = {"Name": product_name_filtered, "Preço": list_price_filter}
        df = pd.DataFrame(columns_data)
        print(df)

    else:
        print("\n" + f"Nada encontrado na página {page}")



