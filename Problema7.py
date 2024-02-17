import sqlite3
import requests


conn = sqlite3.connect('base.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                    fecha TEXT PRIMARY KEY,
                    precio_compra REAL,
                    precio_venta REAL
                )''')

# URLs de la API de SUNAT para cada mes del año 2023
urls = [
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=1&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=2&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=3&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=4&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=6&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=7&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=8&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=9&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=10&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=11&year=2023',
    'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=12&year=2023'
]


for url in urls:
    try:
        
        response = requests.get(url)
        
        
        data = response.json()
        
        listado=list(data)
        
        for lista in listado:
            fecha = lista['fecha']
            precio_compra = lista['compra']
            precio_venta = lista['venta']
            
        
            cursor.execute('''INSERT INTO sunat_info (fecha,precio_compra, precio_venta)
                            VALUES (? ,?, ?)''', (fecha,precio_compra, precio_venta))
    except requests.RequestException as err:
        print(f'Hubo un error al obtener datos de la API: {err}')
    except KeyError:
        print('Error: Los datos de la API no tienen el formato esperado')
        
        
conn.commit()


cursor.execute('''SELECT * FROM sunat_info''')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
