import requests
import sqlite3

def crear_tabla():
    conexion = sqlite3.connect('basedb.db')
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS bitcoin(
                    fecha TEXT PRIMARY KEY,
                    precio_usd REAL,
                    precio_gbp REAL,
                    precio_eur REAL,
                    precio_pen REAL
                        );

                """)

    conexion.commit()
    conexion.close()
    
def insertar_datos(fecha,precio_usd,precio_gbp,precio_eur,precio_pen):
    conexion = sqlite3.connect('basedb.db')
    cursor = conexion.cursor()
    
    cursor.execute("""INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                    VALUES (?, ?, ?, ?, ?)""",(fecha,precio_usd,precio_gbp,precio_eur,precio_pen))
    conexion.commit()
    conexion.close()
    
    
def obtener_precios():
    conexion=sqlite3.connect("basedb.db")
    cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM bitcoin""")
    bitcoin_info = cursor.fetchall()
    conexion.close()
    return bitcoin_info

def costo_total(cantidad_bitcoins, precio_pen, precio_eur):
    total_pen = cantidad_bitcoins * precio_pen
    total_eur = cantidad_bitcoins * precio_eur
    
    print(f'Costo total en euros {total_eur}, Costo total en pesos {total_pen}')
    
    
def consulta_bitcoin():
    
    crear_tabla()
    estado = True
    while(estado):
        try:
        
            cantidad_bitcoins = int(input("Digite la cantidad de bitcoins que posee:   "))
            if cantidad_bitcoins < 0:
                print("---La cantidad de monedas no puede ser un valor numérico negativo----")
                print("\n")
            else:
                estado = False    
            
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            response = requests.get(url)
        
            data = response.json()
            precio_usd = float(data['bpi']['USD']['rate'].replace(",", ""))
            precio_gbp = float(data['bpi']['GBP']['rate'].replace(",", ""))
            precio_eur = float(data['bpi']['EUR']['rate'].replace(",", ""))
            
            response_sunat = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat')
            sunat_data = response_sunat.json()
            precio_pen = sunat_data['compra']
            
            fecha_actual = sunat_data['fecha']
            
            insertar_datos(fecha_actual, precio_usd, precio_gbp, precio_eur, precio_pen)
            
        except ValueError as va:
            print("----Error. Ingrese una cantidad numérica de monedas----")
            print("\n")
            estado = True
            
        except requests.RequestException as er:
            print("Error al obtener el precio de Bitcoin...", er)
            estado = True

    bitcoin_info = obtener_precios()
    if bitcoin_info:
        costo_total(cantidad_bitcoins, bitcoin_info[0][4], bitcoin_info[0][3])

if __name__ == "__main__":
    consulta_bitcoin()






