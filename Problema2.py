from pyfiglet import Figlet
import random

figlet = Figlet()

def opcion_1():
    print("\n")
    
    print(figlet.getFonts())
    print("\n")
    
    estado = True
    
    while(estado):
        try:
            f_texto = input("Ingrese un estilo de fuente --->  ")
            
            if f_texto in figlet.getFonts():
                estado = False
            else:
                print("\nNo se encuentra este estilo de fuente. Ingrese otro de la lista")
                
        except KeyboardInterrupt:
            print("\nSe ha interrumpido la entrada")    
            return
        
    texto = input("Ingrese un texto cualquiera ---> ")
            
    figlet.setFont(font=f_texto)
    print(figlet.renderText(texto))

def opcion_2():
    f_texto_random = random.choice(figlet.getFonts())
    texto = input("Ingrese un texto cualquiera --->  ")
    print("\n")
    figlet.setFont(font=f_texto_random)
    print(figlet.renderText(texto))
    

def main():
    while(True):
        print("""---------MENÚ ITERATIVO------------
                        1. -> Ingresar una fuente de texto <-
                        2. -> Elegir aleatoriamente una fuente de texto <-
                        3. -> Salir del Programa""")
        print("\n")            
        opc = int(input(" Ingrese una opción -> : "))
        
        
        if opc == 1:
            opcion_1()
        elif opc == 2:
            opcion_2()
        elif opc == 3:
            print("\nAdiós y vuelva pronto.")
            break
    
main()
#print(figlet.getFonts())