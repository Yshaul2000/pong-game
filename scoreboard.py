from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()
       
    def update_scoreboard(self):
        """ Update the score each time ."""
        self.clear()
         # Top right_center position of the screen .
        self.goto(100 , 200)
        self.write(self.right_score , align = "center" , font = ("Courier" , 80 , "normal"))

        # Top left_center position of the screen .
        self.goto(-100 , 200)
        self.write(self.left_score , align = "center" , font = ("Courier" , 80 , "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()