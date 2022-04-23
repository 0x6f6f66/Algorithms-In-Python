from turtle import *

speed(100)
color('cyan')
bgcolor('black')
b = 210

while b > 0:
    left(b)
    forward(b * 3)
    b -= 1
    if b < 10:
       b = 200

Screen().exitonclick()