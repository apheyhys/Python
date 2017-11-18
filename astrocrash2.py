# Прерванный полет-2
# Только астероиды движутся по экрану
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
    ROTATION_STEP = 3

    def update(self):
        """Вращает корабль при нажатии клавиш со стрелками."""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP


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
    the_ship = Ship(image=Ship.image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()

main()