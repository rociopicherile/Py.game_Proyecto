import pygame, sys
import random
pygame.init()
pygame.display.set_caption("Astronauta vs Ovnis")

reloj = pygame.time.Clock()
BLACK=(0,0,0)
size = (600,600)
screen = pygame.display.set_mode(size)
fondo_menu = pygame.image.load("assets/fondo_menu.jpg")
escenario = pygame.image.load("assets/5e304ba8-4300-4511-bc2c-96b6d407a980.jpg")
fondo_help = pygame.image.load("assets/menu_ayuda.png")

#OBJETOS----------------------------------------------------------
class Disparos(pygame.sprite.Sprite):
        def __init__(self,x,y):
            super().__init__()
            self.image = pygame.image.load("assets/orange_fireball.png")
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.y = y
            self.rect.centerx = x
        def update(self): 
            self.rect.y -= 9 #PARA QUE LAS BALAS VAYAN HACIA ARRIBA
            
class Astronauta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/astronauta.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width()/2 
        self.rect.y = 450
    def update(self): 
        self.speed_x = 0
        keystate = pygame.key.get_pressed() #PARA VER QUÉ TECLA ESTÁ SIENDO PRESIONADA Y REALIZAR EL MOVIMIMIENTO DERECHA-IZQUIERDA
        if keystate[pygame.K_RIGHT]:
            self.speed_x += 5
        elif keystate[pygame.K_LEFT]:
            self.speed_x -= 5
        self.rect.x += self.speed_x
        if self.rect.right > 600: #PARA QUE EL PERSONAJE NO SE EXCEDA DEL MAPA
            self.rect.right = 600
        elif self.rect.left < 0:
            self.rect.left = 0
    def disparos(self): #LOS DISPAROS DEBEN SALIR DEL PERSONAJE
        disparo = Disparos(self.rect.centerx,self.rect.y)
        group_sprites.add(disparo)
        group_disparos.add(disparo)


class Ovnis(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("assets/ovni.png").convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.y = random.randrange(10,300) 
            self.rect.x = random.randrange(1,600) 
        def update(self):
            self.speed_x = 2
            self.rect.x += self.speed_x #EL OVNI DEBE MOVERSE DE FORMA HORIZONTAL
            if self.rect.right > 600: #SI SUPERA EL LÍMITE, VUELVE A APARECER EN POSX = 0
                self.rect.right = 0

class Boton():
        def __init__(self, image, pos):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        def update(self,screen):
            screen.blit(self.image, (self.x_pos,self.y_pos))
        def checkForInput(self,posc): #PARA LEER EL CLICK SOBRE EL RECTANGULO DEL OBJETO
            if posc[0] in range (self.rect.left, self.rect.right) and posc[1] in range (self.rect.top, self.rect.bottom):
                return True
            return False
#OBJETOS----------------------------------------------------------
        


#INSTANCIANDO AL JUGADOR Y CREANDO LOS GRUPOS DE OBJETOS
astronautita = Astronauta()
group_sprites = pygame.sprite.Group()
group_ovnis = pygame.sprite.Group()
group_sprites.add(astronautita)
group_disparos = pygame.sprite.Group()
group_botones = pygame.sprite.Group()
for i in range(4): #PARA CREAR LOS CUATRO OVNIS VOLADORES
    ovni = Ovnis()
    group_sprites.add(ovni)
    group_ovnis.add(ovni)

#FUNCIONES----------------------------------------------------------
def help(): #FUNCIÓN MENÚ HELP
    while True:
        screen.blit(fondo_help,(-13,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
        pygame.display.flip()
def menu(): #FUNCIÓN MENÚ PRINCIPAL
    while True:
        mouse = pygame.mouse.get_pos()
        screen.blit(fondo_menu,(0,0))
        boton_jugar = Boton(image=pygame.image.load("assets/play button.png"), pos=(200, 100)) 
        boton_help = Boton(image=pygame.image.load("assets/Help button.png"), pos=(200, 200))
        boton_quit = Boton(image=pygame.image.load("assets/Quit button 2.png"), pos=(200, 300))
        for button in [boton_jugar, boton_help, boton_quit]:
            button.update(screen)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #SI SE CLIKEA:
                if boton_jugar.checkForInput(mouse): #...DENTRO DEL BOTÓN "PLAY"
                    juego()                          #ENTONCES INICIAR JUEGO
                elif boton_quit.checkForInput(mouse):#...DENTRO DEL BOTÓN "EXIT"
                    sys.exit()                       #ENTONCES SALIR DEL PROGRAMA
                elif boton_help.checkForInput(mouse):#...DENTRO DEL BOTÓN "HELP"
                    help()                           #ENTONCES ABRIR VENTANA DE AYUDA
        
        pygame.display.flip()

def juego(): #FUNCIÓN JUEGO
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t: #SI SE PULSA LA TECLA t, GENERAR DISPAROS
                    astronautita.disparos()
                elif event.key == pygame.K_ESCAPE: #SI SE PULSA LA TECLA esc, ENTRAR AL MENU
                    menu()
        group_sprites.update()
        hits = pygame.sprite.groupcollide(group_disparos, group_ovnis, True, True) #ESTO SIRVE PARA LAS COLISIONES DISPARO-OVNI
        for hit in hits: #COMO AL DISPARAR LOS OVNIS DESAPARECEN, HAY QUE VOLVER A INSTANCIAR MÁS OVNIS
            ovni = Ovnis()
            group_sprites.add(ovni)
            group_ovnis.add(ovni)

        screen.blit(escenario,(0,0))
        group_sprites.draw(screen)
        pygame.display.flip()

        reloj.tick(60)
#FUNCIONES----------------------------------------------------------

menu()