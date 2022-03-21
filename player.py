import settings,pygame
s = settings

class Bagplayer():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("resources/bag.png")
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw(self, window):
        #window.blit(self.img, (self.x, self.y))
        window.blit(self.img, (self.rect))


    def movex(self, pos):
        self.rect.centerx+=pos

    def movey(self, pos):
        self.rect.centery+=pos


#thorbjørn kode
    def shipCollision(self,other):
        retVal=0
        if (self.rect.colliderect(other)):
            retVal=1
        return retVal


#tim kode
    def collision(self, obj):
        return collide(self, obj)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None