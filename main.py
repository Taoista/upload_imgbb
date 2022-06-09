from imgbb.client import Client
import os
import aiohttp
import asyncio
import imgbbpy
import time
import openpyxl

# * img => carpeta donde estan las imagenes
# * software para subir img en el server de imgbb exportar la lista en exel agrega los lisnks de dominio
# * la api crashe despues de x subidas de img se debe generar otra cada x tiempo

key = os.environ.get("KEY")


def create_xlsx():
    filepath = "imgs.xlsx"
    wb = openpyxl.Workbook()
    wb.save(filepath)


async def main():
    create_xlsx()
    path = "imgs"
    list_img = os.listdir(path)

    list_final = list()

    client = imgbbpy.SyncClient(key)
    for i in list_img:
        path_img = "imgs\\"+str(i)
        print(i)
        image = client.upload(file=path_img)

        list_final.append((i,image.url))


    wb = openpyxl.load_workbook(filename='imgs.xlsx')
    hoja = wb.active

    for i in list_final:
        hoja.append(i)
    wb.save('imgs.xlsx')


async def run_main():
    await main()


asyncio.run(run_main())