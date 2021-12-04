from pygame import *
mixer.init()
font.init()
from random import randint
win_wid = 700
win_hei = 500
clock = time.Clock()
FPS = 60
window = display.set_mode((win_wid, win_hei))
display.set_caption("Shooter")
game = True
font1 = font.SysFont('Arial', 36)
finish = False
score = 0
goal = 10
lost = 0
max_l = 5
lose = font1.render("YOU LOSE", True, (240, 248, 255))
win = font1.render("YOU WIN", True, (240, 248, 255))

mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
back = 'galaxy.jpg'
background = transform.scale(image.load(back), (win_wid, win_hei))
rocket = image.load('rocket.png')
ufo = image.load('ufo.png')
bull = image.load('bullet.png')


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(rocket, (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect
        self.rect_x = player_x
        self.rect_y = player_y
    def reset(self):
        window.blit(self.image, (self.rect_x, self.rect_y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys[K_RIGHT] and self.rect_x < win_width - 80:
            self.rect_x += self.speed
        global kill 
    def fire(self):
        mixer.music.play(fire_sound)
        bullet = Bullet(bull, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

bullets = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.image = transform.scale(image.load(bull), (size_x, size_y))
        self.rect_y += self.speed
        if self.rect_y < 0:
            self.kill()

class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.speed
        global lost
        if self.rect.y > win_hei:
            self.rect.x = randint(80, win_wid - 80)
            self.rect.y = 0
            lost = lost + 1 

player = Player(rocket, 450, - 500, 80, 100, 10)
enemies = sprite.Group()
while game:
    for e in event.get():
        if e.type == QUIT:
            game == False
        elif e.type == KEYDOWN:
            if e.type == [SPACE]:
                    ship.fire()
    if not finish:
        window.blit(background, (0, 0))
        bullets.update()
        player.update()
        enemies.update()

        player.reset()
        enemies.draw(window)
        bullets.draw(window)
        
        collides = sprite.groupcollide(enemies, bullets, True, True)
        for с in collides:
            score = score+1
            monster = Enemy(ufo, randint(80, win_wid-80, -40, 80, 50, randint(1,5)))
            monsters.add(monster)
        #lose
        if sprite.spritecollide(player, enemies, False) or lost >= max_l:
            finish == True
            window.blit(lose, (200, 200))
        #win
        if score >= goal:
            finish == True
            window.blit(win,(200,200))
        #text on screen
        text_lose = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10,50))
        text = font2.render("Счет:" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        display.update()
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in enemies:
                m.kill()

time.delay(3000)
for i in range(1,6):
    monster = Enemy(ufo, randint(80, win_wid - 80, -40, 80, 50, randint(1,5)))
    monsters.add(monster)
time.delay(50)    

