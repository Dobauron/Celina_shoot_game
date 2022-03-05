# Dobromir Matuszak 2022

# Celina shoot game
from livewires import games

import random

games.init(screen_width = 1100, screen_height = 825, fps = 50)

celina_image = games.load_image("celina.jpg", transparent = False)

games.screen.background = celina_image



class Mewa(games.Sprite):
    image = games.load_image("mewa1.bmp")
    image2 = games.load_image("mewa2.jpg")
    list_of_mewy = [image, image2]

    TIME_RESPAWN = 200

    def __init__(self):
        rand_mewa = random.randrange(len(Mewa.list_of_mewy))
        super(Mewa, self).__init__(image = Mewa.list_of_mewy[rand_mewa],
                                  x = random.randrange(games.screen.width-10),
                                  y = random.randrange(games.screen.height-10),
                                  dx = random.randrange(1,3),
                                  dy = random.randrange(1,3),
                                  )

        self.dead = False
        self.time_respawn = random.randrange(Mewa.TIME_RESPAWN, 400)

    def update(self):

        if self.right > games.screen.width or self.left <0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top <0:
            self.dy = -self.dy

        if self.dead == 1:
            if self.top < self.falling:
                self.dy = - self.dy
            if self.bottom > games.screen.height -15:
                self.destroy()



    def respawn(self):
        self.time_respawn -=1
        if self.time_respawn == 0:
            mewa = Mewa()
            games.screen.add(mewa)
            self.time_respawn =200

    def die(self):
        self.angle = -180
        self.dx = 0
        self.falling = self.top
        self.dead = True




class Celownik(games.Sprite):
    target_image = games.load_image("celownik.jpg")
    Reload =3


    def __init__(self):
        super(Celownik, self).__init__(image = Celownik.target_image,
                                       x = games.mouse.x,
                                       y = games.mouse.y,
                                       is_collideable=False)
        self.update()
        self.reload = Celownik.Reload


    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        if games.mouse.is_pressed(games.BUTTON_MIDDLE):
            self.reload -= 1
            if self.reload == 0:
                shoot = Bullet()
                games.screen.add(shoot)
                self.reload =50



class Bullet(games.Sprite):
    bullet_image = games.load_image("kula.jpg")
    LIFETIME =30
    bullet_sound = games.load_sound("shoot.mp3")


    def __init__(self):
        Bullet.bullet_sound.play()
        super(Bullet, self).__init__(image = Bullet.bullet_image,
                                     x = games.mouse.x,
                                     y = games.mouse.y,
                                     is_collideable=False
                                     )

        self.lifetime = Bullet.LIFETIME

    def update(self):
        self.lifetime -=2
        if self.lifetime==0:
            self.destroy()
        self.check_collide()


    def check_collide(self):
        for mewa in self.overlapping_sprites:
            mewa.die()

celownik = Celownik()

for i in range(8):

    mewa= Mewa()
    games.screen.add(mewa)

games.mouse.is_visible= False

games.screen.even_grab= True


games.screen.add(celownik)
games.screen.background = celina_image

games.screen.mainloop()