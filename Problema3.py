import os
import zipfile
import requests


url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

#Obtener la imagen descargada en la web
with open('imagen_perro.jpg', 'wb') as f:
    #f.write(response.content)
    pass

#Zipeando los archivos de tipo jpg
with zipfile.ZipFile('archivo_imagen.zip','w') as zip:
    for file in os.listdir('.'):
        file_path = os.path.join(os.getcwd(),file)
        
        if file.endswith('.jpg'):
            zip.write(file_path
                    , os.path.basename(file_path))
            
#Extrayendo los archivos de tipo jpg 
with zipfile.ZipFile('./archivo_imagen.zip','w') as zip_ref:
    zip_ref.extractall(path='./unzip')

