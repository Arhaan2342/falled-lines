class Player:
    xPos = 0
    yPos = 0
    psize = 10
    playercolor = (0,220,0)
    hit = False
    def __init__(self,x,y,s):
        xPos = x 
        yPos = y
        psize = s
        playercolor = (0,220,0)
    def update(self):
        self.xPos = mouseX
        self.yPos = mouseY
        self.psize+=.01
    def draw (self):
         if self.hit:
             fill (255, 0, 0)
         else:
             fill(0,220,0)
         strokeWeight(1) 
         circle(self.xPos,self.yPos,self.psize)
