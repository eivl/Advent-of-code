from collections import namedtuple

with open('day7_input.txt') as f:
    result = f.read().splitlines()


class Dir(namedtuple('Dir', 'name folders files parent')):
    @property
    def size(self):
        dir_size = sum(directory.size for directory in self.folders.values())
        file_size = sum(file[0] for file in self.files)
        return dir_size+file_size

    def find(self, total_size, lt=False):
        if lt and self.size < total_size or not lt and self.size > total_size:
            yield self
        for directory in self.folders.values():
            yield from [directory for directory in directory.find(total_size, lt)]


drive = Dir(name='/', folders={}, files=[], parent=None)


current = drive
for line in result:
    match line.split():
        case['$', 'cd', '/']:
            current = drive
        case['$', 'cd', '..']:
            current = current.parent
        case['$', 'cd', folder]:
            current = current.folders[folder]
        case['dir', folder]:
            current.folders[folder] = Dir(folder, {}, [], current)
        case[num, folder] if num.isdigit():
            current.files.append((int(num), folder))

print('Part1', sum(directory.size for directory in drive.find(100_000, True)))
print('Part2', min(directory.size for
                   directory in drive.find(drive.size - 40_000_000)))
