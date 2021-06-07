#Pygame klaviatuuri kasutamine
#Autor: Alar-Mikk Udu ISK20
#Kuupäev: 07.06.2021

import pygame
pygame.init()
#ekraani seaded mõlemale ringile
screenX = 800
screenY = 600
screen=pygame.display.set_mode([screenX,screenY])
x = y = 0
#graafika failide laadimine
taust = pygame.image.load("farm.jpg")
mees = pygame.image.load("mees.jpg")
sword = pygame.image.load("sword.jpg")
mesilane = pygame.image.load("bee.jpg")
bat = pygame.image.load("bat.jpg")
bat2 = pygame.image.load("bat3.jpg")
rectangle_image = pygame.image.load("sword.jpg")
screen.blit(taust, (0,0)) #tekitame tausta
rectangle = pygame.Rect(122, 328, 100,100) #swordi hitbox + asukoht
rectangle2= pygame.Rect(500, 100, 150,200) #nahkhiire hitbox + asukoht
rectangle3= pygame.Rect(200, 70 , 220, 200) # teise nahkhiire hitbox  koos asukohaga
rectangle4= pygame.Rect(250, 400 , 200, 200) # kolmanda nahkhiire hitbox + asukoht
rectangle_draging = False # muutuja mõõga liigutamiseks
#programmi akna nimetus
pygame.display.set_caption("hiire kasutamine")

#mootor   
running = True
while running:
    pygame.event.get()
    screen.blit(mees, (x,y)) # kuvame pildi ekraanile koos asukohaga
    screen.blit(rectangle_image, (rectangle))
    screen.blit(mesilane ,(rectangle2))
    screen.blit(bat, (rectangle3))
    screen.blit(bat2, (rectangle4))
    pygame.display.flip() #värskendame ekraani
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Kui sündmuseks on hiirenupu vajutus,...
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:            
                if rectangle.collidepoint(event.pos): # kui puudutame mõõka, siis liigub hiirega kaasa
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
                if rectangle2.collidepoint(event.pos): # kui liigume hiirega vastu teatud koordinaate = event
                    mouse_x, mouse_y = event.pos
                    #kaotame ära mesilase ekraanilt (uus asukoht):
                    rectangle2.y = 2000
                    rectangle2.x = 1000

                #teine nahkhiir
                if rectangle3.collidepoint(event.pos):
                    mouse_x, mouse_y = event.pos
                    rectangle3.x = 1000
                    rectangle3.y = 2000
                #kolmas nahkhiir
                if rectangle4.collidepoint(event.pos):
                    mouse_x, mouse_y = event.pos
                    rectangle4.x = 1000
                    rectangle4.y = 2000
        # kui hiirenupp on üleval, siis mõõka kaasa ei võta
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False
        #kui hiir liigub, siis mõõga asukoht muutub vastavald hiire positsioonile
        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos



        screen.blit(taust, (0,0))
pygame.display.flip()
pygame.quit()


