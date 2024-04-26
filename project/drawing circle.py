#author: Ken Vu
#Date: Marc. 6,2024
#purpose: Drawing a ring of 36 alternating colou circles
import turtle
colors=["red","pink","blue"]

anna = turtle.Turtle()

anna.speed(0)

anna.goto(0 ,0)

time =0
#drawing 
while time < 36:
 anna.penup()
 anna.forward(100)
 anna.pendown()
 anna.pencolor(colors[time%3])
 anna.fillcolor(colors[time%3])
 anna.begin_fill()
 anna.circle(10)
 anna.end_fill()
 anna.penup()
 anna.goto(0,0)
 anna.right(10)
 time +=1
anna.done()
anna.bye()
