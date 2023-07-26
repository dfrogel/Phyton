"""
Este módulo faz a leitura e impressão do nome e preços dos 6 primeiros produtos
exibidos na página web: https://www.magazineluiza.com.br/selecao/ofertasdodia/
"""

import unicodedata
import requests
from bs4 import BeautifulSoup


def normalize_text(text):
    """
    Remove caracteres especiais de um texto.

    Args:
        text (str): O texto que será normalizado.

    Returns:
        str: O texto normalizado sem caracteres especiais.
    """
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")


def scrape_magazine_luiza():
    """
    Obtém informações dos produtos (nome e preço) a partir de uma URL da página web.

    Args:
        product_url (str): A URL da página web com os produtos.

    Returns:
        None
    """
    url = "https://www.magazineluiza.com.br/selecao/ofertasdodia/"
    response = requests.get(url, timeout=10)  # Timeout de 10 segundos

    if response.status_code != 200:
        print("Falha ao acessar a página.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("li", class_="sc-gbWDHf jTBHBv")

    print("Ofertas do dia (6 primeiros produtos) - MAGALU:")
    for i, product in enumerate(products[:6], start=1):
        name = product.find("h2", class_="sc-euWMRQ daTFjj").text.strip()
        price = product.find(
            "p", class_="sc-kpDqfm eCPtRw sc-hYmls gMDrLP"
        ).text.strip()

        # Normaliza o texto para remover caracteres especiais
        name = normalize_text(name)
        price = normalize_text(price)

        print(f"\n{i}. Produto: {name}\n   Valor: {price}\n")


if __name__ == "__main__":
    scrape_magazine_luiza()
