import time
import os
class Wall:
    def __init__(self, dimensions, wall_coords):
        self.room = [ [" " for i in range(dimensions[1])] for j in range(dimensions[0]) ]
        self.dimensions = dimensions
        try:
            for wall_coord in wall_coords:
                start = wall_coord[0]
                end = wall_coord[1]
                if start[0] == end[0]:
                    for k in range(start[1], end[1]):
                        self.room[start[0]][k] = "*"
                else:
                    for l in range(start[0], end[0]):
                        self.room[l][start[1]] = "*"
        except IndexError:
            print(wall_coord)


    def print_board(self):
        for i in range(self.dimensions[0]):
            print("".join(self.room[i]))
        for i in range(0,0):
            print("hello")



class Robot:
    def __init__(self):
        self.direction = 'n'
        self.start = [23,50]
        self.position = [*self.start]
        self.dirConvention = ['n', 'e', 's', 'w']

    def turn_left(self):
        self.direction = self.dirConvention[self.dirConvention.index(self.direction) - 1]

    def turn_right(self):
        self.direction = self.dirConvention[(self.dirConvention.index(self.direction) + 1) % 4]

    def move_straight(self):
        wall.room[self.position[0]][self.position[1]] = " "
        if self.direction == 'n':
            self.position[0] -= 1
        elif self.direction == 's':
            self.position[0] += 1
        elif self.direction == 'e':
            self.position[1] += 1
        elif self.direction == 'w':
            self.position[1] -= 1

    def place_robot(self, wall):
        wall.room[self.position[0]][self.position[1]] = "@"


    def check_wall(self, wall, at):
        if wall.room[at[0]][at[1]] == "*":
            return True
        return False

    def wall_left(self, wall):
        left_dir = self.dirConvention[self.dirConvention.index(self.direction) - 1]
        future_pos = []
        if left_dir == 'w':
            future_pos += [ self.position[0], self.position[1] -1 ]
        elif left_dir == 'n':
            future_pos += [ self.position[0] - 1, self.position[1]  ]
        elif left_dir == 'e':
            future_pos += [self.position[0], self.position[1] + 1 ]
        elif left_dir == 's':
            future_pos += [self.position[0] + 1, self.position[1] ]
        return self.check_wall(wall, future_pos)

    def wall_right(self, wall):
        right_dir = self.dirConvention[(self.dirConvention.index(self.direction) + 1) % 4]
        if right_dir == 'w':
            future_pos = [ self.position[0], self.position[1] -1 ]
        elif right_dir == 'n':
            future_pos = [ self.position[0] - 1, self.position[1]  ]
        elif right_dir == 'e':
            future_pos = [ self.position[0], self.position[1] + 1 ]
        elif right_dir == 's':
            future_pos = [ self.position[0] + 1, self.position[1] ]
        return self.check_wall(wall,future_pos)

    def wall_straight(self, wall):
        str_dir = self.direction
        if str_dir == 'w':
            future_pos = [ self.position[0], self.position[1] -1 ]
        elif str_dir == 'n':
            future_pos = [ self.position[0] - 1, self.position[1]  ]
        elif str_dir == 'e':
            future_pos = [ self.position[0], self.position[1] + 1 ]
        elif str_dir == 's':
            future_pos = [ self.position[0] + 1, self.position[1] ]
        return self.check_wall(wall,future_pos)

    def wall_back(self, wall):
        str_dir = self.dirConvention[self.dirConvention.index(self.direction) - 2]
        if str_dir == 'w':
            future_pos = [ self.position[0], self.position[1] -1 ]
        elif str_dir == 'n':
            future_pos = [ self.position[0] - 1, self.position[1]  ]
        elif str_dir == 'e':
            future_pos = [ self.position[0], self.position[1] + 1 ]
        elif str_dir == 's':
            future_pos = [ self.position[0] + 1, self.position[1] ]
        return self.check_wall(wall,future_pos)

    def make_move(self, wall):
        if not self.wall_left(wall) and not self.wall_right(wall) and not self.wall_straight(wall) and self.wall_back(wall):
            self.turn_left()
        elif self.wall_left(wall) and not self.wall_right(wall) and not self.wall_straight(wall):
            self.move_straight()
        elif not self.wall_left(wall) and self.wall_right(wall) and not self.wall_straight(wall):
            self.move_straight()
        elif not self.wall_left(wall) and self.wall_right(wall) and self.wall_straight(wall):
            self.turn_left()
        elif self.wall_left(wall) and not self.wall_right(wall) and  self.wall_straight(wall):
            self.turn_right()
        # elif self.wall_left(wall) and self.wall_right(wall) and not self.wall_straight(wall):
        elif self.wall_left(wall) and self.wall_right(wall) and not self.wall_straight(wall):
            self.move_straight()
        else:
            self.turn_left()
            self.move_straight()

    def print_status(self):
        print(self.direction, self.position)


wall = Wall((25, 100), [
        [(0,0),(0,100)],
        [(0,50), (20,50)],
        [(0, 99), (25, 99)],
        [(24, 0), (24, 100)],
        [(0, 0), (25, 0)],
        [(20, 25), (20, 50)],
        [(5, 25), (20, 25)],
        [(5, 25), (5, 70)],
])
# wall.print_board()
robot = Robot()
while True:
    robot.make_move(wall)
    robot.place_robot(wall)
    robot.print_status()
    wall.print_board()
    time.sleep(0.1)
    os.system('cls||clear')
