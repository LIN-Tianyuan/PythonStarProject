class VirusSimulation:
    def __init__(self, grid):
        self.grid = grid
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # UP, RIGHT, DOWN, LEFT
        self.direction = 0     # Start facing UP
        self.position = (0, 0)  # Start position
        self.infected_count = 0

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def move_forward(self):
        x, y = self.position
        dx, dy = self.directions[self.direction]
        self.position = (x + dx, y + dy)

    def infect_or_clean(self):
        x, y = self.position
        if self.grid.get(self.position) == '#':  # If cell is infected
            self.grid[self.position] = '.'
            self.turn_right()
        else:
            self.grid[self.position] = '#'  # Infect the cell
            self.infected_count += 1
            self.turn_left()
        self.move_forward()

    def run(self, iterations):
        for _ in range(iterations):
            self.infect_or_clean()
        return self.infected_count


def parse_initial_state(initial_state_str):
    grid = {}
    rows = initial_state_str.strip().split('\n')
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell != ' ':
                grid[(x - len(row) // 2, -y)] = cell  # Center (0,0) in the middle of the grid
    return grid


initial_state_str = """
.###.#.#####.##.#...#....
..####.##.##.#..#.....#..
.#####.........#####..###
#.#..##..#.###.###.#.####
.##.##..#.###.###...#...#
#.####..#.#.##.##...##.##
..#......#...#...#.#....#
###.#.#.##.#.##.######..#
###..##....#...##....#...
###......#..#..###.#...#.
#.##..####.##..####...##.
###.#.#....######.#.###..
.#.##.##...##.#.#..#...##
######....##..##.######..
##..##.#.####.##.###.#.##
#.###.#.##....#.##..####.
#.#......##..####.###.#..
#..###.###...#..#.#.##...
#######..#.....#######..#
##..##..#..#.####..###.#.
..#......##...#..##.###.#
....##..#.#.##....#..#.#.
..#...#.##....###...###.#
#.#.#.#..##..##..#..#.##.
#.####.#......#####.####.
"""

initial_grid = parse_initial_state(initial_state_str)
simulation = VirusSimulation(initial_grid)
iterations = 10000
infected_count = simulation.run(iterations)
print(infected_count)