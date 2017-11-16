# Игра камнепад
# Игрок должен уворачиваться от падающих с неба камней
from livewires import games, color
import random

games.init(screen_width=800, screen_height=500, fps=50)

class Men(games.Sprite):
    """Человечек, который будет уворачиваться от камней."""
    image = games.load_image("man.gif")

    def __init__(self):
        """Инициализирует объект Men."""
        super(Men, self).__init__(image=Men.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.simple_timer = 0

    def update(self):
        """Передвигает объект по горизонтали в точку с абсциссой, как у указателя мыши."""
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()


    def check_catch(self):
        """Проверяет, не столкнулся ли игрок с камнем."""
        for rock in self.overlapping_sprites:
            rock.handle_caught()
            rock.end_game()


class Rock(games.Sprite):
    """Камни, падающие на землю."""
    image = games.load_image("rock.png")
    speed = 1

    def __init__(self, x, y, dy):
        """Инициализирует объект Rock."""
        super(Rock, self).__init__(image=Rock.image,
                                    x=x, y=y,
                                    dy=dy)
        self.Pizza_speed = Rock.speed


    def update(self):
        """Проверяет, не коснулась ли нижняя кромка спрайта нижней границы экрана."""
        if self.bottom > games.screen.height:
            self.destroy()

    def handle_caught(self):
        """Разрушает объект, пойманный игроком."""
        self.destroy()

    def end_game(self):
        """Завершает игру."""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

class Sky(games.Sprite):
    """Небо, которое, двигаясь влево-вправо, разбрасывает камни."""
    image = games.load_image("pixel.png")
    speed = games.screen.fps/10

    def __init__(self, y=55, odds_change=200):
        """Инициализирует объект Sky и счетчик для количества камней."""
        super(Sky, self).__init__(image=Sky.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=Sky.speed)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)
        self.odds_change = odds_change
        self.time_til_drop = 0
        self.speed = Sky.speed
        self.change_speed = 2

    def update(self):
        """Определяет, надо ли сменить направление и уменьшить скорость."""
        if self.dx < 2 or self.dx < -2:
            if self.left < 0 or self.right > games.screen.width:
                self.dx = -self.dx
            elif random.randrange(self.odds_change) == 0:
                self.dx = -self.dx
        else:
            if self.left < 0 or self.right > games.screen.width:
                self.dx = -self.dx/1.05
            elif random.randrange(self.odds_change) == 0:
                self.dx = -self.dx/1.05
        self.check_drop()
        # плавно увеличиваем скорость каждого нового камня
        self.change_speed_of_rock()

    def change_speed_of_rock(self):
        if self.change_speed < 5:
            self.change_speed += 0.001

    def check_drop(self):
        """Уменьшает интервал ожидания на единицу или сбрасывает очередной камень и восстанавливает исходный интервал."""
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_rock = Rock(x=self.x, y=0, dy=self.change_speed)
            self.score.right = games.screen.width - 10
            self.score.value += 10
            games.screen.add(new_rock)
            # вне зависимости от скорости падения камня "зазор" между падающими кругами принимается равным 20% каждого из них по высоте
            self.time_til_drop = int(new_rock.height*1.2/Rock.speed) + 1


def main():
    wall_image = games.load_image("landscape.jpg", transparent=False)
    games.screen.background = wall_image
    the_men = Men()
    games.screen.add(the_men)
    the_rocks = Sky()
    games.screen.add(the_rocks)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()