import  pygame
from Configuracion  import *

 

def QuitGame():
    pygame.quit()
    quit()

def ReproducirAudio(Audio):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(Audio)
    pygame.mixer.music.play()

def PlayCelebrar():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(SONIDO_CELEBRAR)
    pygame.mixer.music.play()

def PlayMusicGameMaster():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(SONIDO_Continuo)
    pygame.mixer.music.play()
def PlayMusicGameIni():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(SONIDO_Inicio)
    pygame.mixer.music.play()

def text_objects(text, font):
    textSurface = font.render(text, True, NEGRO)
    return textSurface, textSurface.get_rect()

def button(gameDisplay,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(F_AarvarkCafe, TAMANNO_TITULOS)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def imageButton(gameDisplay,Imagen,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:  
        if click[0] == 1 and action != None:
            action()          
    imgImagen=pygame.image.load(Imagen).convert_alpha()
    gameDisplay.blit(imgImagen, [x,y])

def CambiarDeColorLetra(gameDisplay,Fuente,palabras,Coordenadas,color):
    texto = Fuente.render(palabras, True, color) 
    gameDisplay.blit(texto, Coordenadas)

def MostrarTexto(gameDisplay,Fuente,palabras,Coordenadas,color):
    texto1 = Fuente.render(palabras, True, color)
    gameDisplay.blit(texto1, Coordenadas)