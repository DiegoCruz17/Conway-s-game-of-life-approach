import pygame,math
def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b
def lerpColor(obj,baseColor,targetColor1,targetColor2,pace):
        if obj.condition:
            baseColor[0] =lerp(baseColor[0],targetColor1[0],pace)
            baseColor[1] =lerp(baseColor[1],targetColor1[1],pace)
            baseColor[2] =lerp(baseColor[2],targetColor1[2],pace)
            if math.fabs(targetColor1[0] - baseColor[0])<1:
                obj.condition = False
        else:
            baseColor[0] =lerp(baseColor[0],targetColor2[0],pace)
            baseColor[1] =lerp(baseColor[1],targetColor2[1],pace)
            baseColor[2] =lerp(baseColor[2],targetColor2[2],pace)
            if math.fabs(targetColor2[0] - baseColor[0])<1:
                obj.condition = True

        return baseColor

class Cell:
    def __init__(self,x,y,size,state=False):
        self.x = x
        self.y = y
        self.size = size
        self.alive = state
        self.color = [199, 44, 65]
        self.color2 = [128, 19, 54]
        self.tempColor = [199,44,65]  
        self.condition = True

    def draw(self, screen): 
        if self.alive:        
            self.tempColor = lerpColor(self,self.tempColor,self.color,self.color2,0.1)
            pygame.draw.rect(screen, self.tempColor,(self.x*self.size, self.y*self.size,self.size,self.size))
        else:
            pygame.draw.rect(screen, ("#801336"),(self.x*self.size, self.y*self.size,self.size,self.size),1)

    
