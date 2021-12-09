# I'm tired
# so so tired today
# so we're gonna try brute force

def load_input(path):
    with open(path) as fp:
        return fp.read().split('\n')


class BasinNav:
    def __init__(self, input) -> None:
        self.visited = {}
        self.input = input
        self.height = len(input)
        self.width = len(input[0])
        self.mins = self.get_mins()

    # lower than all *cardinally* adjacent points
    def get_mins(self):
        mins = []

        for y in range(self.height):
            for x in range(self.width):
                if self.is_min(x, y):
                    mins.append((x, y))
        return mins

    def get_min_risk_sum(self):
        return sum([int(self.input[y][x]) + 1 for (x, y) in self.mins])

    def get_basins(self):
        basins = []

        for x, y in self.mins:
            basins.append(self.get_all_adjacents(x, y))
            self.visited = {}
        return basins

    def get_all_adjacents(self, x, y):
        adj = [(x, y)]
        self.visited[(x, y)] = True
        for ax, ay in self.get_adjacent(x, y):
            if self.input[ay][ax] < '9' and (ax, ay) not in self.visited:
                adj.extend(self.get_all_adjacents(ax, ay))
        return adj

    def get_basin_result(self):
        basins = self.get_basins()
        top_basins = sorted(basins, key=len)[len(basins) - 3:]
        print([len(b) for b in basins])
        product = 1
        for basin in top_basins:
            render_board(self.input, basin)
            product = product * len(basin)
        return product

    def get_adjacent(self, x, y):
        adj = []
        if y - 1 >= 0:
            adj.append((x, y - 1))
        if y + 1 < self.height:
            adj.append((x, y + 1))
        if x - 1 >= 0:
            adj.append((x - 1, y))
        if x + 1 < self.width:
            adj.append((x + 1, y))
        return [pos for pos in adj if pos not in self.visited]

    def is_min(self, x, y, excluded=(None, None)):
        n = self.input[y][x]
        if n == '9':
            return False
        for ax, ay in self.get_adjacent(x, y):
            # don't count excluded positions
            if (ax, ay) == excluded:
                continue

            adj = self.input[ay][ax]
            if adj <= n:
                return False
        return True


def main():
    input = load_input('input.txt')
    basinNav = BasinNav(input)
    print(basinNav.get_basin_result())


def render_board(input, pos_list):
    rend = ''
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (x, y) in pos_list:
                rend = rend + input[y][x] + "*"
            else:
                rend = rend + input[y][x] + " "
        rend = rend + "\n"
    print(rend)


if __name__ == '__main__':
    main()

    # 399840 TOO LOW
