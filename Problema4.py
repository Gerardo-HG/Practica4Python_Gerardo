import requests

def main():
    estado = True
    while(estado):
        try:
        
            cantidad_bitcoins = int(input("Digite la cantidad de bitcoins que posee:   "))
            if cantidad_bitcoins <0:
                print("---La cantidad de monedas no puede ser un valor numérico negativo----")
                print("\n")
            else:
                estado = False    
            
            url = " https://api.coindesk.com/v1/bpi/currentprice.json"
            response = requests.get(url)
        
            data = response.json()
            costo_bitcoins = float(data['bpi']['USD']['rate'].replace(",",""))
        
        except ValueError as va:
            print("----Error. Ingrese una cantidad numérica de monedas----")
            print("\n")
            estado = True
            
        except requests.RequestException as er:
            print("Error al obtener el precio de Bitcoin...",er)
            costo_bitcoins = None

    if costo_bitcoins is not None:
        monto_total = costo_bitcoins * cantidad_bitcoins
        print("\n")
        texto = f"El costo total de {cantidad_bitcoins} bitcoins es de ${monto_total:,.4f} USD."
        print(texto)
        
    with open('./precios_bitcoin.txt','a') as f:
        f.write(texto +"\n")
        f.seek(0)

        
main()