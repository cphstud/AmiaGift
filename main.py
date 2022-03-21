import sys
import pygame
import random
import settings
import graphics

from random import randint
from player import Bagplayer
from gift import Giftbox
pygame.init()
s= settings
grap =graphics

#Entiteter
baggie = Bagplayer(300, 650)
gifts = []


"""main def"""
def main():
    run = True
    while run:
        s.Window.fill(s.WHITE)
        # tjek events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed() # Brug af piltaster til Playerbag

                if keys[pygame.K_LEFT]:
                    #baggie.x -= s.player_vel
                    baggie.movex(s.player_vel)
                if keys[pygame.K_RIGHT]:
                    baggie.movex(-s.player_vel)
                    #baggie.x += s.player_vel
                if keys[pygame.K_UP]:
                    baggie.movey(-s.player_vel)
                    #baggie.y -= s.player_vel
                if keys[pygame.K_DOWN]:
                    baggie.movey(s.player_vel)
                    #baggie.y += s.player_vel


        if len(gifts) == 0:
            s.level += 1
            s.spawn = 3
            for i in range(s.spawn):
                gift = Giftbox(randint(s.delta, s.width - s.delta), randint(-1000,0), random.choice(["red", "blue"]))
                s.speed = randint(1, 7)
                gifts.append(gift)


        for gift in gifts:
            if baggie.rect.colliderect(gift.gift_rect):
                #gift.remove(gifts)
                #gift.y=-100
                gifts.remove(gift)
                s.points = s.points +1
                #gift.bagged()
            elif gift.gift_rect.centery >= s.height:
                #gift.x = randint(0, s.width)
                gifts.remove(gift)
                #gift.y = 0
                s.gift_vel = 3
            else:
                gift.move(s.gift_vel)
                gift.draw(s.Window)

        #grap.draw_window() # Tegne grafik
        baggie.draw(s.Window)
        s.pygame.display.update()
        s.clock.tick(s.FPS)

#herunder ! Gør at filen kun kører herfra
if __name__ == '__main__':
    main()
