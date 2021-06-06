import turtle

from ball import Ball 
# from peddle import Peddle 



wn=turtle.Screen()
wn.title("Pong by @_iitsjana")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



ball1=Ball(0.2,-0.2,"white", "circle")
ball1.drawBall()
ball1.drawPen()
ball1.stuff_a()
ball1.stuff_b()
ball1.peddle_a_up()
ball1.peddle_a_down()
ball1.peddle_b_up()
ball1.peddle_b_down()


wn.listen()
wn.onkeypress(ball1.peddle_a_up,"w")
wn.onkeypress(ball1.peddle_a_down,"s")
wn.onkeypress(ball1.peddle_b_up,"Up")
wn.onkeypress(ball1.peddle_b_down,"Down")

while True:
    
    wn.update() 
    ball1.moveBall()
    ball1.movePeddle()

