# Importing the library
import keyboard
import pygame
import asyncio


# Initializing Pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 14)

# Initializing surface
surface = pygame.display.set_mode((1400, 600))

# Initializing RGB Color
color = (100, 100, 100)

# Creating a text typing function
def texting(text,  x, y):
    img = font.render(text, True, color)
    surface.blit(img, (x, y))

#fonction qui va créer des rectangles pour dessiner le piano
def recting(x, y):

    #2 octaves dont 2 itérations
    whites = []
    blacks = []
    for i3 in range(2):
        #7 itérations pour créer les 7 touches blanches
        for i in range(7):
            i5 = pygame.draw.rect(surface, (120, 120, 120), (x, y, 50, 150), width = 2, border_radius=5 )
            whites.append(i5)
            #zarma pour que pygame update le GUI avec les rectangles
            pygame.display.flip()
            pygame.display.update()
            # x coordinates auquel on rajoute +50 pour que chaque nouveau rectangle se décale vers la droite et se superpose pas
            x += 50

            #black notes, same shit
            if i == 2 or i == 6:
                pass
            else:
                i2 = pygame.draw.rect(surface, (0, 0, 0), (x-17,y, 30, 100), width = 0, border_radius=5)
                blacks.append(i2)
    i = 0
    i2 = 0
    return whites, blacks;


# Changing surface color
surface.fill("white")




clock = pygame.time.Clock()
position = pygame.mouse.get_pos()
run = True


while run :
    clock.tick(10)
    #retrieve les values des rectangles
    [white, black] = recting(310, 300)
    #soundlist
    notes_white = ["do1.wav", "re1.wav", "mi1.wav", "fa1.wav", "sol1.wav", "la1.wav", "si1.wav", "do2.wav", "re2.wav", "mi2.wav", "fa2.wav", "sol2.wav", "la2.wav", "si2.wav"]
    notes_black = ["dos1.wav", "res1.wav", "fas1.wav", "sols1.wav", "las1.wav", "dos2.wav", "res2.wav", "fas2.wav", "sols2.wav", "las2.wav"]
    hotkeys_white = ["w", "x", "c", "v", "b", "n", ",", "y", "u","i","o","p","^","$"]
    hotkeys_black = ["s","d","g","h","j","7","8","0","°","_"]

    for i in range(len(hotkeys_white)):
        #putting the notes on the keys
        texting(notes_white[i][0]+notes_white[i][1], white[i][0]+15, white[i][1]+120)
        #showing the hotkeys
        texting(hotkeys_white[i], white[i][0]+20, white[i][1]+155)


    #play a note if x is pressed

    #white notes
    for i in range(len(hotkeys_white)):
        if keyboard.is_pressed(hotkeys_white[i]):
            pygame.mixer.music.load(notes_white[i])
            pygame.mixer.music.play(1)
    #black notes
    for i in range(len(hotkeys_black)):
        if keyboard.is_pressed(hotkeys_black[i]):
            pygame.mixer.music.load(notes_black[i])
            pygame.mixer.music.play(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # check if we click on a note and play it
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            #white
            for items in range(len(white)):
                if white[items].collidepoint(mouse_pos) and not black[items-4].collidepoint(mouse_pos):
                    pygame.mixer.music.load(notes_white[items])
                    pygame.mixer.music.play(1)
            #black
            for items in range(len(black)):
                if black[items].collidepoint(mouse_pos):
                    pygame.mixer.music.load(notes_black[items])
                    pygame.mixer.music.play(1)
