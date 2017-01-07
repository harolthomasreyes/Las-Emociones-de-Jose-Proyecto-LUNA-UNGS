"""
 Ejemplo de cómo crear una ventana de instrucciones.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
 
pygame.init()
  
#  Establecemos el largo y ancho de la pantalla.
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones)
 
pygame.display.set_caption("Pantalla de Instrucciones")
 
#Iteramos hasta que el usuario haga click sobre le botón de salida.
hecho = False
 
#  Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# Posición de partida del rectángulo
rect_x = 50
rect_y = 50
 
# Velocidad y dirección del rectángulo
rect_cambio_x = 5
rect_cambio_y = 5
 
# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
mostrar_instrucciones = True
pagina_de_instrucciones = 1
 
# -------- Bucle de la Página de Instrucciones -----------
while not hecho and mostrar_instrucciones:
    for evento in pygame.event.get(): #  El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pagina_de_instrucciones += 1
            if pagina_de_instrucciones == 3:
                mostrar_instrucciones = False
 
    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(NEGRO)
 
    if pagina_de_instrucciones == 1:
        # Instrucciones de dibujo, página 1
        # Esto también podría cargar una imagen realizada por cualquier otro programa.
        # De esta forma sería más fácil y flexible.
         
        texto = fuente.render("Instrucciones", True, BLANCO)
        pantalla.blit(texto, [10, 10])
         
        texto = fuente.render("Página 1", True, BLANCO)
        pantalla.blit(texto, [10, 40])
         
    if pagina_de_instrucciones == 2:
        # Instrucciones de dibujo, página 2
        texto = fuente.render("Este programa hace rebotar un rectángulo", True, BLANCO)
        pantalla.blit(texto, [10, 10])
         
        texto = fuente.render("Página 2", True, BLANCO)
        pantalla.blit(texto, [10, 40])
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
 
    # Dibuja el rectángulo
    pygame.draw.rect(pantalla,BLANCO,[rect_x, rect_y, 50, 50])
  
    # Mueve el punto de partida del rectángulo      
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y
 
    # Rebota el rectángulo, si hace falta.
    if rect_y > 450 or rect_y < 0:
        rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x * -1
     
    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(60)
 
    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
     
# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit()