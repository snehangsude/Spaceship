from turtle import Turtle

"""Opens a file if it's present else it would create and read the file and save it on the variable - CONTENT"""
try:
    with open("score.txt") as file:
        CONTENT = file.read()
except FileNotFoundError:
    with open('score.txt', mode='w+') as file:
        file.write('0')
        CONTENT = file.read()


class Score(Turtle):
    """Initializes the scorecard"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('PeachPuff2')
        self.goto(0, 270)
        self.score = 0
        self.high_score = int(CONTENT)
        self.update_score()

    def increase_score(self):
        """Increases the score of the score card and updates it"""
        self.score += 1
        self.update_score()

    def update_score(self):
        """Function responsible for clearing the old score and updating with the current score"""
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align='center',
                   font=("Tahoma", 14, "bold"))

    def memorize(self):
        """Function to register the high score and save it on the file"""
        with open('score.txt', mode='w') as file_m:
            file_m.write(str(self.score))

    def reset_score(self):
        """Resets the score to zero and registers the high score if it was higher than the previous high score"""
        if self.score > self.high_score:
            self.memorize()
        self.score = 0
        self.update_score()
