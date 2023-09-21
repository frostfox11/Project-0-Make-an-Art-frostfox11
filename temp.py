import turtle as t

t.goto(-50, 0)
t.bgcolor("black")
t.color("yellow")
t.speed(100)

t.begin_fill()
points = 1
while points < 5:
  t.forward(250)
  t.left(145)
  points += 1
t.end_fill()
