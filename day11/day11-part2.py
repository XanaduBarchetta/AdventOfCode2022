import queue
import re
import sys
from typing import List

STARTING_RE = re.compile(r'\d+')
NUM_ROUNDS = 10000


class MonkeyItem:
    def __init__(self, value):
        self.value = value
        self.values = {}

    def init_values(self, values):
        for value in values:
            self.values[value] = self.value

    def add(self, value) -> None:
        for mod, old_val in self.values.items():
            self.values[mod] = (old_val + value) % mod

    def multiply(self, value) -> None:
        for mod, old_val in self.values.items():
            self.values[mod] = (old_val * value) % mod

    def square(self) -> None:
        for mod, old_val in self.values.items():
            self.values[mod] = (old_val * old_val) % mod

    def is_divisible_by(self, divisor) -> bool:
        if self.values[divisor] == 0:
            return True
        return False


class Monkey:
    def __init__(self, starting_items, operation, operation_value, test_num, true_monkey, false_monkey):
        self.items = queue.Queue()
        for item in starting_items:
            self.items.put(MonkeyItem(item))
        self.operation = operation
        self.operation_value = operation_value
        self.test_num = test_num
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def check_item(self) -> (MonkeyItem, int):
        self.inspections += 1
        item: MonkeyItem = self.items.get()
        if self.operation == 'addition':
            item.add(self.operation_value)
        elif self.operation == 'multiplication':
            item.multiply(self.operation_value)
        elif self.operation == 'squared':
            item.square()
        if item.is_divisible_by(self.test_num):
            return item, self.true_monkey
        return item, self.false_monkey


def main(f):
    # Build the monkey list
    monkeys: List[Monkey] = []
    line = f.readline()  # Monkey index line
    while line:
        starting_items = [int(item) for item in STARTING_RE.findall(f.readline().strip())]
        operation_data = f.readline().split(' ')[-2:]
        operation = 'squared'
        operation_value = None
        if operation_data[1] != 'old\n':
            operation = 'multiplication' if operation_data[0] == '*' else 'addition'
            operation_value = int(operation_data[1])
        test_num = int(f.readline().split(' ')[-1])
        true_monkey = int(f.readline().split(' ')[-1])
        false_monkey = int(f.readline().split(' ')[-1])
        monkeys.append(Monkey(
            starting_items=starting_items,
            operation=operation,
            operation_value=operation_value,
            test_num=test_num,
            true_monkey=true_monkey,
            false_monkey=false_monkey
        ))
        f.readline()  # Empty line or EOF
        line = f.readline()  # Monkey index line or EOF
    mods = [monkey.test_num for monkey in monkeys]
    for monkey in monkeys:
        for item in list(monkey.items.queue):
            item.init_values(mods)

    # Run the simulation
    for r in range(NUM_ROUNDS):
        for monkey_num, monkey in enumerate(monkeys):
            while not monkey.items.empty():
                item, to_monkey = monkey.check_item()
                monkeys[to_monkey].items.put(item)
    top_two = sorted(m.inspections for m in monkeys)[-2:]
    print(top_two[0] * top_two[1])


if __name__ == "__main__":
    # First parameter to program is the input file
    with open(sys.argv[1]) as file:
        main(file)
