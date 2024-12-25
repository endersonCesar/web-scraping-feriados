import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import re
from datetime import datetime

ano_atual = datetime.now().year
print(ano_atual)
def obter_feriados(url, cidade_formatada_id):
    response = requests.get(url)
    if response.status_code != 200:
        print('Erro ao acessar a URL.')
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    feriados = {
        'federais': [],
        'estaduais': [],
        'municipais': [],
        'nao_classificados': [],
        'facultativo': []
    }

    div_feriados = soup.find('div', {'id': 'Feriados '+cidade_formatada_id+' '+str(ano_atual)})
    if not div_feriados:
        print('Div de feriados não encontrada.')
        return

    lista_feriados = div_feriados.find('ul', {'class': 'multi-column'})
    if not lista_feriados:
        print('Lista de feriados não encontrada.')
        return

    itens = lista_feriados.find_all('li')
    for item in itens:
        div = item.find('div')
        title = div['title']
        data_nome = div.find('span').text.strip()

        if 'Nacional' in title:
            feriados['federais'].append(data_nome)
        elif 'Estadual' in title:
            feriados['estaduais'].append(data_nome)
        elif 'Municipal' in title:
            feriados['municipais'].append(data_nome)
        elif 'Facultativo' in title:
            feriados['facultativo'].append(data_nome)
        else:
            feriados['nao_classificados'].append(data_nome)

    return feriados

def funca_base(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Erro ao acessar a URL.')
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.find('div', {'id': 'menu_direito'})
    if not div:
        print('Div de div_estados não encontrada.')
        return
    return div


def obter_cidade(value):
    print(value)
    url = 'https://www.feriados.com.br/feriados-estados-'+value.lower()+'.php?ano='+str(ano_atual)
    
    # Configure o driver do navegador (neste exemplo, Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Aguarde até que o select de estados esteja presente
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'estado')))
    
    # Selecione um estado para carregar as cidades
    select_estado = Select(driver.find_element(By.ID, 'estado'))
    select_estado.select_by_value(value)  # Substitua pelo valor do estado desejado

    # Aguarde até que o select de cidades esteja presente e carregado
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cidade')))
    
    # Obtenha todas as opções do select de cidades
    select_cidade = Select(driver.find_element(By.ID, 'cidade'))
    cidades = [{'value': option.get_attribute('value'), 'text': option.text} for option in select_cidade.options if option.get_attribute('value')]

    print(cidades)
    
    # Feche o navegador
    driver.quit()

    return cidades

def obter_estado():
    url ='https://www.feriados.com.br/feriados-amapa-ap.php?ano='+str(ano_atual)
    div_estados = funca_base(url)
    lista_estados = div_estados.find('select', {'id': 'estado'})

    estados_cidades = []
    for option in lista_estados.find_all('option'):
        value = option.get('value')
        if value and value != "NONE":
            cidades = obter_cidade(value)
            estados_cidades.append({'estado': value, 'cidades': cidades})
            cidades =[]

    return estados_cidades




estados_cidades = obter_estado()
todos_feriados = []
for item in estados_cidades:
    for cidade in item['cidades']:
        cidade_formatada_id = cidade['text'].upper()
        print(cidade_formatada_id)
        cidade_formatada = re.sub(r'[^a-zA-Z0-9]', '_', cidade['value'].lower().replace(' ', '_').replace("'", ""))
        url = 'https://www.feriados.com.br/feriados-'+cidade_formatada.lower()+'-'+item['estado'].lower()+'.php?ano='+str(ano_atual)
        feriados = obter_feriados(url,cidade_formatada_id)
        if feriados:
            print('Feriados de '+cidade['value']+' - '+item['estado']+':')
            for feriado in feriados['federais']:
                print(feriado)
            for feriado in feriados['estaduais']:
                print(feriado)
            for feriado in feriados['municipais']:
                print(feriado)
            for feriado in feriados['facultativo']:
                print(feriado)
            for feriado in feriados['nao_classificados']:
                print(feriado)
            print('\n')
        todos_feriados.append({'cidade': cidade['value'], 'estado': item['estado'], 'feriados': feriados})
print(feriados)
with open('todos_feriados.json', 'w', encoding='utf-8') as f:
    json.dump(todos_feriados, f, ensure_ascii=False, indent=4)

print("Dados exportados para todos_feriados.json")
