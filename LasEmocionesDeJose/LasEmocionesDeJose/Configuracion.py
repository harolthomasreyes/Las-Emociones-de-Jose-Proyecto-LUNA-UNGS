from collections import namedtuple
import random, pygame
  


FPS = 60

ANCHO = 800
ALTO = 600
   
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255) 
Red= 	(255,0,0)
Lime	= 	(0,255,0)
Blue= 	(0,0,255)
Yellow	= 	(255,255,0)
Aqua	= 	(0,255,255)
Fuchsia	= 	(255,0,255)
Silver	= 	(192,192,192)
Gray	= 	(128,128,128)
Maroon	= 	(128,0,0)
Olive	= 	(128,128,0)
Green	= 	(0,128,0)
Purple	= 	(128,0,128)
Teal= 	(0,128,128)
Navy	= 	(0,0,128)

TAMANNO_TITULOS = 56
TAMANNO_LETRA = 36


Audio_Jose = 'Sonidos/Escenas/Jose.wav'
Audio_Cumpleanos = 'Sonidos/Escenas/Cumpleanos.mp3'
SONIDO_CELEBRAR = 'Sonidos/Escenas/Celebrar.wav'

F_AarvarkCafe = 'Fuentes/Aarvark Cafe.ttf'
Arial = 'Fuentes/arial.ttf'

SONIDO_Inicio = 'Sonidos/Background.mp3'
SONIDO_Continuo = 'Sonidos/Background_Inicio.mp3'


Dimensiones = [ANCHO,ALTO]
Fondo_Intro='Imagenes/BackGround_Intro.png'
Fondo_Intro='Imagenes/BackGround_Intro.png'
FlechaDerecha='Imagenes/FlechaDerecha.png'
Close='Imagenes/Close.png'
NinosJugando = 'Imagenes/NinosJugando.png'
Joseensucumpleanos = 'Imagenes/Joseensucumpleanos.jpg'
Block_Jose = 'Imagenes/Block_Jose.png'
Block_Bien = 'Imagenes/Bien.png'
Block_Calle = 'Imagenes/Calle.png'
Block_Crecer = 'Imagenes/Crecer.png'  
Block_Asustado = 'Imagenes/Jose_Asustado.png'  
Block_Fuerte = 'Imagenes/Fuerte.png'
Block_JoseCumpleanos= 'Imagenes/Block_JoseCumpleanos.png'
Block_Escena2= 'Imagenes/Escena2.png'
Block_Escena3= 'Imagenes/Background_Escena3.png'