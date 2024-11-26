class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.collided = False

    def move_forward(self, field):
        # Move the car based on the direction
        if self.direction == "N" and self.y < field.height - 1:
            self.y += 1
        elif self.direction == "S" and self.y > 0:
            self.y -= 1
        elif self.direction == "E" and self.x < field.width - 1:
            self.x += 1
        elif self.direction == "W" and self.x > 0:
            self.x -= 1

    def rotate_left(self):
        # Rotate counter-clockwise: N -> W -> S -> E
        direction_order = ["N", "W", "S", "E"]
        idx = direction_order.index(self.direction)
        self.direction = direction_order[(idx + 1) % 4]

    def rotate_right(self):
        # Rotate clockwise: N -> E -> S -> W
        direction_order = ["N", "E", "S", "W"]
        idx = direction_order.index(self.direction)
        self.direction = direction_order[(idx + 1) % 4]

    def check_collision(self, other_car):
        if self.x == other_car.x and self.y == other_car.y:
            self.collided = True
            other_car.collided = True
