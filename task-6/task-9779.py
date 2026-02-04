from turtle import *

tracer(False)

m = 20


for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(-10, 23):
    for y in range(-10,10):
        goto(x * m,y * m)
        dot(8, 'white')


update()
done()
