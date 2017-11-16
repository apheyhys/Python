# Ускользающая пицца
# Демонстрирует проверку на соприкосновение спрайтов
from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Pan(games.Sprite):
    """Перемещаемая мыщью сковорода."""
    def update(self):
        """Перемещает объект в позицию указателя."""
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """Проверяет, не соприкоснулись ли сковорода и пицца."""
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

class Pizza(games.Sprite):
    """Ускользающая пицца."""
    def handle_collide(self):
        """Перемещает спрайт в случайную позицию на графическом экране."""
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image("pizza.bmp")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    the_pizza = Pizza(image=pizza_image,
                  x=pizza_x,
                  y=pizza_y
                  )
    games.screen.add(the_pizza)
    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(
        image=pan_image,
        x=games.mouse.x,
        y=games.mouse.y
    )
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()


if __name__ == '__main__':
    main()