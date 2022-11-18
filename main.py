import requests
import time
from datetime import datetime
from tkinter import messagebox

def cria_linha():
    print('#~' * 40)

def cria_linha2():
    print('..' * 40)

def hora_de_comprar():
    messagebox.showwarning(title='Alerta', message='O Euro atingiu o valor desejado')

cria_linha()
print(f"{'Bem vindo':^80}")
cria_linha()
print(f"{'Vamos configurar o cotador de Euro':^80}")
cria_linha()

while True:
    try:
        preco_alvo = float(input('Digite o valor desejado: R$'))
        break
    except ValueError:
        print('Valor Invalido. Use o ponto para casas decimais.')

while True:
    tempo_de_atualizacao = input('Digite o tempo de atualização (em segundos):')
    if tempo_de_atualizacao.isnumeric():
        tempo = int(tempo_de_atualizacao)
        break
    else:
        print('Digite apenas numeros.!')

cria_linha2()
print(f"{'Agora você pode minimizar, te avisaremos quando atigir o valor desejado.':^80}")
cria_linha2()

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
    cotacao = requisicao.json()
    euro = float(cotacao['EUR']['bid'])
    print('Atualizado em: ', datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    print('Cotação Atual:', euro)
    if (euro <= preco_alvo):
        print('Bora comprar!')
        hora_de_comprar()
    elif (euro > preco_alvo):
        print('Ainda está caro!')
        cria_linha2()
    time.sleep(tempo)
