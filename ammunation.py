from turtle import Turtle

BOMBS = 10


class Ammo(Turtle):

    def __init__(self, ship):
        """Initializes the repel bombs which can and the count of ammunition"""
        super().__init__()
        self.loc = ship
        self.bombs = BOMBS
        self.ammo = Turtle('circle')
        self.ammo.penup()
        self.ammo.goto(-3300, 3000)
        self.ammo.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.ammo.color('yellow2')
        self.ammo_score()

    def bomb(self):
        """The function that places the bomb based on the location of the mid-compartment of the ship"""
        if self.bombs > 0:
            new_x = self.loc.all_list[1].xcor()
            new_y = self.loc.all_list[1].ycor()
            self.ammo.goto(new_x, new_y)
            self.bombs -= 1
            self.ammo_score()
        else:
            pass

    def ammo_score(self):
        """Initializes the turtle for the ammunition scorecard"""
        self.clear()
        self.penup()
        self.color('PaleGreen2')
        self.goto(0, 245)
        self.hideturtle()
        self.write(f'Ammo: {self.bombs}', align='center',
                   font=("Tahoma", 14, "bold"))
