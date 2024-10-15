import unittest
from main import Ant


CELL_SIZE = 20


class AntTestCase(unittest.TestCase):
    def test_ant_initialization(self):
        ant = Ant(11, 34, 99, CELL_SIZE)
        self.assertIs(ant.x, 11)
        self.assertIs(ant.y, 34)

    def test_move_forward_when_up(self):
        ant = Ant(0, 20, 100, CELL_SIZE)
        ant.move_forward()
        self.assertIs(ant.x, 0)
        self.assertIs(ant.y, 0)

    def test_move_forward_when_up_and_y_is_zero(self):
        ant = Ant(0, 0, 100, CELL_SIZE)
        ant.move_forward()
        self.assertIs(ant.x, 0)
        self.assertIs(ant.y, 100)

    def test_move_forward_when_right(self):
        ant = Ant(0, 0, 100, CELL_SIZE)
        ant.turn_right()
        ant.move_forward()
        self.assertIs(ant.x, 20)
        self.assertIs(ant.y, 0)

    def test_move_forward_when_right_and_x_is_on_last_cell(self):
        ant = Ant(100, 0, 100, CELL_SIZE)
        ant.turn_right()
        self.assertIs(ant.direction, 1)
        ant.move_forward()
        self.assertIs(ant.x, 0)
        self.assertIs(ant.y, 0)

    def test_move_forward_when_down(self):
        ant = Ant(20, 40, 100, CELL_SIZE)
        ant.turn_right()
        self.assertIs(ant.direction, 1)
        ant.turn_right()
        self.assertIs(ant.direction, 2)
        ant.move_forward()
        self.assertIs(ant.x, 20)
        self.assertIs(ant.y, 60)

    def test_move_forward_when_down_and_is_on_last_row(self):
        ant = Ant(20, 100, 100, CELL_SIZE)
        ant.turn_right()
        self.assertIs(ant.direction, 1)
        ant.turn_right()
        self.assertIs(ant.direction, 2)
        ant.move_forward()
        self.assertIs(ant.x, 20)
        self.assertIs(ant.y, 0)

    # def test_move_up_when_y_is_between_zero_and_upper_bound(self):
    #     ant = Ant(0, 40, 80, CELL_SIZE)
    #     ant.move_up()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 20)
    #
    # def test_move_up_when_y_is_zero(self):
    #     ant = Ant(0, 0, 80, CELL_SIZE)
    #     ant.move_up()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 80)
    #
    #
    # def test_move_down_when_y_is_between_zero_and_upper_bound(self):
    #     ant = Ant(0, 20, 100, CELL_SIZE)
    #     ant.move_down()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 40)
    #
    # def test_move_down_when_y_is_upper_bound(self):
    #     ant = Ant(0, 9, 9, CELL_SIZE)
    #     ant.move_down()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 0)
    #
    # def test_move_left_when_x_is_between_zero_and_upper_bound(self):
    #     ant = Ant(20, 80, 100, CELL_SIZE)
    #     ant.move_left()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 80)
    #
    # def test_move_left_when_x_is_zero(self):
    #     ant = Ant(0, 8, 100, CELL_SIZE)
    #     ant.move_left()
    #     self.assertIs(ant.x, 100)
    #     self.assertIs(ant.y, 8)
    #
    # def test_move_right_when_x_is_between_zero_and_upper_bound(self):
    #     ant = Ant(20, 40, 100, CELL_SIZE)
    #     ant.move_right()
    #     self.assertIs(ant.x, 40)
    #     self.assertIs(ant.y, 40)
    #
    # def test_move_right_when_x_is_upper_bound(self):
    #     ant = Ant(9, 8, 9, CELL_SIZE)
    #     ant.move_right()
    #     self.assertIs(ant.x, 0)
    #     self.assertIs(ant.y, 8)
