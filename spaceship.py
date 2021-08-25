from turtle import Turtle

COLOR = ["grey40", "grey50", "grey60"]
DIST = 20


class Ship:

    def __init__(self):
        """Initializes a list to store the compartment of ships"""
        self.all_list = []
        self.num = 1

    def block_ship(self):
        """Generate the ship and it's location and appends it to the initialization list"""
        for i in range(3):
            ship = Turtle('square')
            ship.color(COLOR[i])
            ship.penup()
            ship.goto(0, -300)
            new_y = ship.ycor() + (20 * self.num)
            ship.goto(0, new_y)
            ship.turtlesize(stretch_wid=1, stretch_len=(4 - self.num))
            self.num += 1
            self.all_list.append(ship)

    def create_ship(self):
        """Create the ship in the bottom of the screen - on the y-axis"""
        self.num = 1
        self.block_ship()

    def move_right(self):
        """Function to move the ship right on the x-axis"""
        if self.all_list[2].xcor() < 205:
            for seg in self.all_list:
                seg.forward(DIST)

    def move_left(self):
        """Function to move the ship left on the x-axis"""
        if self.all_list[0].xcor() > -220:
            for seg in self.all_list:
                seg.backward(DIST)

    def move_up(self):
        """Function to move the ship upwards on the y-axis"""
        if self.all_list[2].ycor() < -100:
            for seg in range(len(self.all_list)):
                if seg == 2:
                    new_xcor = self.all_list[seg].xcor()
                    new_ycor = self.all_list[seg].ycor()
                    self.all_list[seg].goto(new_xcor, new_ycor + DIST)
                else:
                    new_x = self.all_list[seg + 1].xcor()
                    new_y = self.all_list[seg + 1].ycor()
                    self.all_list[seg].goto(new_x, new_y)

    def move_down(self):
        """Function to move the ship downwards on the y-axis"""
        if self.all_list[0].ycor() >= -260:
            for seg in range(len(self.all_list) - 1, -1, -1):
                if seg == 0:
                    new_xcor = self.all_list[seg].xcor()
                    new_ycor = self.all_list[seg].ycor()
                    self.all_list[seg].goto(new_xcor, new_ycor - DIST)
                else:
                    new_x = self.all_list[seg - 1].xcor()
                    new_y = self.all_list[seg - 1].ycor()
                    self.all_list[seg].goto(new_x, new_y)

    def ship_reset(self):
        """Resets the position of the ship and sets it to the starting position"""
        for i in self.all_list:
            i.goto(-50000, 50000)
        self.all_list.clear()
        self.create_ship()


