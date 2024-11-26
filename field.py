class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupied_positions = {}  # Tracks car positions: {car_name: (x, y)}

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_occupied(self, x, y):
        return any(pos == (x, y) for pos in self.occupied_positions.values())

    def update_position(self, car_name, x, y):
        self.occupied_positions[car_name] = (x, y)
