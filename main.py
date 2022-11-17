import requests
import json
import time
from datetime import datetime

def cria_linha():
  print('#~' *40)

def cria_linha2():
  print('..' *40)
  
def hora_de_comprar():
  pass


cria_linha()
print(f"{'Bem vindo':^80}")
cria_linha()
print(f"{'Vamos configurar o cotador de Euro':^80}")
cria_linha()

preco_alvo = input('Digite o valor alvo: R$')
tempo_de_atualizacao = input('Digite o tempo de atualização (em segundos):')
tempo = int(tempo_de_atualizacao)

cria_linha2()
print(f"{'Agora você pode minimizar, te avisaremos quando atigir o valor desejado.':^80}")
cria_linha2()

while True:
  requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
  cotacao = requisicao.json()
  euro = cotacao['EUR']['bid']
  print('Atualizado em: ', datetime.now().strftime("%d-%m-%y %H:%M:%S"))
  print('Cotação Atual:', euro)
  if (euro <= preco_alvo):
    print('Bora comprar!')
    hora_de_comprar()
  elif (euro > preco_alvo):
    print('Ainda está caro!')
    cria_linha2()
  time.sleep(tempo)


