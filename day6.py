from collections import defaultdict


with open('day6_input.txt') as f:
    content = f.readlines()

class SolutionPart1():

    def run(self, s):
        positions = set()
        for line in s:
            line.split()
            x, y = line.split(", ")
            positions.add((int(x), int(y)))

        left, top, right, bot = self.grid(positions)

        infinite = set()
        grid = dict()
        data = defaultdict(int)

        for i in range(left, right + 1):
            grid[i] = dict()
            for j in range(top, bot + 1):
                grid[i][j] = self.closest_pos(i, j, positions)

                if grid[i][j] is not None:
                    data[grid[i][j]] += 1

                if (i == left or i == right or j == top or j == bot) and grid[i][j] is not None:
                    infinite.add(grid[i][j])

        return max(val for key, val in data.items() if key not in infinite)

    def grid(self, positions):
        left = min(x for (x, _) in positions)
        top = min(y for (_, y) in positions)
        right = max(x for (x, _) in positions)
        bot = max(y for (_, y) in positions)

        return left, top, right, bot

    def closest_pos(self, i, j, positions):
        dist = dict()

        for pos in positions:
            dist[pos] = abs(pos[0] - i) + abs(pos[1] - j)

        result = set(pos for pos in positions if dist[pos] == min(dist.values()))

        if len(result) > 1:
            return None
        return list(result)[0]


class SolutionPart2():

    def run(self, s):
        positions = set()
        for line in s:
            x, y = line.split(", ")
            positions.add((int(x), int(y)))

        left, top, right, bot = self.grid(positions)

        result = 0

        for i in range(left, right + 1):
            for j in range(top, bot + 1):
                if self.sum_dist(i, j, positions) < 10000:
                    result += 1

        return result

    def grid(self, positions):
        left = min(x for (x, _) in positions)
        top = min(y for (_, y) in positions)
        right = max(x for (x, _) in positions)
        bot = max(y for (_, y) in positions)

        return left, top, right, bot

    def sum_dist(self, i, j, positions):
        dist = 0

        for pos in positions:
            dist += abs(pos[0] - i) + abs(pos[1] - j)

        return dist

