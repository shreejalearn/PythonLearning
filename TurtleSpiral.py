import turtle

define = turtle.Turtle()
define.speed(100)

def triangle (color, size):
  for x in ["pink"]:
    define.circle(size)
    define.color(x)
    define.forward(1)
    define.left(90)

size = 5
for x in range (200):
  triangle(define, size)
  size = size + 1
  define.forward(1)
  define.right(17)

turtle.done()
