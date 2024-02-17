def tabla_multiplicar(n):
    with open(f'tabla{n}.txt','w') as file:
        for i in range(1,13):
            file.write(f' {n} * {i} = {n*i}' +"\n")
    
        file.close()

def leer_tabla_multiplicar(n):
    try:
        with open(f'tabla{n}.txt','r') as file:
            
            lineas = file.readlines()
            for linea in lineas:
                print(linea)
            
    except FileNotFoundError:
        print("Archivo no encontrado, pruebe otro")

def leer_tabla_parametros(n,m):
    try:
        with open(f'tabla{n}.txt','r') as file:
            lineas = file.readlines()
        
            print(lineas[m-1])
        
    except FileNotFoundError:
        print("Archivo no encontrado, pruebe otro")
    


def main():
    print("""==============  BIENVENIDO AL PROGRAMA :))))))))   =============
                
                A continuación se presentan las siguientes opciones.......
                
                        1. Guardar en un fichero la tabla de multiplicar de un número del 1 al 10
                        2. Leer el fichero de la tabla de multiplicar de un número del 1 al 10
                        3. Leer el fichero con una línea específica del fichero""")
    
    
    
    estado = True
    while(estado):
        
        opc = int(input("\nIngrese una opción ----> :  "))
        
        if opc == 1 :
            numero = int(input("----------Ingrese un número del 1 al 10---------:  "))
            tabla_multiplicar(numero)    
            print("\n")    

        elif opc == 2 :
            numero = int(input("------Ingrese un número del 1 al 10 para la lectura del fichero ------:  "))
            leer_tabla_multiplicar(numero)        
            estado = False
        
        elif opc == 3:
            n = int(input(" ---- Ingrese un número del 1 al 10 para la lectura del fichero ----- :  "))
            m = int(input(" ----- Ingrese la línea del fichero a leer ----- :  "))
        
            print("\n")
            leer_tabla_parametros(n,m)        
            estado = False

        else:
            print("Opción no válida. Ingrese otro ")    
            

if __name__ == "__main__":
    main()