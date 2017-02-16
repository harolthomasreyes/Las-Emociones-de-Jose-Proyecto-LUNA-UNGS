import pygame, os,  sys
from Configuracion  import *
from Funciones  import *
  
#gameIcon = pygame.image.load('carIcon.png') 
#pygame.display.set_icon(gameIcon)
#centramos la ventana al iniciar
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init() 
#pantalla = pygame.display.set_mode(Dimensiones, pygame.FULLSCREEN) 
pantalla = pygame.display.set_mode(Dimensiones) 
pygame.display.set_caption("A Jugar")
reloj = pygame.time.Clock()
 

SONG_END = pygame.USEREVENT + 1

Fuente1 = pygame.font.Font(F_AarvarkCafe, TAMANNO_TITULOS) 
Fuente2 = pygame.font.Font(F_AarvarkCafe, TAMANNO_LETRA) 
Fuente3 = pygame.font.Font(Arial, TAMANNO_LETRA) 
Background_Inicio=pygame.image.load(Fondo_Intro).convert()
Jose_Cumpleanos=pygame.image.load(Joseensucumpleanos).convert()
Background_Escena2 = pygame.image.load(Block_Escena2).convert()
Background_Escena3 = pygame.image.load(Block_Escena3).convert()
PlayMusicGameIni()

hecho = False 

# -------- Bucle de la Pagina de Inicio -----------
def game_intro():
    global hecho
    Mostrar_Inicio = True 
    while not hecho and Mostrar_Inicio:
        for evento in pygame.event.get(): #  El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
            if evento.type == pygame.MOUSEBUTTONDOWN:
                Mostrar_Inicio = False
            if evento.type ==SONG_END:
                PlayMusicGameIni()
   
         
        # Instrucciones de dibujo, pagina 1
        # Esto tambien podria cargar una imagen realizada por cualquier otro programa.
        # De esta forma seria mas facil y flexible. 
        pantalla.blit(Background_Inicio,(0,0))
        texto = Fuente1.render("Las emociones de Jose", True, Teal)
        pantalla.blit(texto, [10, 10])
      

        #button(pantalla,"A JUGAR!",350,500,180,50,Teal,Lime,game_loop) 
        imageButton(pantalla,NinosJugando,550,20,200,153,PrimeraEscena)

        
        # Limitamos a 20 fotogramas por segundo.
        reloj.tick(FPS)
 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
 
# -------- Bucle Principal del Programa -----------
iSelecciono_Jose = False
iSelecciono_FelizCumple = False
def PrimeraEscena():
    global hecho
    PlayMusicGameMaster()
    global iSelecciono_Jose  
    global iSelecciono_FelizCumple 
    PuedeContinuar = False
    while not hecho:
        for evento in pygame.event.get(): # El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
            if evento.type ==SONG_END:
                PlayMusicGameMaster()
 
     

        pantalla.blit(Jose_Cumpleanos,(0,0)) 

        if PuedeContinuar: 
            imageButton(pantalla,FlechaDerecha,ANCHO - 50,50,50,50,SegundaEscena)
            MostrarTexto(pantalla,Fuente2,"Jose",[270, 100],Blue)
            MostrarTexto(pantalla,Fuente2,"cumpleanos",[340, 100],Blue)
        else: 
            if iSelecciono_Jose: 
                MostrarTexto(pantalla,Fuente2,"Jose",[270, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"Jose",[270, 100],Teal)

            if iSelecciono_FelizCumple: 
                MostrarTexto(pantalla,Fuente2,"cumpleanos",[340, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"cumpleanos",[340, 100],Teal)
       
   
        imageButton(pantalla,Close,ANCHO - 50,0,50,50,QuitGame)

        if iSelecciono_FelizCumple & iSelecciono_Jose:
            iSelecciono_FelizCumple =False
            iSelecciono_Jose =False
            PuedeContinuar=True
            PlayCelebrar()

       
        imageButton(pantalla,Block_Jose, 270,0,130,99,PintarJose)
        imageButton(pantalla,Block_JoseCumpleanos, 420,0,130,99,PintarCumpleAnos)


        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(FPS) 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip()

def PintarJose():
    CambiarDeColorLetra(pantalla,Fuente2,"Jose",[270, 100],Blue)
    global iSelecciono_Jose  
    iSelecciono_Jose =True

def PintarCumpleAnos():
    CambiarDeColorLetra(pantalla,Fuente2,"cumpleanos",[340, 100],Blue)
    global iSelecciono_FelizCumple 
    iSelecciono_FelizCumple =True

hecho = False
iSelecciono_Jose = False
iSelecciono_Bien= False
iSelecciono_Crecer= False
iSelecciono_Fuerte= False
def SegundaEscena():
    global hecho
    PlayMusicGameMaster() 
    global iSelecciono_Bien
    global iSelecciono_Jose
    global iSelecciono_Crecer
    global iSelecciono_Fuerte
    PuedeContinuar = False
    while not hecho:
        for evento in pygame.event.get(): # El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
            if evento.type ==SONG_END:
                PlayMusicGameMaster()
  
        pantalla.blit(Background_Escena2,(0,0)) 
        
        if PuedeContinuar: 
            imageButton(pantalla,FlechaDerecha,ANCHO - 50,50,50,50,TercerEscena)
            MostrarTexto(pantalla,Fuente2,"Bien!",[50, 100],Blue) 
            MostrarTexto(pantalla,Fuente2,"Jose",[230, 100],Blue)
            MostrarTexto(pantalla,Fuente2,"va a crecer",[410, 100],Blue)
            MostrarTexto(pantalla,Fuente2,"Fuerte",[590, 100],Blue)
        else: 
            if iSelecciono_Bien: 
                MostrarTexto(pantalla,Fuente2,"Bien!",[50, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"Bien!",[50, 100],Teal)
            if iSelecciono_Jose: 
                MostrarTexto(pantalla,Fuente2,"Jose",[230, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"Jose",[230, 100],Teal)
            if iSelecciono_Crecer: 
                MostrarTexto(pantalla,Fuente2,"va a crecer",[410, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"va a crecer",[410, 100],Teal)
            if iSelecciono_Fuerte: 
                MostrarTexto(pantalla,Fuente2,"Fuerte",[590, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"Fuerte",[590, 100],Teal)


            if iSelecciono_Bien & iSelecciono_Jose & iSelecciono_Crecer & iSelecciono_Fuerte:
                iSelecciono_Jose = False
                iSelecciono_Bien= False
                iSelecciono_Crecer= False
                iSelecciono_Fuerte= False
                PuedeContinuar=True
                PlayCelebrar()


        imageButton(pantalla,Block_Bien, 50,0,130,99,PintarBien)
        imageButton(pantalla,Block_Jose, 230,0,130,99,PintarJoseEscena2) 
        imageButton(pantalla,Block_Crecer, 410,0,130,99,PintarCrecerEscena2)
        imageButton(pantalla,Block_Fuerte, 590,0,130,99,PintarFuerteEscena2)

        imageButton(pantalla,Close,ANCHO - 50,0,50,50,QuitGame)
        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(FPS) 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip() 
def PintarBien():
    CambiarDeColorLetra(pantalla,Fuente2,"Bien!",[50, 100],Blue)
    global iSelecciono_Bien  
    iSelecciono_Bien =True
def PintarJoseEscena2():
    CambiarDeColorLetra(pantalla,Fuente2,"Jose",[230, 100],Blue)
    global iSelecciono_Jose  
    iSelecciono_Jose =True
def PintarCrecerEscena2():
    CambiarDeColorLetra(pantalla,Fuente2,"va a crecer",[410, 100],Blue)
    global iSelecciono_Crecer  
    iSelecciono_Crecer =True
def PintarFuerteEscena2():
    CambiarDeColorLetra(pantalla,Fuente2,"Fuerte",[590, 100],Blue)
    global iSelecciono_Fuerte  
    iSelecciono_Fuerte =True

iSelecciono_Asustado= False
iSelecciono_Jose = False

def TercerEscena():
    global hecho
    PlayMusicGameMaster() 
    global iSelecciono_Asustado
    global iSelecciono_Jose 
    PuedeContinuar = False
    while not hecho:
        for evento in pygame.event.get(): # El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
            if evento.type ==SONG_END:
                PlayMusicGameMaster()
  
        pantalla.blit(Background_Escena3,(0,0)) 
        
        if PuedeContinuar: 
            #imageButton(pantalla,FlechaDerecha,ANCHO - 50,50,50,50,game_intro)
            MostrarTexto(pantalla,Fuente2,"Jose",[50, 100],Blue) 
            MostrarTexto(pantalla,Fuente2,"esta asustado!",[230, 100],Blue) 
        else: 
            if iSelecciono_Jose: 
                MostrarTexto(pantalla,Fuente2,"Jose",[50, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"Jose",[50, 100],Teal)
            if iSelecciono_Asustado: 
                MostrarTexto(pantalla,Fuente2,"esta asustado!",[230, 100],Blue)
            else:        
                MostrarTexto(pantalla,Fuente2,"esta asustado!",[230, 100],Teal)
 


            if iSelecciono_Asustado & iSelecciono_Jose  :
                iSelecciono_Jose = False
                iSelecciono_Bien= False 
                PuedeContinuar=True
                PlayCelebrar()


        imageButton(pantalla,Block_Jose, 50,0,130,99,PintarJoseEscena3)
        imageButton(pantalla,Block_Asustado, 230,0,130,99,PintarASustadoEscena3)  

        imageButton(pantalla,Close,ANCHO - 50,0,50,50,QuitGame)
        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(FPS) 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip() 

def PintarJoseEscena3():
    CambiarDeColorLetra(pantalla,Fuente2,"Jose",[50, 100],Blue)
    global iSelecciono_Jose  
    iSelecciono_Jose =True

def PintarASustadoEscena3():
    CambiarDeColorLetra(pantalla,Fuente2,"esta asustado!",[230, 100],Blue)
    global iSelecciono_Asustado  
    iSelecciono_Asustado =True
# Partate bien con el IDLE. Si nos olvidamos de esta linea, el programa se 'colgara'
# en la salida.
game_intro()
PrimeraEscena()
SegundaEscena()
TercerEscena()
pygame.quit()
quit()