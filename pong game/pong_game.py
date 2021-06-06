
import turtle  



wn=turtle.Screen()
wn.title("Pong by @_iitsjana")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score

score_a=0
score_b=0
#a
peddle_a=turtle.Turtle()
peddle_a.speed(0)
peddle_a.shape("square")
peddle_a.color("white")
peddle_a.shapesize(stretch_wid=5, stretch_len=1)
peddle_a.penup()
peddle_a.goto(-350,0)

#b
peddle_b=turtle.Turtle()
peddle_b.speed(0)
peddle_b.shape("square")
peddle_b.color("white")
peddle_b.shapesize(stretch_wid=5, stretch_len=1)
peddle_b.penup()
peddle_b.goto(350,0)


#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx= 0.2
ball.dy= -0.2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  PlayerB:0", align="center", font=("Courier",24,"normal"))



#moving peddles

def peddle_a_up():
    y=peddle_a.ycor()
    y+=20
    peddle_a.sety(y)

def peddle_a_down():
    y=peddle_a.ycor()
    y-=20
    peddle_a.sety(y)

def peddle_b_up():
    y=peddle_b.ycor()
    y+=20
    peddle_b.sety(y)

def peddle_b_down():
    y=peddle_b.ycor()
    y-=20
    peddle_b.sety(y)

wn.listen()
wn.onkeypress(peddle_a_up,"w")
wn.onkeypress(peddle_a_down,"s")
wn.onkeypress(peddle_b_up,"Up")
wn.onkeypress(peddle_b_down,"Down")

#moving the ball




#main game loop

while True:
    wn.update() 

    #moving the ball

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


    #peddle collisions
    if( ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<peddle_b.ycor()+40 and ball.ycor()>peddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1  

    if( ball.xcor()<-340 and ball.xcor()<350) and (ball.ycor()<peddle_a.ycor()+40 and ball.ycor()>peddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1 

"""
wn=turtle.Screen()
wn.title("Pong by @_iitsjana")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

class Pong:
    def __init__(self, speed, shape, color):
        self.speed=speed
        self.shape=shape
        self.color=color
 

    def draw_a(self):
        a=turtle.Turtle()
        a.speed(0)
        a.shape("square")
        a.color("white")
  

    def draw_b(self):
        b=turtle.Turtle()
        b.speed(0)
        b.shape("square")
        b.color("white")
         

        while True:
            wn.update() 
    
r1=Pong(0,"square","white")

"""





