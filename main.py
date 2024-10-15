import pygame
from pygame.constants import QUIT

#         If the ant is on a white cell:
#             Turn 90 degrees to the right (clockwise).
#             Flip the color of the cell to black.
#             Move forward one cell.
#         If the ant is on a black cell:
#             Turn 90 degrees to the left (counterclockwise).
#             Flip the color of the cell to white.
#             Move forward one cell.
#
# The process repeats for each step of the ant’s movement, and over time, interesting patterns emerge.


class Ant:
    def __init__(self, x, y, upper_bound, cell_size, direction=0) -> None:
        self.x = x
        self.y = y
        self.upper_bound = upper_bound
        self.cell_size = cell_size
        self.direction = direction
        self.directions = ["up", "right", "down", "left"]

    def move_forward(self):
        if self.direction == 0:
            self.move_up()
        elif self.direction == 1:
            self.move_right()
        elif self.direction == 2:
            self.move_down()
        elif self.direction == 3:
            self.move_left()

    def turn_right(self):
        self.direction = (self.direction + 1) % len(self.directions)

    def turn_left(self):
        self.direction = (self.direction - 1) % len(self.directions)

    def move_up(self):
        if self.y == 0:
            self.y = self.upper_bound
        else:
            self.y = self.y - self.cell_size

    def move_down(self):
        if self.y == self.upper_bound:
            self.y = 0
        else:
            self.y = self.y + self.cell_size

    def move_left(self):
        if self.x == 0:
            self.x = self.upper_bound
        else:
            self.x = self.x - self.cell_size

    def move_right(self):
        if self.x == self.upper_bound:
            self.x = 0
        else:
            self.x = self.x + self.cell_size


pygame.init()


# Initialize a grid of white cells (0)
# Place the ant in the center of the grid
# Set the initial direction of the ant (e.g., up)
#
# While running:
#     If the ant is on a white cell:
#         Turn the ant right
#         Flip the cell to black (1)
#     Else if the ant is on a black cell:
#         Turn the ant left
#         Flip the cell to white (0)
#
#     Move the ant forward one cell
#     Display the grid (optional for visualization)
#


def main():
    WHITE = "white"
    BLACK = "black"
    WIDTH = 1200
    HEIGHT = 1200
    CELL_SIZE = 5
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    running = True

    SCREEN.fill("black")

    GRID = {}
    grid_list = []
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            grid_list.append((x, y))

    for item in grid_list:
        GRID[item] = WHITE

    # print(GRID)

    middle_x = (WIDTH // CELL_SIZE) // 2 * CELL_SIZE
    middle_y = (HEIGHT // CELL_SIZE) // 2 * CELL_SIZE

    ant = Ant(middle_x, middle_y, WIDTH - CELL_SIZE, CELL_SIZE)

    def move_ant():
        is_white = GRID[(ant.x, ant.y)] == WHITE
        # ant.move_right()
        if is_white:
            GRID[(ant.x, ant.y)] = BLACK
            ant.turn_right()
        else:
            GRID[(ant.x, ant.y)] = WHITE
            ant.turn_left()

        ant.move_forward()

    def draw_grid():
        for cell in GRID:
            rect = pygame.Rect(cell[0], cell[1], CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(SCREEN, GRID[(cell[0], cell[1])], rect)

    while running:
        draw_grid()
        move_ant()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
