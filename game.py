import pygame,sys

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ninja game")#change name of the window
        self.screen = pygame.display.set_mode((640,480)) #function that creates the screen
        self.clock = pygame.Clock()#Clock object

        self.image = pygame.image.load("data/images/clouds/cloud_1.png")#loads an image and creates a Surface

        self.image_pos = [300,300]
        self.image.set_colorkey((0, 0, 0)) # A color key is to say pygame what color of the image will treat as trasparent , in these case 0,0,0(black)
        self.movement = [False,False]
   
        self.collision_area = pygame.Rect(50,50,300,50)#first two parameters r the pos and the rest the width and height

    def run(self):
        while True:
            self.screen.fill((14,219,248))

            image_rect = pygame.Rect(*self.image_pos, *self.image.get_size())
            #UGLIER WAY BUT EASIER --> img_r = pygame.Rect(self.image_pos[0] , self.image_pos[1] , self.image.get_width() , self.image.get_height())
        
            if image_rect.colliderect(self.collision_area):
                pygame.draw.rect(self.screen,"blue",self.collision_area)#1 draws a Rect, 2 where it draws, 3 color, 4 select which rect to render           
            else:
                pygame.draw.rect(self.screen,"red",self.collision_area)#same but red


            #updates position
            self.image_pos[1] += (self.movement[1] - self.movement[0])*5 #booleans r converted to 1 or 0
            print(self.movement)
            self.screen.blit(self.image,self.image_pos)#blit draws a Surface on top of another(screen)

            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Movement
                if event.type == pygame.KEYDOWN: #expects any key to be pressed, if the key is the up arrow,movement[0] will become True
                    if event.key == pygame.K_w:   
                        self.movement[0] = True                         
                    if event.key == pygame.K_s: #expects any key to be pressed, if the key is the up arrow,movement[1] will become True   
                        self.movement[1] = True
                #Makes the oposite
                if event.type == pygame.KEYUP: 
                    if event.key == pygame.K_w:   
                        self.movement[0] = False                        
                    if event.key == pygame.K_s:
                        self.movement[1] = False
                    
                
        
            pygame.display.update()
            self.clock.tick(60)



Game().run()