import os
from tkinter import messagebox
from playsound import playsound

class Menu:
    #inicializar variables
    #self privado
    
    def __init__(self, lista, nombre, ano):
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

class Monedas:
    
    #def __init__(self,saldo) -> None:  
    def __init__(self,saldo):    
        self._saldo = saldo

    def setMonedas(self, coin):
        if (coin>0):
            self._saldo = self._saldo + coin       
            return self._saldo
    
    def setGastar(self, gasto):
        self._saldo = self._saldo - gasto
    
    def getSaldo(self):
        return self._saldo

class CrearMenu:

    def crearMenu():
    
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
        
        verCanciones.verCanciones()

        option = 0
        
        while option>=1 & option<=6:
            try: 
             option = int(input("\nElige cancion para reproducir o presiona una letra para salir: "))
            except:
                break
                print("Error: Ingresa una cancion de la lista\n")           
                continue  
            else:
                if option == 1:
                    audio1.get_reproduccion()
                    playsound(file1)
                    break               
                elif option ==2:
                    audio2.get_reproduccion()
                    playsound(file2)
                    break
                elif option ==3:
                    audio3.get_reproduccion()
                    playsound(file3)
                    break
                elif option ==4:
                    audio4.get_reproduccion()
                    playsound(file4)
                    break
                elif option ==5:
                    audio5.get_reproduccion()
                    playsound(file5)
                    break
                elif option ==6:
                    audio6.get_reproduccion()
                    playsound(file6)
                    break
                
class Loop:
    def loop():
        x = messagebox.askquestion("Saldo No Disponible","Desea Ingresar mas Monedas?")

        if (x=="yes"):
            Inicio.inicio()
        else:
            print("**ESKERRIK ASKO***\n")
            print("   ** AGUR **\n")
                                 
class Inicio:
    
    def inicio():
    
        gasto = 1
        
        Limpiar.limpiar()
        print("****REPRODUCTOR DE MUSICA****\n")
        print("Valor de cada cancion: 1 euro\n")
        coin = int(input("Ingresa moneda: "))

        saldo = Monedas(coin)
        
        while (saldo.getSaldo()<=0):
            print("Ingrese monedas de 1 euro\n")
            coin = int(input("Ingresa moneda: "))
            Monedas.setMonedas(saldo, coin)
        
        while (saldo.getSaldo()>0):
            Monedas.setGastar(saldo, gasto)
            Limpiar.limpiar()
            print(f"Saldo actual: {saldo.getSaldo()} Euro \n")
            CrearMenu.crearMenu()
            Limpiar.limpiar() 
            
            if (saldo.getSaldo()==0):
                print("No dispone de saldo\n")
                Loop.loop()
                #break              


class Reproductor:
    Limpiar.limpiar()
    Inicio.inicio()

    
Reproductor()
   
    
                 
