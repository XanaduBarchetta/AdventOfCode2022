import sys

CHAMBER_WIDTH = 7
ROCK_HORIZONTAL_OFFSET = 2
ROCK_VERTICAL_OFFSET = 4
MAX_ROCKS = 2022


class Chamber:
    def __init__(self):
        self.positions = [{0} for _ in range(CHAMBER_WIDTH)]
        self.max_position = 0
        self.rock_order = [RockFlat, RockPlus, RockL, RockI, RockSquare]
        self.num_rock_types = len(self.rock_order)
        self.current_rock: Rock = RockFlat(ROCK_VERTICAL_OFFSET)
        self.next_rock_type = 1
        self.total_rocks = 0

    def move_left(self) -> None:
        collision_detected = False
        for i in range(len(self.positions) - 1):
            if self.positions[i] & self.current_rock.positions[i+1]:
                collision_detected = True
                break
        if not collision_detected:
            self.current_rock.move_left()
        self.move_down()

    def move_right(self) -> None:
        collision_detected = False
        for i in range(1, len(self.positions)):
            if self.positions[i] & self.current_rock.positions[i-1]:
                collision_detected = True
                break
        if not collision_detected:
            self.current_rock.move_right()
        self.move_down()

    def move_down(self) -> None:
        collision_detected = False
        for col, rock_col in zip(self.positions, self.current_rock.positions):
            if col & set(x - 1 for x in rock_col):
                collision_detected = True
                break
        if not collision_detected:
            self.current_rock.move_down()
            return
        self.add_next_rock()

    def add_next_rock(self) -> None:
        # Add current rock's positions to the chamber
        for col, values in enumerate(self.current_rock.positions):
            self.positions[col].update(values)
        self.max_position = max(self.max_position, max(set().union(*self.current_rock.positions)))
        # Initialize the next rock
        self.current_rock = self.rock_order[self.next_rock_type](self.max_position + ROCK_VERTICAL_OFFSET)
        self.total_rocks += 1
        self.next_rock_type = (self.next_rock_type + 1) % self.num_rock_types


class Rock:
    def __init__(self):
        self.positions = [set() for _ in range(CHAMBER_WIDTH)]

    def move_right(self) -> None:
        if not self.positions[-1]:
            for i in reversed(range(1, CHAMBER_WIDTH)):
                self.positions[i] = self.positions[i-1]
            self.positions[0] = set()

    def move_left(self) -> None:
        if not self.positions[0]:
            for i in range(CHAMBER_WIDTH - 1):
                self.positions[i] = self.positions[i+1]
            self.positions[-1] = set()

    def move_down(self) -> None:
        self.positions = [set(x - 1 for x in col) for col in self.positions]


class RockFlat(Rock):
    def __init__(self, floor: int):
        super().__init__()
        self.positions[ROCK_HORIZONTAL_OFFSET] = {floor}
        self.positions[ROCK_HORIZONTAL_OFFSET+1] = {floor}
        self.positions[ROCK_HORIZONTAL_OFFSET+2] = {floor}
        self.positions[ROCK_HORIZONTAL_OFFSET+3] = {floor}


class RockPlus(Rock):
    def __init__(self, floor):
        super().__init__()
        self.positions[ROCK_HORIZONTAL_OFFSET] = {floor + 1}
        self.positions[ROCK_HORIZONTAL_OFFSET+1] = {floor, floor + 1, floor + 2}
        self.positions[ROCK_HORIZONTAL_OFFSET+2] = {floor + 1}


class RockL(Rock):
    def __init__(self, floor):
        super().__init__()
        self.positions[ROCK_HORIZONTAL_OFFSET] = {floor}
        self.positions[ROCK_HORIZONTAL_OFFSET+1] = {floor}
        self.positions[ROCK_HORIZONTAL_OFFSET+2] = {floor, floor + 1, floor + 2}


class RockI(Rock):
    def __init__(self, floor):
        super().__init__()
        self.positions[ROCK_HORIZONTAL_OFFSET] = {floor, floor + 1, floor + 2, floor + 3}


class RockSquare(Rock):
    def __init__(self, floor):
        super().__init__()
        self.positions[ROCK_HORIZONTAL_OFFSET] = {floor, floor + 1}
        self.positions[ROCK_HORIZONTAL_OFFSET+1] = {floor, floor + 1}


def main(f):
    commands = f.readline()
    num_commands = len(commands)
    command_index = 0
    chamber = Chamber()
    while chamber.total_rocks < MAX_ROCKS:
        command = commands[command_index]
        if command == '<':
            chamber.move_left()
        else:
            chamber.move_right()
        command_index = (command_index + 1) % num_commands
    print(chamber.max_position)


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
