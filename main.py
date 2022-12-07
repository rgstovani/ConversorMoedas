import requests
import time
from datetime import datetime
from tkinter import messagebox

opcao = [1,2,3,4,5,6,7,8,9]
moeda_escolhida = {1: 'Euro', 2: 'Dólar Americano', 3: 'Dólar Canadense', 4: 'Dólar Australiano', 5: 'Iene Japonês', 6: 'Boliviano', 7: 'Guarani Paraguaio', 8: 'Peso Argentino', 9: 'Peso Colombiano'}
sigla_moeda = {1: 'EURBRL', 2: 'USDBRL', 3: 'CAD', 4: 'AU', 5: 'JPY', 6: 'BOB', 7: 'PYG', 8: 'ARS', 9: 'COP'}

def cotar():
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,CAD-BRL,EUR-BRL,ARS-BRL,JPY-BRL,AUD-BRL,PYG-BRL,COP-BRL,BOB-BRL')
    cotacao = requisicao.json()
    moeda = float(cotacao[sigla_moeda[escolha]]['bid'])
    return moeda

def cria_linha():
    print('#~' * 40)

def cria_linha2():
    print('..' * 40)

def hora_de_comprar():
    messagebox.showwarning(title='Alerta', message='O Euro atingiu o valor desejado')

#Bem vindo
cria_linha()
print(f"{'Bem vindo':^80}")
cria_linha()
print(f"{'Vamos configurar o cotador de moeda':^80}")
cria_linha()

#Escolha da moeda
while True:
    try:
        print('Escolha a moeda: \n ( 1 ) Euro ( 2 ) Dólar Americano ( 3 ) Dólar Canadense\n ( 4 ) Dólar Australiano ( 5 ) Iene Japonês ( 6 ) Boliviano\n ( 7 ) Guarani Paraguaio ( 8 ) Peso Argentino ( 9 ) Peso Colombiano')
        escolha = int(input('Digite o numero correspondente: '))
        cria_linha()
        if escolha in opcao:
            print('Voce escolheu a moeda',moeda_escolhida[escolha])
            cria_linha()
            break
    except ValueError:
        print('Opção invalida!. \nVoce deve escolher um numero de 1 a 9')
        cria_linha()
        pass

#Cotação da moeda
print(f'O valor atual do {moeda_escolhida[escolha]} é ',cotar())
while True:
    try:
        preco_alvo = float(input('Digite o valor desejado: R$'))
        cria_linha()
        break
    except ValueError:
        print('Valor Invalido. Use o ponto para casas decimais.')
        cria_linha()

#tempo de atualização
while True:
    tempo_de_atualizacao = input('Digite o tempo de atualização (em segundos):')
    cria_linha()
    if tempo_de_atualizacao.isnumeric():
        tempo = int(tempo_de_atualizacao)
        break
    else:
        print('Digite apenas numeros.!')

#Execução
cria_linha2()
print(f"{'Agora você pode minimizar, te avisaremos quando atigir o valor desejado.':^80}")
cria_linha2()

while True:
    cotar()
    print('Atualizado em: ', datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    print('Cotação Atual:', cotar())
    if (cotar() <= preco_alvo):
        print('Bora comprar!')
        hora_de_comprar()
    elif (cotar() > preco_alvo):
        print('Ainda está caro!')
        cria_linha2()
    time.sleep(tempo)
