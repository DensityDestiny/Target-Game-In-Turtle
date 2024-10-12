import turtle
import random

targets = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]


def goto(randomx, randomy):
  t.penup()
  randomx = -175 + (50 * randomx)
  randomy = -175 + (50 * randomy)
  t.goto(randomx, randomy)
  t.pendown()

  
def draw_square():
   randomx = random.randint(0,7)
   randomy = random.randint(0,7)
   goto(randomx, randomy)
   for i in range(4):
       t.forward(50)
       t.right(90)
    

def move(x, y):
  turtle.penup()
  turtle.goto(x, y)
  if t.xcor() + 50 >= turtle.xcor() and t.xcor() <= turtle.xcor():
    if t.ycor() - 50 <= turtle.ycor() and t.ycor() >= turtle.ycor():
      for i in range(8):
        t.undo()
      draw_square()
      list.append(1)
      scores(len(list))


def scores(list):
  list = list + 1
  print("Score: " + str(list - 1))


global score
score = 0

list = []
turtle.setup(500,500)
t = turtle.Turtle()
t.speed(0)
draw_square()
window = turtle.Screen()
window.listen()
window.onclick(move)
