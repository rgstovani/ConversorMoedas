import PySimpleGUI as sg
import requests
import time
from datetime import datetime
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
              [sg.Text('Digite o valor que procura: '), sg.InputText(key='valor_proc')],
              [sg.Text('Digite o tempo de atualização: '), sg.InputText(key='tempo_atualizacao')],
              [sg.Button('Avançar'), sg.Button('Fechar')]]
    return sg.Window('Configurações', layout, finalize=True)


def tela_cotacao():
    layout = [[sg.Text(f'A moeda a ser cotada é: {moeda}')],
              [sg.Text(key='loop_cotacao')],
              [sg.Text(f'Avisaremos quando chegar em: {preco_alvo}')],
              [sg.Text(key='loop_atualiz')],
              [sg.Button('Iniciar'), sg.Button('Fechar')]]
    return sg.Window('Cotando...', layout, finalize=True)

janela1, janela2, janela3 = tela_menu(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if (window == janela1 and event == sg.WIN_CLOSED) or (window == janela2 and event == sg.WIN_CLOSED) or (window == janela3 and event == sg.WIN_CLOSED) or (window == janela2 and event == 'Fechar') or (window == janela3 and event == 'Fechar'):
        break

    if window == janela1 and event in lista:
        moeda_escolhida = (event)
        moeda = (moeda_escolhida+'BRL')
        janela1.hide()
        janela2 = tela_config()

    if window == janela2 and event == 'Avançar':
        preco_alvo = values['valor_proc']
        tempo = values['tempo_atualizacao']
        janela2.hide()
        janela3 = tela_cotacao()

    if window == janela3 and event == 'Inicio':
        janela3.hide()
        janela1 = tela_menu()

    if window == janela3 and event == 'Iniciar':
        cotar()
        janela3['loop_cotacao'].update(f"A cotação atual é: {cotar()[0]}.")
        janela3['loop_atualiz'].update(f"Atualizado em: {cotar()[1]}.")
        time.sleep(int(tempo))
