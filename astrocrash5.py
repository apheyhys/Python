# Прерванный полет-5
import math, random
import random
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Asteroid(games.Sprite):
    """Астероид, прямолинейно движущийся по экрану."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {
        SMALL: games.load_image("asteroid_small.bmp"),
        MEDIUM: games.load_image("asteroid_med.bmp"),
        LARGE: games.load_image("asteroid_big.bmp")
    }
    SPEED = 2

    def __init__(self, x, y, size):
        """Инициализирует спрайт с изображением астероида."""
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1])*Asteroid.SPEED*random.random()/size,
            dy=random.choice([1, -1])*Asteroid.SPEED*random.random()/size
        )
        self.size = size

    def update(self):
        """Заставляет астероид обогнуть экран."""
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

class Ship(games.Sprite):
    """Корабль игрока."""
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        """Инициализирует спрайт с изображением космического корабля."""
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.missile_wait = 0

    def update(self):
        """Вращает корабль при нажатии клавиш со стрелками."""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        # корабль совершает рывок
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            # изменение горизонтальной и вертикальной скорости корабля с учетом угла поворота
            angle = self.angle * math.pi / 180 # преобразование в радианы
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        # корабль будет "огибать" экран
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # если запуск следующей ракеты пока еще не разрешен, вычесть 1 из длины оставшегося итервала ожидания
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # если нажат Пробел и интервал ожидания истек, выпустить ракету
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY


class Missile(games.Sprite):
    """Ракета, которую может выпустить космический корабль игрока."""
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """Инициализирует спрайт с изображением ракеты."""
        Missile.sound.play()
        # преобразование в радианы
        angle = ship_angle * math.pi / 180
        # вычисление начальной позиции ракеты
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y
        # вычисление горизонтальной и вертикальной скорости ракеты
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        # создание ракеты
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """Перемещает ракету"""
        # если срок существования ракеты истек, она исчезает
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
        # ракета будет "огибать" экран
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width


def main():
    # назначаем фоновую картинку
    nebula_image = games.load_image("nebula.jpg", transparent=False)
    games.screen.background = nebula_image
    # создаем 8 астероидов
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    # создаем корабль
    the_ship = Ship(x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()

main()