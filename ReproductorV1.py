import os
from playsound import playsound

class Menu:
    #inicializar variables
    #self privado
    def __init__(self, lista, nombre, ano) -> None:
       self._lista = lista
       self._nombre = nombre
       self._ano = ano

    def get_cancion(self):       
        return print(f"{self._lista}.- {self._nombre} ({self._ano})")

    def get_reproduccion(self):
        return print(f"Reproduciendo: {self._nombre} ({self._ano})")

    # setters
    # def set_cancion(self, l, n, a):
    #     self._lista=l
    #     self._nombre=n
    #     self._ano=a    

class Limpiar():
    def limpiar():
        if os.name == "posix":
           os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

class verCanciones():
    
    def verCanciones():
        print("   ***CANCIONERO****\n")
        audio1 = Menu(1, "Cancion 1",1970)
        audio2 = Menu(2, "Cancion 2",1971)
        audio3 = Menu(3, "Cancion 3",1972)
        audio4 = Menu(4, "Cancion 4",1973)
        audio5 = Menu(5, "Cancion 5",1974)
        audio6 = Menu(6, "Cancion 6",1975)
        
        audio1.get_cancion()
        audio2.get_cancion()
        audio3.get_cancion()
        audio4.get_cancion()
        audio5.get_cancion()
        audio6.get_cancion() 

         
class Bucle:
    
    file1 = ("Python/ReproductorIndividual/audio/1audio.mp3")      
    file2 = ("Python/ReproductorIndividual/audio/2audio.wav")
    file3 = ("Python/ReproductorIndividual/audio/3audio.wav")
    file4 = ("Python/ReproductorIndividual/audio/4audio.wav")      
    file5 = ("Python/ReproductorIndividual/audio/5audio.wav")
    file6 = ("Python/ReproductorIndividual/audio/6audio.wav")
    
    audio1 = Menu(1, "Cancion 1",1970)
    audio2 = Menu(2, "Cancion 2",1971)
    audio3 = Menu(3, "Cancion 3",1972)
    audio4 = Menu(4, "Cancion 4",1973)
    audio5 = Menu(5, "Cancion 5",1974)
    audio6 = Menu(6, "Cancion 6",1975)
       
    option = 0
    
    while option>=1 & option<=6:
        try:
         Limpiar.limpiar()   
         verCanciones.verCanciones() 
         option = int(input("\nElige cancion para reproducir o presiona una letra para salir: "))
        except:
            break
            print("Error: Ingresa una cancion de la lista\n")           
            continue  
        else:
            if option == 1:
                audio1.get_reproduccion()
                playsound(file1)               
            elif option ==2:
                audio2.get_reproduccion()
                playsound(file2)
            elif option ==3:
                audio3.get_reproduccion()
                playsound(file3)
            elif option ==4:
                audio4.get_reproduccion()
                playsound(file4)
            elif option ==5:
                audio5.get_reproduccion()
                playsound(file5)
            elif option ==6:
                audio6.get_reproduccion()
                playsound(file6)
                     
Bucle()