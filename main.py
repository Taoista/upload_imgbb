import asyncio
import imgbbpy
import os


async def main():
    client = imgbbpy.AsyncClient(os.environ.get('API_KEY'))

    CURRENT_PATH = os.getcwd()+'\\files\\'
    
    all_files = os.listdir(CURRENT_PATH)

    f = open("lista_upload.txt", "w")

    for file in all_files:
        file_name = os.path.basename(file)
        name = os.path.splitext(file_name)[0]
        image = await client.upload(file=CURRENT_PATH+file_name)
        f.write('\n' + f"{name}, {image.url}")
        print(image.url)

    f.close()



if __name__ == '__main__':
    asyncio.run(main())
