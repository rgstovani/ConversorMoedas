import PySimpleGUI as sg
import requests
import time
from datetime import datetime
from threading import Event
lista = ['EUR','USD','CAD','AUD','JPY','BOB','PYG','ARS','COP']

def cotar():
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,CAD-BRL,EUR-BRL,ARS-BRL,JPY-BRL,AUD-BRL,PYG-BRL,COP-BRL,BOB-BRL')
    cotacao = requisicao.json()
    valor = float(cotacao[moeda]['bid'])
    atualizacao = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    return (valor, atualizacao)

def tela_menu():
    layout = [  [sg.Text('Escolha a moeda a ser cotada.')],
                [sg.Button('EUR'), sg.Button('USD'), sg.Button('CAD')],
                [sg.Button('AUD'), sg.Button('JPY'), sg.Button('BOB')],
                [sg.Button('PYG'), sg.Button('ARS'), sg.Button('COP')] ]
    return sg.Window('Cotação de Moedas', layout, finalize=True)


def tela_config():
    layout = [[sg.Text(f'A moeda a ser cotada é: {moeda_escolhida}')],
              [sg.Text(f'A cotação atual é: {cotar()[0]} ')],
              [sg.Text('Digite o valor que procura: '), sg.InputText(5.40, key='valor_proc')],
              [sg.Text('Digite o tempo de atualização: '), sg.InputText(10, key='tempo_atualizacao')],
              [sg.Button('Avançar'), sg.Button('Fechar')]]
    return sg.Window('Configurações', layout, finalize=True)


def tela_cotacao():
    layout = [[sg.Text(f'A moeda a ser cotada é: {moeda}')],
              [sg.Text(f'Avisaremos quando chegar em: {preco_alvo}')],
              [sg.Text(f"A cotação atual é: {cotar()[0]}.", key='loop_cotacao')],
              [sg.Text(f"Atualizado em: {cotar()[1]}.", key='loop_atualiz')],
              [sg.Button('Atualizar'), sg.Button('Fechar')]]
    return sg.Window('Cotando...', layout, finalize=True)

janela1, janela2, janela3 = tela_menu(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if (window == janela1 and event == sg.WIN_CLOSED) or (window == janela2 and event == sg.WIN_CLOSED) or (window == janela3 and event == sg.WIN_CLOSED) or (window == janela2 and event == 'Fechar') or (window == janela3 and event == 'Fechar'):
        break

    elif window == janela1 and event in lista:
        moeda_escolhida = (event)
        moeda = (moeda_escolhida+'BRL')
        janela1.hide()
        janela2 = tela_config()

    elif window == janela2 and event == 'Avançar':
        preco_alvo = values['valor_proc']
        tempo = values['tempo_atualizacao']
        janela2.hide()
        janela3 = tela_cotacao()

    elif window == janela3 and event == 'Inicio':
        janela3.hide()
        janela1 = tela_menu()

    elif window == janela3 and event == 'Atualizar':
        #Event().wait(5)
        cotar()
        janela3['loop_cotacao'].update(f"A cotação atual é: {cotar()[0]}.")
        janela3['loop_atualiz'].update(f"Atualizado em: {cotar()[1]}.")

