from .field import Field
from .car import Car
from .simulation import Simulation


def get_field_dimensions():
    while True:
        try:
            user_input = input("Please enter the width and height of the simulation field in x y format: ")
            width, height = map(int, user_input.split())
            if width > 0 and height > 0:
                return width, height
            else:
                print("Width and height must be positive integers. Try again.")
        except ValueError:
            print("Invalid input. Please enter two space-separated integers (e.g., '10 10').")

def main():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = get_field_dimensions()
    print(f"You have created a field of {width} x {height}.")
    field = Field(width, height)
    simulation = Simulation(field)

    while True:
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Please enter the name of the car: ")
            x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
            x, y = int(x), int(y)
            commands = input(f"Please enter the commands for car {name}: ")
            simulation.add_car(Car(name, x, y, direction, commands))
        elif choice == "2":
            simulation.run()
            print("\nAfter simulation, the result is:")
            for car in simulation.cars:
                if car.collided:
                    print(f"- {car.name}, collided at ({car.x},{car.y})")
                else:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
            break

if __name__ == "__main__":
    main()
