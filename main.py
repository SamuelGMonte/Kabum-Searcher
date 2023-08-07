import requests
from bs4 import BeautifulSoup
import pandas as pd

list_price = []
list_name = []
for page in range(1, 10):
    url = "https://www.kabum.com.br/busca/rtx" + "?page_number=" + str(page)
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.text, "html.parser")
    all_products = soup.find_all("span", class_ = "sc-d79c9c3f-0 hkwBHG sc-d55b419d-16 kaRfLk nameCard")
    all_prices = soup.find_all("span", class_ = "sc-3b515ca1-2 gABrIj priceCard")

    for product in all_products:
        list_name.append(product.text)

    for price in all_prices:
        list_price.append(price.text)
        list_price = [float(price.text.replace("R$", "").replace(".", "").replace(",", "."))]

    if "rtx" in ''.join(list_name).lower():
        print("\n" + f"Mostrando resultados da página: {page}")
        columns_data = {"Name": list_name, "Preço": list_price}
        df = pd.DataFrame(columns_data)
        print(df)

    else:
        print("\n" + f"Nenhum produto relacionado encontrado na página: {page}")

    integer_list = [int(list_filter) for list_filter in list_price if list_filter <= 1800]
    print(integer_list)

