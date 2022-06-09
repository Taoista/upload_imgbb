from imgbb.client import Client
import os
import aiohttp
import asyncio
import imgbbpy
import time
import openpyxl

key = os.environ.get("KEY")


async def main():
    path = "imgs"
    dir_list = os.listdir(path)


    list_final = list()


    client = imgbbpy.SyncClient(key)
    for i in dir_list:
        path_img = "imgs\\"+str(i)
        print(i)
        image = client.upload(file=path_img)

        list_final.append((i,image.url))


    wb = openpyxl.load_workbook(filename='productos.xlsx')
    hoja = wb.active

    for i in list_final:
        hoja.append(i)
    wb.save('productos.xlsx')


async def run_main():
    await main()


asyncio.run(run_main())