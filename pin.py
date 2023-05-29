from pygame import *
back = (200,255,255)
window = display.set_mode((700,500))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__ (self, player_img, player_x, player_y,width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600 - 80:
            self.rect.x += self.speed


raket1 = Player('ракетка.png',30 ,200, 4, 50, 150)
raket2 = Player('ракетка2.png', 520, 200, 4, 50, 150)
ball = GameSprite('мячик.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if  finish != True:
        window.fill(back)
    



    display.update()
    clock.tick(FPS)