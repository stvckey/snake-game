from turtle import Turtle
with open("data.txt") as file:
    high_score = int(file.read())



class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-220,y=250)
        self.color("white")
        self.score = 0
        self.high_score = high_score
        self.write(f"Score: {self.score} High Score: {self.high_score} ", font=('Courier', 25, 'bold'))
        self.hideturtle()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
        self.goto(-1000,1000)
        self.write("GAME OVER", font=('Courier', 25, 'bold'))
        self.goto(x=-220,y=250)
    
    def get_point(self):
        self.score += 1
        self.update_scoreboard()
                
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=('Courier', 25, 'bold'))
    
