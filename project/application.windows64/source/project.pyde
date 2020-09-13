from player import *
from linee import*
player = Player(50,50,50)
lasers = []
gamestate = 0
def setup():
    global gamestate
    for i in range (50):
        lasers.append (Line(random(0,width), random(-100,-10), random (19,39), random (1,10),player))
    size(1000,500)
    gamestate = 0
def draw():
    global gamestate
    background(255)
    if gamestate == 0:
        textSize(50)
        fill(0)
        textAlign(CENTER, CENTER)
        text( "Click to start!", width/2, height/2)
    elif gamestate == 1:
        player.update()
        player.draw()
        for i in range(50):
            lasers [i].update()
            lasers[i].draw()
        if player.hit: 
            gamestate = 2
    elif gamestate == 2:
        textSize(50)
        fill(150, 10, 10)
        textAlign(CENTER, CENTER)
        text("You are trash!", width/2, height/2)
        
def mouseClicked():
    global gamestate
    if gamestate == 0:
        gamestate = 1
        
    elif gamestate == 2:
        gamestate = 0
    

        

    
