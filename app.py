import requests
import scrapy

print("Bem vindo ao bot AISWEB, digite o código do aeródromos que deseja ter informações:")
#codigo = input().upper()
codigo = "SBJD"



url = f'https://aisweb.decea.mil.br/?i=aerodromos&codigo={codigo}'
#response = requests.get(url)
#html = BeautifulSoup(response.text, 'html.parser')

class Bot(scrapy.Spider):
    name = "AISWEB"
    start_urls = [url] # SBJD mt-0

    def parse(self, response):
        #link = response.css('title::text').getall()
        sol = response.css("div.col-6")[0]
        sol = sol.css("h4.mt-0 sunrise::text").get()

        lua = response.css("div.text-left")[0]
        lua = lua.css("h4.mt-0 sunset::text").get()
    
        print(f"\nNascer do Sol: {sol}")
        print(f"\nEntardecer: {lua}\n")        
