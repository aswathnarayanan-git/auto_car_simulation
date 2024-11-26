class Simulation:
    def __init__(self, field):
        self.field = field
        self.cars = []

    def add_car(self, car):
        # Check if a car with the same name already exists
        if any(existing_car.name == car.name for existing_car in self.cars):
            raise ValueError(f"Car with name {car.name} already exists.")
        self.cars.append(car)

    def run(self):
        for car in self.cars:
            for command in car.commands:
                if command == "F":
                    car.move_forward(self.field)
                elif command == "L":
                    car.rotate_left()
                elif command == "R":
                    car.rotate_right()

                # Check for collisions after each move
                for other_car in self.cars:
                    if car != other_car:
                        car.check_collision(other_car)
