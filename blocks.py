from turtle import Turtle
import random

COLOR = ["MediumSeaGreen", "SteelBlue4"]


class Blocks:

    def __init__(self):
        """Initializes a list to store the blocks of blockades"""
        self.all_blocks = []

    def generate_blocks(self):
        """Generates a block on a chance of hitting '10' from a random sequence of 1-45 and appends the
        blocks to the initialized list"""
        chance = random.randint(1, 45)
        if chance == 10:
            new_x = random.randint(-230, 230)
            for i in range(2):
                block = Turtle("square")
                block.color(COLOR[i])
                block.setheading(270)
                block.penup()
                block.goto(new_x, 250)
                block.turtlesize(stretch_wid=8, stretch_len=0.5)
                self.all_blocks.append(block)
                new_x *= -1

    def block_move(self):
        """Function to move the block towards the negative y-axis"""
        self.generate_blocks()
        for seg in self.all_blocks:
            seg.forward(5)

    def block_coll(self):
        """Collapses the block if it reaches a respective y-co-ordinate to reset the length of the initialized list"""
        for i in self.all_blocks:
            if i.ycor() < -320 or i.ycor() > 320:
                self.all_blocks.remove(i)
            else:
                continue
