#set-up
import turtle
t = turtle.Pen()

'''
#Creates canvas
t = turtle.Pen()

#Tells arrow to move 50 pixels to the direction it's facing
t.forward(50)
# *Note* Can also use t.backward(-50)

#Changes direction of travel by 90 degrees to left (up in this case)
t.left(90)

#Clears canvas, puts turtle at origin
t.reset()

#Clears canvas, turtle does not move
t.clear()

#Pulls pen "up" / Stops drawing
t.up()

#Puts pen "down" / Keeps drawing
t.down() 
'''

#triangle 1
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

#re-positioning
t.up()

t.forward(50)
t.left(90)
t.forward(60)
t.left(90)
t.backward(50)

#triangle 2
t.down()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
