import sys
from typing import Dict, List


TOTAL_DISK_SPACE = 70000000
SPACE_REQUIRED = 30000000


class Dir:
    def __init__(self, name: str):
        self.name: str = name
        self.files: Dict[str, int] = {}
        self.dirs: List[Dir] = []

    def __str__(self):
        return f"Dir: {self.name}"

    def _get_dir_names(self) -> List[str]:
        return [d.name for d in self.dirs]

    def add_file(self, name: str, size: int):
        self.files[name] = size

    def add_dir(self, name: str):
        if name not in self._get_dir_names():
            self.dirs.append(Dir(name))

    def get_dir(self, name: str):
        for d in self.dirs:
            if d.name == name:
                return d

    def get_size(self) -> int:
        return sum(self.files.values()) + sum(d.get_size() for d in self.dirs)


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    f.readline()  # It would be cruel to not give us root dir as the first command, right?
    root = Dir('/')
    pwd = ['/']
    line = f.readline().strip()
    while line:
        # Determine the command
        if line[2:4] == 'cd':
            if line[5:] == '/':
                pwd = ['/']
            elif line[5:] == '..':
                pwd.pop()
            else:
                pwd.append(line[5:])
            line = f.readline().strip()
        else:
            # Assert: line[2:4] == 'ls'
            line = f.readline().strip()
            current_dir = root
            if len(pwd) > 1:
                for d in pwd[1:]:
                    current_dir = current_dir.get_dir(d)
            while line and not line[0] == '$':
                if line[0] == 'd':
                    current_dir.add_dir(line[4:])
                else:
                    file_size, file_name = line.split(' ')
                    current_dir.add_file(file_name, int(file_size))
                line = f.readline().strip()
    smallest_deletable = root.get_size()
    maybe_smallest = smallest_deletable
    dirs_to_search: List[Dir] = []
    free_space = TOTAL_DISK_SPACE - smallest_deletable
    # Probably safe to assume root is not the solution...
    for d in root.dirs:
        maybe_smallest = d.get_size()
        if maybe_smallest + free_space >= SPACE_REQUIRED:
            dirs_to_search.append(d)
            if maybe_smallest < smallest_deletable:
                smallest_deletable = maybe_smallest
    while dirs_to_search:
        for d in dirs_to_search.pop().dirs:
            maybe_smallest = d.get_size()
            if maybe_smallest + free_space >= SPACE_REQUIRED:
                dirs_to_search.append(d)
                if maybe_smallest < smallest_deletable:
                    smallest_deletable = maybe_smallest
    print(smallest_deletable)
