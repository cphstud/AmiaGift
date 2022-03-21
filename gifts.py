from gift import Giftbox
import settings, random
from random import randint
s=settings
#endnu ikke færdig liste med aliens/gaver


class Gifts():
    def __init__(self, settings,screen):
        self.conf=settings
        self.screen=screen
        self.list_of_gift = self.init_targets()

    def init_targets(self):
        gifts = []
        for i in range(s.spawn):
            gift = Giftbox(randint(s.delta, s.width - s.delta), randint(-1000, -100), random.choice(["red", "blue"]))
            s.speed = randint(1, 7)
            gifts.append(gift)
        return gifts