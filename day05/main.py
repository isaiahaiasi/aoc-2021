# determine number of points where at least 2 lines overlap
# (for now, NO DIAGONALS)
# create class for a line, which is constructed using 2 points
# and also has a slope property

# board which the lines are "rendered" to
# each point on the board is an int which record the number of lines there
# a line is rendered by incrementing each point on which it lies

# the final number is found simply by iterating over the final board,
# and listing the number of points > 1

# (and hopefully part 2 will just involve upgrading the "figure out which points the line is on" part...)

# (there might be a smart way to calculate the intersections, but I can't think of non-n^2 way...)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]

    # returns all points between p1 & p2, inclusive
    def get_points(self):
        x_dir = self.x_dir()
        y_dir = self.y_dir()
        if (self.y_delta() == 0):
            x_range = range(0, (self.x_delta()) * x_dir + x_dir, x_dir)
            return [(self.x1 + i, self.y1) for i in x_range]
        elif (self.x_delta() == 0):
            y_range = range(0, (self.y_delta()) * y_dir + y_dir, y_dir)
            return [(self.x1, self.y1 + i) for i in y_range]
        else:
            x_range = range(0, (self.x_delta()) * x_dir + x_dir, x_dir)
            y_range = range(0, (self.y_delta()) * y_dir + y_dir, y_dir)
            xs = [self.x1 + i for i in x_range]
            ys = [(self.y1 + i) for i in y_range]
            return zip(xs, ys)

    def x_delta(self):
        return abs(self.x2 - self.x1)

    def y_delta(self):
        return abs(self.y2 - self.y1)

    def x_dir(self):
        return 1 if self.x2 - self.x1 >= 0 else -1

    def y_dir(self):
        return 1 if self.y2 - self.y1 >= 0 else -1

    def __str__(self):
        # eg, "0,9 -> 5,9"
        return f"{self.p1[0]},{self.p1[1]} -> {self.p2[0]},{self.p2[1]}"


class Board:
    def __init__(self):
        self.board = {}
        self.width = 0
        self.height = 0

    def add_point(self, point):
        if point in self.board:
            self.board[point] = self.board[point] + 1
        else:
            self.board[point] = 1
        x, y = point
        if x + 1 > self.width:
            self.width = x + 1
        if y + 1 > self.height:
            self.height = y + 1

    def get_overlap_count(self):
        count = 0
        for k, v in self.board.items():
            if v > 1:
                count = count + 1
        return count

    def render_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.board:
                    print(self.board[(x, y)], end='')
                else:
                    print('.', end='')
            print()


def get_input(path):
    with open(path) as fp:
        lines = []
        for line in fp:
            p1, p2 = get_point_from_str(line)
            lines.append(Line(p1, p2))
    return lines


def get_point_from_str(str):
    return [[int(i) for i in p.strip().split(',')] for p in str.split('->')]


def print_lines(lines):
    [print(line) for line in lines]


if __name__ == "__main__":
    lines = get_input('input.txt')

    board = Board()

    for line in lines:
        for point in line.get_points():
            board.add_point(point)
    # board.render_board()
    print(board.get_overlap_count())
