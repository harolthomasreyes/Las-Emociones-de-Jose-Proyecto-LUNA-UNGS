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
Background_Inicio=pygame.image.load(Fondo_Intro).convert()
Jose_Cumpleanos=pygame.image.load(Joseensucumpleanos).convert()
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
        imageButton(pantalla,NinosJugando,550,20,200,153,game_loop)

        
        # Limitamos a 20 fotogramas por segundo.
        reloj.tick(FPS)
 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
 
# -------- Bucle Principal del Programa -----------
def game_loop():
    global hecho
    PlayMusicGameMaster()

    while not hecho:
        for evento in pygame.event.get(): # El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
            if evento.type ==SONG_END:
                PlayMusicGameMaster()
 
        pantalla.blit(Jose_Cumpleanos,(0,0)) 
        texto = Fuente2.render("Jose cumpleanos", True, Teal)
        pantalla.blit(texto, [270, 100])
  

        imageButton(pantalla,Close,ANCHO - 50,0,50,50,QuitGame)
        imageButton(pantalla,Block_Jose, 270,0,130,99)
        imageButton(pantalla,Block_JoseCumpleanos, 420,0,130,99)


        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(FPS) 
        # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
     
# Partate bien con el IDLE. Si nos olvidamos de esta linea, el programa se 'colgara'
# en la salida.
game_intro()
game_loop()
pygame.quit()
quit()