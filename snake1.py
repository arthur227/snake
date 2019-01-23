class damier:
    def __init__(self, tailleX, tailleY, icon):
        
        self.tailleX = tailleX
        self.tailleY = tailleY
        self.icon = icon
        self.listeDamier = []
        y = 0
        while y <= tailleY:
            x = 0
            while x <=tailleX:
                
                self.listeDamier.append([x,y,icon])
                x += 1
            y += 1


def affichage_carte( position_boule, score, deplacement):
    affichage = ""
    #Création de l'object damier
    Mondamier = damier(19,19,"x")

    
    position_boule.append("*")
    nouveau_deplacement = []

    #Les dernier déplacement en fonction du score
    deplacement = deplacement[-score:]
    #Liste des déplacements avec "o"
    for co in deplacement:
        
        nouveau_deplacement.append([co[0], co[1], "o"])
    

    #Met la boule dans le damier
    for i in Mondamier.listeDamier:
        if position_boule[0] == i[0] and position_boule[1] == i[1]:
            i[2] = position_boule[2]
            
    #Met le bout de snake        
    for i in Mondamier.listeDamier:
        for a in nouveau_deplacement:
            if i[0] == a[0] and i[1] == a[1]:
                i[2] = a[2]

    #Afficher le damier
    y = 0
    while y <= Mondamier.tailleY:
        x = 0
        while x <= Mondamier.tailleX:
            for i in Mondamier.listeDamier:
                if i[0] == x and i[1] == y:
                    affichage = affichage + i[2]
            x = x + 1
        affichage = affichage + "\n"
        y += 1
    return(affichage)
        
    
    
    
    

import time
import curses
from curses import wrapper
import random
from math import *
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(1)

def main(stdscr):
    while True:
        # Clear screen
        stdscr.clear()

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLUE)
        
       

        #Affichage du perso
        score = 1
        deplacement = [[5,8],[5,8]]
        position_perso = [5,8]
        deplacement.append(position_perso)
        
        position_boule = [random.randrange(1,20), random.randrange(1,20)]
        t = affichage_carte( position_boule, score, deplacement)

        compteur_case = 0
        for i in t:
                
            if i == "x":
                stdscr.addstr(i, curses.color_pair(2))
            elif i == "o":
                stdscr.addstr(i, curses.color_pair(3))
            elif i == "*":
                stdscr.addstr(i, curses.color_pair(1))
            
            if compteur_case == 20:
                compteur_case = 0
                stdscr.addstr("\n", curses.color_pair(2))
            compteur_case +=1    
        

        gameover = 0
        c = None
        while True:
            
            p = stdscr.getch()
            if p == -1:
                p = None
            elif c != p:
                    c = p
            
                    
           
            
            if c == curses.KEY_UP:
                
                position_perso[1] = position_perso[1] - 1
                deplacement.append([position_perso[0], position_perso[1]])
            elif c == curses.KEY_RIGHT:
                
                position_perso[0] = position_perso[0] + 1
                deplacement.append([position_perso[0], position_perso[1]])
            elif c == curses.KEY_DOWN:
                
                position_perso[1] = position_perso[1] + 1
                deplacement.append([position_perso[0], position_perso[1]])
            elif c == curses.KEY_LEFT:
                
                position_perso[0] = position_perso[0] - 1
                deplacement.append([position_perso[0], position_perso[1]])


            
            #Si deux pion sont sur la même case, il y a collision = gameover
            deplacement_actuelle = deplacement[-score:]
            
            for i in deplacement_actuelle:
                if deplacement_actuelle.count(i) > 1:
                    gameover=1
                    
            #Si on rencontre un mur
            if position_perso[0] == - 1 or position_perso[0] == 20 or position_perso[1] == - 1 or position_perso[1] == 20:
                gameover=1
                
            
            #Si personnage a la même position que la boule
            if position_perso[0] == position_boule[0] and position_perso[1] == position_boule[1] :
                position_boule = [random.randrange(1,20), random.randrange(1,20)]
                score += 1

            
            stdscr.clear()
            
                
            t = affichage_carte(position_boule, score, deplacement)
            
            compteur_case = 0
            for i in t:
                
                if i == "x":
                    stdscr.addstr(i, curses.color_pair(2))
                elif i == "o":
                    stdscr.addstr(i, curses.color_pair(3))
                elif i == "*":
                    stdscr.addstr(i, curses.color_pair(1))
                else:
                    stdscr.addstr(i, curses.color_pair(2))
                    
                
            stdscr.addstr("\nLe personnage à un position de [" + str(position_perso[0]) + ";" + str(position_perso[1]) + "]\n")
            stdscr.addstr("\nLa boule à un position de [" + str(position_boule[0]) + ";" + str(position_boule[1]) + "]")
            stdscr.addstr("  Vous avez un score de: " + str(score))
            time.sleep(0.15)
            
            if gameover == 1:
                
                break

        stdscr.clear()
        stdscr.refresh()
        
        print("GameOver.. Vous avez fait " + str(score) + ". Une partie va se relancer!")
        time.sleep(5)
        
        
    
    

wrapper(main)

