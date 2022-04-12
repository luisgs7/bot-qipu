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

        taf = response.css("p")[7]
        taf = taf.css("p::text").get()

        meta = response.css("p")[6]
        meta = meta.css("p::text").get()

        cartas_text = response.css("h4.heading-primary")[4]
        cartas_text = cartas_text.css("h4.a")

        cartas = response.css("ul.list-primary")[0]
        cartas = cartas.css("a::text").getall()
        
        # xpath='descendant-or-self::p/text()
        # response.xpath('//title/text()').get()
        #taf = response.xpath('//p/text()').get()
    
        print(f"\nNascer do Sol: {sol}")
        print(f"Entardecer: {lua}")
        print(f"TAF: {taf}\n")
        print(f'META: {meta}\n')  
        print(f'CARTAS: {cartas[1]}\n')      
