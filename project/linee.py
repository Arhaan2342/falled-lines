from player import *
class Line:
    player = Player(0,0,0)
    xPos = 0
    yPos = 0
    llength = 0
    speed = 0
    def __init__(self,x,y,l,s, p):
        self.xPos = x
        self.yPos = y
        self.llength = l
        self.speed = s
        self.player = p
    
            
    def checkCollision():
        delatx = self.xPos - self.player.xPos
        if abs(deltax) <= (self.player.psize / 2):
            deltaY1 = self.yPos - self.player.yPos
            deltaY2 = (self.yPos + self.llength ) - self.player.yPos
            if abs(deltaY1) <= (self.player.psize / 2):
                return True;
            elif abs(deltaY2) <= (self.player.psize / 2):
                return True;
            elif self.yPos < self.player.yPos and self.player.yPos < self.yPos + self.llength:
                return True;
            else:
                return False;
        else:
            return False;
    
    def update(self):
        self.yPos+=self.speed
        
        if(checkCollision()):
            self.player.hit = True
        if self.yPos > height:
            self.yPos = 0
            self.xPos = random(0,width)
    def draw(self):
        fill(15*self.speed,15*self.speed,15*self.speed )
        line(self.xPos, self.yPos, self.xPos, self.yPos + self.llength)

        
    
