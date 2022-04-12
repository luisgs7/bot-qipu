# Bot desenvolvido para Participar do processo seletivo da QIPU.

## Para utilizar o bot siga os seguintes passos:

### 01 - Primeiro crie um ambiente virtual, e em seguinda ative este ambiente virtual com os seguintes comandos:
```
python3 -m venv venv
``` 
```
source ./venv/bin/activate
``` 
### 02 - Depois instale as dependências com o próximo comando:
```
pip install -r requirements.txt
``` 
### 03 - Para inicializar o projeto execute o comando abaixo, e em seguida será solicitado que digite um ICAO válido, depois é só aguardar alguns instantes que o bot irá buscar os dados de cartas disponíveis, horários de nascer e pôr do sol de hoje e informação de TAF e METAR disponíveis.
```
scrapy runspider app.py
``` 
### 04 - Os dados serão apresentados no terminal assim como informado abaixo:

<img src="https://github.com/luisgs7/bot-qipu/blob/main/screen/01.png">