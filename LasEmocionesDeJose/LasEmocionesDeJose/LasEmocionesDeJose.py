import pygame, os,  sys
from Configuracion  import *
from Funciones  import *
 
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init() 
#pantalla = pygame.display.set_mode(Dimensiones, pygame.FULLSCREEN) 
pantalla = pygame.display.set_mode(Dimensiones) 
pygame.display.set_caption("A Jugar")
reloj = pygame.time.Clock()

hecho = False 
Mostrar_Inicio = True
Pagina_de_Inicio = 1
 
Fuente1 = pygame.font.Font(F_AarvarkCafe, TAMANNO_TITULOS) 
Background_Inicio=pygame.image.load(Fondo_Intro).convert()

# -------- Bucle de la Pagina de Inicio -----------
while not hecho and Mostrar_Inicio:
    for evento in pygame.event.get(): #  El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
        if evento.type == pygame.MOUSEBUTTONDOWN:
            Pagina_de_Inicio += 1
            if Pagina_de_Inicio == 2:
                Mostrar_Inicio = False
 
    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(NEGRO)
 
    if Pagina_de_Inicio == 1:
        # Instrucciones de dibujo, pagina 1
        # Esto tambien podria cargar una imagen realizada por cualquier otro programa.
        # De esta forma seria m�s facil y flexible.
          
        pantalla.blit(Background_Inicio,(0,0))
        texto = Fuente1.render("Las emociones de Jose", True, Teal)
        pantalla.blit(texto, [10, 10])
         
        
    # Limitamos a 20 fotogramas por segundo.
    reloj.tick(20)
 
    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
# -------- Bucle Principal del Programa -----------
while not hecho:
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
 
    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(NEGRO)
  
     
    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(60) 
    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
     
# Partate bien con el IDLE. Si nos olvidamos de esta linea, el programa se 'colgara'
# en la salida.
pygame.quit()