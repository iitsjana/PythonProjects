
import turtle 
# from peddle import Peddle


class Ball:


    def __init__(self,dx,dy,color,shape):
        self.dx=dx
        self.dy=dy
        self.color=color
        self.shape=shape

    def drawBall(self):
        global ball
        ball=turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("red")
        ball.penup()
        ball.goto(0,0)
        ball.dx= 0.2
        ball.dy= -0.2 


    def drawPen(self):
        global pen
        pen=turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("Player A:0  PlayerB:0", align="center", font=("Courier",24,"normal"))



    def moveBall(self):
        score_a=0
        score_b=0
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor()+ball.dy) 

    #borders
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy*=-1

        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy*=-1    
        if ball.xcor()>390:
            ball.goto(0,0)
            ball.dx*=-1
            score_a+=1
            pen.clear()
            pen.write("Player A:{}  PlayerB:{}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

        if ball.xcor()<-390:
            ball.goto(0,0)
            ball.dx*=-1
            score_b+=1
            pen.clear()
            pen.write("Player A:{}  PlayerB:{}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
    def stuff_a(self):
        global peddle_a
        peddle_a=turtle.Turtle()
        peddle_a.speed(0)
        peddle_a.shape("square")
        peddle_a.color("yellow")
        peddle_a.shapesize(stretch_wid=5, stretch_len=1)
        peddle_a.penup()
        peddle_a.goto(-350,0)

    def stuff_b(self):
        global peddle_b
        peddle_b=turtle.Turtle()
        peddle_b.speed(0)
        peddle_b.shape("square")
        peddle_b.color("yellow")
        peddle_b.shapesize(stretch_wid=5, stretch_len=1)
        peddle_b.penup()
        peddle_b.goto(350,0)

    def peddle_a_up(self):
        y=peddle_a.ycor()
        y+=20
        peddle_a.sety(y)

    def peddle_a_down(self):
        y=peddle_a.ycor()
        y-=20
        peddle_a.sety(y)

    def peddle_b_up(self):
        y=peddle_b.ycor()
        y+=20
        peddle_b.sety(y)

    def peddle_b_down(self):
        y=peddle_b.ycor()
        y-=20
        peddle_b.sety(y)

    def movePeddle(self):
        if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<peddle_b.ycor()+40 and ball.ycor()>peddle_b.ycor()-40):
            ball.setx(340)
            ball.dx*=-1  

        if( ball.xcor()<-340 and ball.xcor()<350) and (ball.ycor()<peddle_a.ycor()+40 and ball.ycor()>peddle_a.ycor()-40):
            ball.setx(-340)
            ball.dx*=-1 
