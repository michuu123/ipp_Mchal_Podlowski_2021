import random
import os
import pygame

podlogaO=pygame.image.load(os.path.join('grafiki', 'podloga.png'))

class pokoj:
    def __init__(self):



        self.rozmiar_x=random.randrange(4)+5
        self.rozmiar_y=random.randrange(4)+5

        self.pozycja_x=random.randrange(9-self.rozmiar_x)
        self.pozycja_y=random.randrange(9-self.rozmiar_y)



        self.bok1x=random.randrange(4-self.pozycja_x)
        self.bok1y=random.randrange(4-self.pozycja_y)
        if self.bok1x==0 or self.bok1y==0:
            self.bok1x=0
            self.bok1y=0

        self.bok2x=random.randrange(self.rozmiar_x+self.pozycja_x-4)
        self.bok2y=random.randrange(4-self.pozycja_y)
        if self.bok2x==0 or self.bok2y==0:
            self.bok2x=0
            self.bok2y=0

        self.bok3x=random.randrange(self.rozmiar_x+self.pozycja_x-4)
        self.bok3y=random.randrange(self.rozmiar_y+self.pozycja_y-4)
        if self.bok3x==0 or self.bok3y==0:
            self.bok3x=0
            self.bok3y=0

        self.bok4x=random.randrange(4-self.pozycja_x)
        self.bok4y=random.randrange(self.rozmiar_y+self.pozycja_y-4)
        if self.bok4x==0 or self.bok4y==0:
            self.bok4x=0
            self.bok4y=0



        self.lewa_sciana=[]
        self.prawa_sciana=[]
        self.dolna_sciana=[]
        self.gorna_sciana=[]
        self.podloga=[]
        self.prawy_dolny=[]
        self.lewy_dolny=[]
        self.prawy_gorny=[]
        self.lewy_gorny=[]
        self.prawy_dolny2=[]
        self.lewy_dolny2=[]
        self.prawy_gorny2=[]
        self.lewy_gorny2=[]
        self.podloga=[]
        self.test=[]



        for x in range(self.rozmiar_y-self.bok1y-self.bok4y):
            self.lewa_sciana.append(pygame.Rect(self.pozycja_x*48,(self.pozycja_y+self.bok1y+x+1)*48,48,48))

        for x in range(self.rozmiar_y-self.bok2y-self.bok3y):
            self.prawa_sciana.append(pygame.Rect(48*(self.rozmiar_x+self.pozycja_x+1),(self.pozycja_y+self.bok2y+x+1)*48,48,48))

        for x in range(self.rozmiar_x-self.bok1x-self.bok2x):
            self.gorna_sciana.append(pygame.Rect((self.pozycja_x+self.bok1x+x+1)*48,self.pozycja_y*48,48,48))

        for x in range(self.rozmiar_x-self.bok3x-self.bok4x):
            self.dolna_sciana.append(pygame.Rect((self.pozycja_x+self.bok4x+x+1)*48,48*(self.rozmiar_y+self.pozycja_y+1),48,48))
        


        if self.bok1x==0:
            self.lewy_gorny.append(pygame.Rect(self.pozycja_x*48,self.pozycja_y*48,48,48))
        else:
             self.lewy_gorny.append(pygame.Rect((self.pozycja_x+self.bok1x)*48,self.pozycja_y*48,48,48))
             self.lewy_gorny.append(pygame.Rect(self.pozycja_x*48,(self.pozycja_y+self.bok1y)*48,48,48))
             self.prawy_dolny.append(pygame.Rect((self.pozycja_x+self.bok1x)*48,(self.pozycja_y+self.bok1y)*48,48,48))
             if self.bok1y!=0:
                for x in range(self.bok1y-1):
                    self.lewa_sciana.append(pygame.Rect((self.pozycja_x+self.bok1x)*48,(self.pozycja_y+x+1)*48,48,48))
                for x in range(self.bok1x-1):
                    self.gorna_sciana.append(pygame.Rect((self.pozycja_x+x+1)*48,(self.pozycja_y+self.bok1y)*48,48,48))
        

        if self.bok2x==0:
            self.prawy_gorny.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,self.pozycja_y*48,48,48))
        else:
            self.prawy_gorny.append(pygame.Rect((self.pozycja_x+self.rozmiar_x-self.bok2x+1)*48,self.pozycja_y*48,48,48))
            self.prawy_gorny.append(pygame.Rect(48*(self.rozmiar_x+self.pozycja_x+1),(self.pozycja_y+self.bok2y)*48,48,48))
            self.lewy_dolny.append(pygame.Rect((self.pozycja_x+self.rozmiar_x-self.bok2x+1)*48,(self.pozycja_y+self.bok2y)*48,48,48))
            if self.bok2y!=0:
                for x in range(self.bok2y-1):
                    self.prawa_sciana.append(pygame.Rect((self.pozycja_x+self.rozmiar_x-self.bok2x+1)*48,(self.pozycja_y+x+1)*48,48,48))
                for x in range(self.bok2x-1):
                    self.gorna_sciana.append(pygame.Rect((self.pozycja_x+self.rozmiar_x-x)*48,(self.pozycja_y+self.bok2y)*48,48,48))


        if self.bok3x==0:
            self.prawy_dolny2.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))
        else:
            self.prawy_dolny2.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,(self.pozycja_y+self.rozmiar_y-self.bok3y+1)*48,48,48))
            self.prawy_dolny2.append(pygame.Rect((self.rozmiar_x+self.pozycja_x+1-self.bok3x)*48,(self.rozmiar_y+self.pozycja_y+1)*48,48,48))
            self.lewy_gorny2.append(pygame.Rect((self.rozmiar_x+self.pozycja_x+1-self.bok3x)*48,(self.pozycja_y+self.rozmiar_y-self.bok3y+1)*48,48,48))
            if self.bok3y!=0:
                for x in range(self.bok3y-1):
                    self.prawa_sciana.append(pygame.Rect((self.rozmiar_x+self.pozycja_x+1-self.bok3x)*48,(self.pozycja_y+self.rozmiar_y-self.bok3y+2+x)*48,48,48))
                for x in range(self.bok3x-1):
                    self.dolna_sciana.append(pygame.Rect((self.rozmiar_x+self.pozycja_x+1-self.bok3x+x+1)*48,(self.pozycja_y+self.rozmiar_y-self.bok3y+1)*48,48,48))


        if self.bok4x==0:
            self.lewy_dolny2.append(pygame.Rect((self.pozycja_x)*48,(self.rozmiar_y+self.pozycja_y+1)*48,48,48))
        else:
            self.lewy_dolny2.append(pygame.Rect((self.pozycja_x)*48,(self.pozycja_y+self.rozmiar_y-self.bok4y+1)*48,48,48))
            self.lewy_dolny2.append(pygame.Rect((self.pozycja_x+self.bok4x)*48,(self.rozmiar_y+self.pozycja_y+1)*48,48,48))
            self.prawy_gorny2.append(pygame.Rect((self.pozycja_x+self.bok4x)*48,(self.pozycja_y+self.rozmiar_y-self.bok4y+1)*48,48,48))
            if self.bok4y!=0:
                for x in range(self.bok4y-1):
                    self.lewa_sciana.append(pygame.Rect((self.pozycja_x+self.bok4x)*48,(self.pozycja_y+self.rozmiar_y-self.bok4y+2+x)*48,48,48))
                for x in range(self.bok4x-1):
                    self.dolna_sciana.append(pygame.Rect((self.pozycja_x+self.bok4x-x-1)*48,(self.pozycja_y+self.rozmiar_y-self.bok4y+1)*48,48,48))

        self.lewa_sciana.remove(pygame.Rect(self.pozycja_x*48,4*48,48,48))
        self.lewa_sciana.remove(pygame.Rect(self.pozycja_x*48,5*48,48,48))

        self.prawa_sciana.remove(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,4*48,48,48))
        self.prawa_sciana.remove(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,5*48,48,48))

        self.gorna_sciana.remove(pygame.Rect(4*48,self.pozycja_y*48,48,48))
        self.gorna_sciana.remove(pygame.Rect(5*48,self.pozycja_y*48,48,48))

        self.dolna_sciana.remove(pygame.Rect(4*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))
        self.dolna_sciana.remove(pygame.Rect(5*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))

        "prawe wejscie"

        for x in range(8-self.pozycja_x-self.rozmiar_x):
            self.gorna_sciana.append(pygame.Rect((x+self.pozycja_x+self.rozmiar_x+2)*48,3*48,48,48))
            self.dolna_sciana.append(pygame.Rect((x+self.pozycja_x+self.rozmiar_x+2)*48,6*48,48,48))
        
        if self.pozycja_y+self.bok2y==3:
            self.gorna_sciana.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,3*48,48,48))
        
        else:
            self.prawa_sciana.remove(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,3*48,48,48))
            self.lewy_dolny.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,3*48,48,48))

        if self.pozycja_y+self.rozmiar_y-self.bok3y==5:
            self.dolna_sciana.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,6*48,48,48))

        else:
            self.prawa_sciana.remove(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,6*48,48,48))
            self.lewy_gorny2.append(pygame.Rect((self.pozycja_x+self.rozmiar_x+1)*48,6*48,48,48))

        "lewe wejście"

        for x in range(self.pozycja_x):
            self.gorna_sciana.append(pygame.Rect(x*48,3*48,48,48))
            self.dolna_sciana.append(pygame.Rect(x*48,6*48,48,48))
        
        if self.pozycja_y+self.bok1y==3:
            self.gorna_sciana.append(pygame.Rect((self.pozycja_x)*48,3*48,48,48))
        
        else:
            self.lewa_sciana.remove(pygame.Rect((self.pozycja_x)*48,3*48,48,48))
            self.prawy_dolny.append(pygame.Rect((self.pozycja_x)*48,3*48,48,48))

        if self.pozycja_y+self.rozmiar_y-self.bok4y==5:
            self.dolna_sciana.append(pygame.Rect((self.pozycja_x)*48,6*48,48,48))

        else:
            self.lewa_sciana.remove(pygame.Rect((self.pozycja_x)*48,6*48,48,48))
            self.prawy_gorny2.append(pygame.Rect((self.pozycja_x)*48,6*48,48,48))

        "gorne wejście"

        for x in range(self.pozycja_y):
            self.lewa_sciana.append(pygame.Rect(3*48,x*48,48,48))
            self.prawa_sciana.append(pygame.Rect(6*48,x*48,48,48))
        
        if self.pozycja_x+self.bok1x==3:
            self.lewa_sciana.append(pygame.Rect(3*48,self.pozycja_y*48,48,48))
        
        else:
            self.gorna_sciana.remove(pygame.Rect(3*48,self.pozycja_y*48,48,48))
            self.prawy_dolny.append(pygame.Rect(3*48,self.pozycja_y*48,48,48))

        if self.pozycja_x+self.rozmiar_x-self.bok2x==5:
            self.prawy_gorny.remove(pygame.Rect(6*48,self.pozycja_y*48,48,48))
            self.prawa_sciana.append(pygame.Rect(6*48,self.pozycja_y*48,48,48))

        else:
            self.gorna_sciana.remove(pygame.Rect(6*48,self.pozycja_y*48,48,48))
            self.lewy_dolny.append(pygame.Rect(6*48,self.pozycja_y*48,48,48))
        

        "dolne wejscie"

        for x in range(8-self.pozycja_y-self.rozmiar_y):
            self.lewa_sciana.append(pygame.Rect(3*48,(x+self.pozycja_y+self.rozmiar_y+2)*48,48,48))
            self.prawa_sciana.append(pygame.Rect(6*48,(x+self.pozycja_y+self.rozmiar_y+2)*48,48,48))
        
        if self.pozycja_x+self.bok4x==3:
            self.lewa_sciana.append(pygame.Rect(3*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))
        
        else:
            self.dolna_sciana.remove(pygame.Rect(3*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))
            self.prawy_gorny2.append(pygame.Rect(3*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))

        if self.pozycja_x+self.rozmiar_x-self.bok3x==5:
            self.prawa_sciana.append(pygame.Rect(6*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))

        else:
            self.dolna_sciana.remove(pygame.Rect(6*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))
            self.lewy_gorny2.append(pygame.Rect(6*48,(self.pozycja_y+self.rozmiar_y+1)*48,48,48))

            "podloga"

        for x in range(10):
            self.podloga.append(pygame.Rect(4*48,x*48,48,48))
            self.podloga.append(pygame.Rect(5*48,x*48,48,48))
            self.podloga.append(pygame.Rect(x*48,4*48,48,48))
            self.podloga.append(pygame.Rect(x*48,5*48,48,48))

            "podloga lewy gorny"

        for x in range(self.bok1y):
            for y in range(3-self.bok1x-self.pozycja_x):
                self.podloga.append(pygame.Rect((self.pozycja_x+self.bok1x+1+y)*48,(self.pozycja_y+x+1)*48,48,48))
        for x in range(3-self.bok1y-self.pozycja_y):
            for y in range(3-self.pozycja_x):
                self.podloga.append(pygame.Rect((self.pozycja_x+1+y)*48,(self.bok1y+self.pozycja_y+x+1)*48,48,48))

            "podloga prawy gorny"

        for x in range(self.pozycja_x+self.rozmiar_x-self.bok2x-5):
            for y in range(self.bok2y):
                self.podloga.append(pygame.Rect((6+x)*48,(self.pozycja_y+y+1)*48,48,48))

        for x in range(self.pozycja_x+self.rozmiar_x-5):
            for y in range(3-self.pozycja_y-self.bok2y):
                self.podloga.append(pygame.Rect((6+x)*48,(self.pozycja_y+self.bok2y+y+1)*48,48,48))


            "podloga prawy dolny"
        
        for x in range(self.pozycja_x+self.rozmiar_x-self.bok3x-5):
            for y in range(self.bok3y):
                self.podloga.append(pygame.Rect((6+x)*48,(self.pozycja_y+self.rozmiar_y-y)*48,48,48))
        for x in range(self.rozmiar_x+self.pozycja_x-5): 
            for y in range(self.rozmiar_y+self.pozycja_y-self.bok3y-5):
                self.podloga.append(pygame.Rect((6+x)*48,(self.pozycja_y+self.rozmiar_y-y-self.bok3y)*48,48,48))

            "podloga lewy dolny"

        for x in range(3-self.pozycja_x-self.bok4x):
            for y in range(self.bok4y):
                self.podloga.append(pygame.Rect((self.pozycja_x+self.bok4x+x+1)*48,(self.pozycja_y+self.rozmiar_y-y)*48,48,48))
        for x in range(3-self.pozycja_x):
            for y in range(self.pozycja_y+self.rozmiar_y-self.bok4y-5):
                self.podloga.append(pygame.Rect((self.pozycja_x+x+1)*48,(6+y)*48,48,48))


        
    def rzut(self,x,y):


        for x in self.lewy_gorny:
            pygame.draw.rect(ekran,(0,100,255),x,4)

        for x in self.prawy_dolny:
            pygame.draw.rect(ekran,(255,150,0),x,4)

        for x in self.prawy_gorny:
            pygame.draw.rect(ekran,(255,255,0),x,4)

        for x in self.prawy_dolny2:
            pygame.draw.rect(ekran,(255,150,0),x,4)

        for x in self.lewy_gorny2:
            pygame.draw.rect(ekran,(0,100,255),x,4)

        for x in self.lewy_dolny:
            pygame.draw.rect(ekran,(150,0,150),x,4)
            
        for x in self.prawa_sciana:
            pygame.draw.rect(ekran,(255,255,255),x,4)

        for x in self.gorna_sciana:
            pygame.draw.rect(ekran,(255,0,0),x,4)
        
        for x in self.lewy_dolny2:
            pygame.draw.rect(ekran,(150,0,150),x,4)

        for x in self.prawy_gorny2:
            pygame.draw.rect(ekran,(255,255,0),x,4)

        for x in self.lewa_sciana:
            pygame.draw.rect(ekran,(100,150,0),x,4)

        for x in self.dolna_sciana:
            pygame.draw.rect(ekran,(0,255,255),x,4)

        for x in self.podloga:
            ekran.blit(podlogaO,x)

        for x in self.test:
            pygame.draw.rect(ekran,(100, 255, 50),x,4)


if __name__ == "__main__":
    import pygame
    print("elo")
    x = pokoj()
    print("rozmiar x - " + str(x.rozmiar_x))
    print("rozmiar y - " + str(x.rozmiar_y))
    print("pozycja x - " + str(x.pozycja_x))
    print("pozycja y - " + str(x.pozycja_y))
    print(x.bok2x)
    print(x.bok2y)


    ekran = pygame.display.set_mode((500,500))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        ekran.fill((0,0,0))
        x.rzut(15,12)
        pygame.display.flip()






