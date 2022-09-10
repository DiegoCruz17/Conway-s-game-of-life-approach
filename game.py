import pygame, math,sys
from eco import Ecosystem as eco
from cell import lerpColor

#Game class, where methods such as drawing the ecosystem and getting events, are declared.

class Game:
    def __init__(self,cellsNum,frameRate):
        pygame.init()
        
        #instead of creating a simple color variable, I worked with arrays so I could later interpolate between them.
        self.CANVAS_COLOR = [45, 20, 44]
        self.MENU_COLOR = [81, 10, 50]
        self.TEMP_COLOR = [45, 20, 44]
        
        self.condition = True
        self.frameRate = frameRate
        self.cellsNum = cellsNum
        self.canvas_size = 500
        self.menu_size = 250
        
        self.screen = pygame.display.set_mode((self.canvas_size+ self.menu_size,self.canvas_size))
        pygame.display.set_caption("Conway's game of life")
        self.font = pygame.font.Font("OpenSans-Light.ttf",18)
        self.clock = pygame.time.Clock()
        self.eco = eco(self.cellsNum,self.canvas_size)
        
        #The following are various button variables for the button management system I built down below. Probably, It would be better to create those on a utils class.
        self.buttons = []
        self.entryText = ''
        self.entryActive = False
        self.createButton(1,"RESET",self.reset)
        self.createButton(2,"CLEAR",self.clear)
        self.createButton(3,"PAUSE/RESUME", self.changeState)
        self.createButton(4,"# OF CELLS",None)

    #The x_holder variable lets me place the button's center on the middle of the menu panel. Also, this button system allows a button implementation,
    #where you can create buttons that call a function or not, and buttons that have no text.
    def createButton(self,y,text:str,func = None,empty = False):
        
        x_holder = self.menu_size // 3
        if not empty:
            txt = self.font.render(text,True,("#faf4d3"))
            button_rect = pygame.Rect(self.canvas_size + x_holder,y,txt.get_width()+20,40)   
            button_rect.center = (self.canvas_size + self.menu_size // 2, y * (self.canvas_size -120) // 4) 
            text_rect = txt.get_rect()
            text_rect.center = button_rect.center
        else:
            txt = self.font.render(text,True,("#faf4d3"))
            button_rect = pygame.Rect(self.canvas_size + x_holder,y,x_holder,40)   
            button_rect.center = (self.canvas_size + self.menu_size // 2, y * (self.canvas_size -120) // 4) 
            text_rect = txt.get_rect()
            text_rect.center = button_rect.center

        self.buttons.append([button_rect,txt,text_rect,func])

    def drawButton(self):
        BUTTONS_COLOR = "#EE4540"
        OUTLINE_COLOR = "#faf4d3"
        for button in self.buttons:

            pygame.draw.rect(self.screen,(BUTTONS_COLOR),button[0])
            pygame.draw.rect(self.screen,(OUTLINE_COLOR),button[0],1)
            self.screen.blit(button[1],button[2])
    #reset() lets the user create a new ecosystem according to the set number of cells.    
    def reset(self):
        self.eco = eco(self.cellsNum,self.canvas_size)
    #changing the setting toggles the game state from setting the board to simulating.
    def changeState(self):
        self.eco.setting = not self.eco.setting 
    #toggles all cells to a 'dead' state.
    def clear(self):
        self.eco.resetCells()
    def drawMenu(self):
        self.TEMP_COLOR = lerpColor(self,self.TEMP_COLOR,self.CANVAS_COLOR,self.MENU_COLOR,0.05)
        pygame.draw.rect(self.screen,(self.TEMP_COLOR),(self.canvas_size,0,self.menu_size,self.canvas_size))
        pygame.draw.rect(self.screen,("#faf4d3"),(self.canvas_size,0,self.menu_size,self.canvas_size),1)
        self.drawButton()


    def render(self):
        self.screen.fill(self.CANVAS_COLOR)
        self.drawMenu()
        self.eco.updateEco(self.screen)
        self.clock.tick(self.frameRate)
        pygame.display.flip()
    
    def getEvents(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = math.floor(mouse_pos[0]/(self.canvas_size/self.eco.boardsize))
        mouse_y = math.floor(mouse_pos[1]/(self.canvas_size/self.eco.boardsize)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0] == 1:
                if event.pos[0] >= 0 and event.pos[0] <= self.canvas_size + self.menu_size:
                    if mouse_pos[0] <= self.canvas_size:
                        self.eco.cells[mouse_y][mouse_x].alive = True
                    for button in self.buttons:
                        if button[0].collidepoint(event.pos):
                            if button[3] != None:
                                button[3]()
                            else:
                                self.entryActive = not self.entryActive
                                print(self.entryActive)
            if pygame.mouse.get_pressed()[2] == 1:
                if mouse_pos[0] <= self.canvas_size:
                    self.eco.cells[mouse_y][mouse_x].alive = False
            #After interacting with the button that changes the number of cells, type a number and press space.
            if self.entryActive:
                if event.type == pygame.KEYDOWN:
                    self.entryText += event.unicode
                    pygame.draw.rect(self.screen,(0,0,0),self.buttons[3][0],1)
                    if event.key == pygame.K_SPACE:
                        self.cellsNum = int(self.entryText)
                        self.eco = eco(self.cellsNum,self.canvas_size)
                        self.entryText = ""
                        self.entryActive = False
