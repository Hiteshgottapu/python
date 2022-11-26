from turtle import *
hideturtle()
fillcolor('red')

begin_fill()
for i in [300 , 200]* 2:
    forward(i)
    circle(30,90)
end_fill()
penup()
goto(120 , 80)
pendown()
fillcolor('white')
begin_fill()
for i in [30 , 120 , 120]:
    left(i)
    forward(100)
end_fill()
done()