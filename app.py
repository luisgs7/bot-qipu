#!/usr/bin/python
# -*- coding: utf-8 -*
'''Python Bot'''
import scrapy

class Bot(scrapy.Spider):
    '''Class Bot extendes the Spider'''
    name = "AISWEB"

    print("\nBem vindo ao bot AISWEB, digite o código do aeródromos que deseja ter informações:")
    codigo = input().upper()

    url = f'https://aisweb.decea.mil.br/?i=aerodromos&codigo={codigo}'

    start_urls = [url]

    def parse(self, response):
        print("########################################")

        try:
            sol = response.css("div.col-6")[0]
            sol = sol.css("h4.mt-0 sunrise::text").get()

            lua = response.css("div.text-left")[0]
            lua = lua.css("h4.mt-0 sunset::text").get()

            taf = response.css("div.col-lg-4")
            taf = taf.css("p")[3]
            taf = taf.css("p::text").get()

            metar = response.css("div.order-sm-12")
            metar = metar.css("p")[2]
            metar = metar.css("p::text").get()

            cartas = response.css("ul.list-primary")
            cartas = cartas.css("a::text").getall()

            print("\nCartas Disponíveis: \n")
            i = 0
            for carta in cartas:
                i += 1
                print(f'CARTA {i}: {carta}')

            print(f"\nNascer do Sol: {sol}")
            print(f"Pôr do Sol de Hoje: {lua}\n")
            print(f"TAF: {taf}\n")
            print(f'METAR: {metar}\n')
            print("########################################")
            return

        except Exception as e:
            print("\nVocê forneceu um ICAO Incorreto!!\n")
            return
