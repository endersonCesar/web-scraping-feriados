# Web Scraping de Feriados do Amapá

Este repositório contém um script em Python para realizar web scraping no site [Feriados.com.br](https://www.feriados.com.br/feriados-amapa-ap.php), com o objetivo de coletar todos os feriados do estado do Amapá. O script utiliza as bibliotecas `requests`, `BeautifulSoup`, e `selenium`, além de outras dependências.

## Funcionalidades

- **Coleta de feriados:** Extrai informações sobre todos os feriados do estado do Amapá listados no site.
- **Manipulação dinâmica:** Usa Selenium para lidar com elementos dinâmicos na página, se necessário.
- **Armazenamento de dados:** Os feriados coletados são armazenados em um arquivo JSON para uso posterior.

## Requisitos

Certifique-se de que você tem os seguintes requisitos instalados:

- Python 3.7 ou superior
- Google Chrome (ou outro navegador suportado pelo Selenium)
- WebDriver compatível com o navegador

### Bibliotecas Python

Instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```
requests
beautifulsoup4
selenium
```

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Configure o WebDriver:**
   - Baixe o WebDriver correspondente ao navegador que você usa.
   - Certifique-se de que o WebDriver está no PATH ou especifique o caminho no script.

3. **Execute o script:**
   ```bash
   python feriados_scraper.py
   ```

4. **Saída:**
   - Os dados coletados serão salvos em um arquivo chamado `feriados_amapa.json` no mesmo diretório do script.

## Estrutura do Repositório

```
┌── feriados_scraper.py       # Script principal
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## Detalhes do Script

O script realiza as seguintes etapas:

1. **Acessa a página do site Feriados.com.br** utilizando `requests` ou `selenium` (caso elementos dinâmicos sejam necessários).
2. **Extrai informações relevantes**, como data e descrição do feriado, usando `BeautifulSoup` para parsing do HTML.
3. **Formata os dados** em um dicionário Python.
4. **Salva os dados** no formato JSON para reutilização.

## Contribuição

São bem-vindas sugestões, relatórios de problemas (issues) e pull requests. Sinta-se à vontade para contribuir!

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

