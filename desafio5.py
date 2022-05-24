import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

todos_paises = []

requisicao = requests.get(url)
html_doc = requisicao.text
soup = BeautifulSoup(html_doc, 'html.parser')

tabela = soup.find("table")
linhas = tabela.find_all("tr")[1:]

for linha in linhas:

  items = linha.find_all("td")

  name = items[0].text
  moeda_nome = items[1].text
  code = items[2].text

  if moeda_nome != "No universal currency":
    pais = {
      'pais': name,
      'codigo': code
    }
    todos_paises.append(pais)
    
def menu():
  try:
    escolha = int(input("Qual numero? >>"))
    if escolha > len(todos_paises):
      print('numero maior do q pode')
      menu()
    else:
      resultado = todos_paises[escolha]
      print(f"Vc escolheu {resultado['pais']} , e a moeda é {resultado['codigo']}")
  except:
    print('mano, isso nao é um numero')
    menu()


print("BEM VINDO AO NOSSO CONSULTADOR DE MOEDA! SELECIO UMA OPCAO DO MENU")

for numera, pais in enumerate(todos_paises):
  print(f"## {numera} - {pais['pais']}")

menu()
