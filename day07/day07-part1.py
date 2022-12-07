import sys
from typing import Dict, List


class Dir:
    def __init__(self, name: str):
        self.name: str = name
        self.files: Dict[str, int] = {}
        self.dirs: List[Dir] = []

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
    total_sizes_under_100000 = 0
    dirs_to_search = [root]
    while dirs_to_search:
        current_dir = dirs_to_search.pop()
        dirs_to_search.extend(current_dir.dirs)
        current_size = current_dir.get_size()
        if current_size <= 100000:
            total_sizes_under_100000 += current_size
    print(total_sizes_under_100000)
