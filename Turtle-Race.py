import turtle 
import time
import random




writer = turtle.Turtle()



writer.speed('0')
writer.pensize('1')
writer.shape('turtle')
writer.penup()
writer.left('90')
writer.forward('100')
writer.backward('200')
writer.right('90')
writer.forward('50')
writer.write("Turtle Race", font=( "Arial",30, "bold"))
writer.hideturtle()



player1 = turtle.Turtle()
player1.speed('0')
player1.color('red')
player1.pensize(1)
player1.shape('turtle')
player1.penup()
player1.left('90')
player1.pendown()


player2 = turtle.Turtle()
player2.speed('0')
player2.color('green')
player2.shape('turtle')
player2.penup()
player2.forward('50')
player2.left('90')
player2.pendown()



player3 = turtle.Turtle()
player3.speed('0')
player3.color('blue')
player3.pensize(1)
player3.shape('turtle')
player3.penup()
player3.backward('50')
player3.left('90')
player3.pendown()

player4 = turtle.Turtle()
player4.speed('0')
player4.color('yellow')
player4.pensize(1)
player4.shape('turtle')
player4.penup()
player4.forward('100')
player4.left('90')
player4.pendown()


player5 = turtle.Turtle()
player5.speed('0')
player5.color('lightgreen')
player5.pensize(1)
player5.shape('turtle')
player5.penup()
player5.backward('100')
player5.left('90')
player5.pendown()


#finish line
fl = turtle.Turtle()
fl.speed('0')
fl.pensize('50')
fl.color('black')
fl.penup()
fl.right('90')
fl.right('90')
fl.right('90')
fl.forward('340')
fl.right('90')
fl.right('90')
fl.right('90')
fl.pendown()
fl.forward('170')
fl.backward('340')



player1.right('90')
player1.right('90')
player1.right('90')


player2.right('90')
player2.right('90')
player2.right('90')


player3.right('90')
player3.right('90')
player3.right('90')


player4.right('90')
player4.right('90')
player4.right('90')


player5.right('90')
player5.right('90')
player5.right('90')



def main() :
  for x in range(145):
    player1.forward(random.randrange(5))
    player2.forward(random.randrange(5))
    player3.forward(random.randrange(5))
    player4.forward(random.randrange(5))
    player5.forward(random.randrange(5))

main()
