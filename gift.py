import pygame
import settings
s = settings

class Giftbox():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.img = self.Gifttypes[color]
        self.mask = pygame.mask.from_surface(self.img)
        self.gift_rect = self.img.get_rect(center=(self.x, self.y))

    Gifttypes = {
        "red": pygame.image.load("resources/gift.png"),
        "blue": pygame.image.load("resources/bonus.png")
        }
#til tb kode med collide
    def bagged(self):
        self.gift_rect.centerx = s.width + 200

    def draw(self, window):
        #window.blit(self.img,self.x, self.y))
        window.blit(self.img,self.gift_rect)

    def move(self, vel):
        #self.y += vel
        self.gift_rect.centery += vel

    def rect(self):
        gift_rect = self.img.get_rect(center=(self.x, self.y))
        return gift_rect
