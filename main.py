import requests
import json
import time
from datetime import datetime


preco_alvo = input('Digite o valor alvo: R$')
tempo_de_atualizacao = input('Digite o tempo de atualização (em segundos):')
tempo = int(tempo_de_atualizacao)

while True:
  requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
  cotacao = requisicao.json()
  euro = cotacao['EUR']['bid']
  print(datetime.now().strftime("%d-%m-%y %H:%M:%S"))
  print('Cotação Atual:', euro)
  if (euro <= preco_alvo):
    print('Bora comprar!')
  elif (euro > preco_alvo):
    print('Ainda está caro!')
  time.sleep(tempo)