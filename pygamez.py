#Pygame klaviatuuri kasutamine
#Autor: Alar-Mikk Udu ISK20
#Kuupäev: 06.06.2021


import pygame
pygame.init()
music = pygame.mixer.music.load('muusika.wav')
pygame.mixer.music.play(loops=-1)
#värvid mida kasutatakse
sinine = [0, 0, 255]
lBlue = [153, 204, 255]
punane = [255, 0, 0]

#ekraani seaded mõlemale ringile
screenX = 800
screenY = 680

screenX2 = 800
screenY2 = 680

#millist ekraani suurust kasutada
screen=pygame.display.set_mode([screenX,screenY])

#mis on programmi akna nimetus
pygame.display.set_caption("Minu mäng")

#Taustavärv ekraanil
screen.fill(lBlue)

clock = pygame.time.Clock()

#koordinaadid ja kiirus
#esimene ring
posX, posY = screenX/2, screenY/2
speedX, speedY = 0, 0
directionX = 0
directionY = 0
#teine ring
posX2 = 360 # paikneb esimese ringi kõrval
posY2 = 340
speedX2 = 0
speedY2 = 0
directionX2 = 0
directionY2 = 0

gameover = False
while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        #klahvivajutuse programm esimesel ringil
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directionX = "move_right"
            elif event.key == pygame.K_LEFT:
                directionX = "move_left"
            elif event.key == pygame.K_UP:
                directionY = "move_up"
            elif event.key == pygame.K_DOWN:
                directionY = "move_down"
            elif event.key == pygame.K_PAGEDOWN:
                directionY = "move_up2"
            elif event.key == pygame.K_PAGEUP:
                directionY = "move_down2"
            elif event.key == pygame.K_HOME:
                posY = 340
                posX = 400
                posY2 = 340
                posX2 = 400
            #klavhivajutuse programm teisel ringil
            elif event.key == pygame.K_w:
                directionY2 = "üles"
            elif event.key == pygame.K_s:
                directionY2 = "alla"
            elif event.key == pygame.K_a:
                directionX2 = "vasakule"
            elif event.key == pygame.K_d:
                directionX2 = "paremale"
            
        #klahvivajutuse vabastamine esimesel ringil
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0
        #page-up/down klahvivajutuste vabastamine
            if event.key == pygame.K_PAGEUP or event.key == pygame.K_PAGEDOWN:
                directionY = 0
        #teise ringi klahvivajutuste vabastamine
            if event.key == pygame.K_w or event.key == pygame.K_s:
                directionY2 = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                directionX2 = 0

    #mängu piirjoonte tuvastamine ja liikumine
    if directionX == "move_left":
        if posX > 5:
            posX -= 3
    elif directionX == "move_right":
        if posX + 30 < screenX:
            posX += 3
    if directionY == "move_up":
        if posY > 30:
            posY -= 3
    elif directionY == "move_down":
        if posY + 30 < screenY:
            posY += 3
    if directionY == "move_up2":
         if posY > 30 < screenY:
            posY += 6
    if directionY == "move_down2":
         if posY + 30 < screenY:
            posY -= 6
    #Teise ringi liikumine ja piirjooned
    if directionY2 == "üles":
        if posY2 > 30:
            posY2 -= 3
    elif directionY2 == "alla":
        if posX2 + 30 < screenY2:
            posY2 += 3
    if directionX2 == "vasakule":
        if posY2 > 30:
            posX2 -= 3
    elif directionX2 == "paremale":
        if posX2 + 30 < screenX2:
            posX2 += 3

  #1 ringi ja 2 ringi väljanägemine (värv ja raadius)  
    ring = pygame.draw.circle(screen, sinine, [posX, posY], 20, 100)
    ring2 = pygame.draw.circle(screen, punane, [posX2, posY2], 20, 100)  
    pygame.display.flip()
    screen.fill(lBlue)


pygame.quit()


