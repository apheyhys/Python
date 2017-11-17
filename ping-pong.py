# Пинг-понг
# Пользователь манипулирует ракеткой, шарик отскакивает от трех стенок
from livewires import games, color
import random

games.init(screen_width=480, screen_height=640, fps=50)

class Ball(games.Sprite):
    """Мяч"""
    image = games.load_image("ball.bmp")

    def __init__(self):
        """Инициализирует объект Ball. """
        super(Ball, self).__init__(image=Ball.image,
                                   x=games.screen.width / 2,
                                   y=games.screen.height / 2,
                                   dx=random.choice([2, 3, -2, -3]),
                                   dy=random.choice([2, 3, -2, -3])
                                   )

    def update(self):
        """Передвигает объект по горизонтали в точку с абсциссой, как у указателя мыши."""
        if self.left < 10 or self.right > games.screen.width-10:
            self.dx = -self.dx
        if self.top < 10:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.end_game()

    def end_game(self):
        """Завершает игру."""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

    # при соприкосновении спрайтов изменяем направление и увеличивем скорость движения мяча
    def change_move(self):
        self.dx = -self.dx*random.uniform(1.0, 1.3)
        self.dy = -self.dy*random.uniform(1.0, 1.3)


class Racket(games.Sprite):
    """Ракетка, которой отбивают мяч."""
    image = games.load_image("racket.bmp")

    def __init__(self):
        """Инициализирует объект Rocket и создает объект Text для отображения счета. """
        super(Racket, self).__init__(image=Racket.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=20, right=games.screen.width-20)
        games.screen.add(self.score)
        self.simple_timer = 0

    def update(self):
        """Передвигает объект по горизонтали в точку с абсциссой, как у указателя мыши."""
        self.x = games.mouse.x
        if self.left < -40:
            self.left = -40
        if self.right > games.screen.width-10:
            self.right = games.screen.width-10
        self.check_catch()

    def check_catch(self):
        """Проверяет, коснулся ли мяч ракетки."""
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 20
            ball.change_move()


def main():
    wall_image = games.load_image("table.png", transparent=False)
    games.screen.background = wall_image
    the_ball = Ball()
    games.screen.add(the_ball)
    the_racket = Racket()
    games.screen.add(the_racket)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()