import turtle as t
t.speed(222)
t.bgcolor('black')

for i in range(180):
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
    if i%2==0:
        if i >=120 :
            t.pencolor('yellow')
        
        else:
            t.pencolor('blue')

    else:
        if i >=120 :
            t.pencolor('red')
        else:
            t.pencolor('green')

t.down()