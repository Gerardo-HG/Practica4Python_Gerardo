
def conteo__lineas_codigo(ruta):
    try:
        with open(ruta,'r') as f:
            lineas = f.readlines()
            
        code_lane = 0

        for linea in lineas:
            linea = linea.strip()
            
            if linea != "" and not linea.startswith("#"):
                code_lane+=1
        
        return code_lane
    
    except FileNotFoundError:
        print("Archivo no encontrado")
        

def main():
    
    while(True):
        ruta_archivo = input("Ingrese la ruta o el nombre de un archivo.py ----> ")

        if ruta_archivo.endswith(".py"):
            break
        else:
            print("\nEl archivo ingresado no es un archivo .py válido...")
        
    lineas_de_codigo = conteo__lineas_codigo(ruta_archivo)
    
    print("\n")
    print(f'El archivo {ruta_archivo} presenta {lineas_de_codigo} lineas de codigo ')

if __name__ == "__main__":
    main()