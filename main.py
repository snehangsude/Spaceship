from turtle import Screen
from spaceship import Ship
from blocks import Blocks
from scorecard import Score
from ammunation import Ammo
import time


def main():
    def close():
        """Close the screen/window"""
        screen.bye()

    screen = Screen()
    screen.bgcolor("grey20")
    screen.title("Spaceship")
    screen.setup(width=500, height=600)
    screen.tracer(0)

    ship = Ship()
    ship.create_ship()

    block = Blocks()

    score = Score()

    ammo = Ammo(ship)

    screen.listen()
    screen.onkey(ship.move_right, "Right")
    screen.onkey(ship.move_left, "Left")
    screen.onkey(ship.move_up, "Up")
    screen.onkey(ship.move_down, "Down")
    screen.onkey(ammo.bomb, "space")
    screen.onkey(close, 'Escape')

    while True:
        screen.update()
        time.sleep(0.1)
        block.block_move()
        block.block_coll()

        # Increase score
        if len(block.all_blocks) > 0 and block.all_blocks[0].ycor() < ship.all_list[0].ycor():
            score.increase_score()

        # Collision detection
        if len(block.all_blocks) > 0:
            for b in range(len(block.all_blocks)):
                # Collision with the Repel Bomb
                if ammo.ammo.distance(block.all_blocks[b]) < 80 and ammo.ammo.distance(ship.all_list[1]) < 40:
                    ammo.ammo.goto(-3000, 3000)
                    block.all_blocks[b].setheading(90)
                # Collision of block with the Ship
                elif (ship.all_list[2].ycor()) > (block.all_blocks[b].ycor()):
                    if abs(ship.all_list[2].xcor() - block.all_blocks[b].xcor()) <= abs(78) and abs(
                            ship.all_list[2].ycor() - block.all_blocks[b].ycor()) <= abs(10):
                        ship.ship_reset()
                        score.reset_score()


if __name__ == '__main__':
    main()
