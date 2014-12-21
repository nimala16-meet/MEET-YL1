import turtle
turtle.pd()
def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()	
	turtle.goto(x+25,y)
	turtle.goto(x+25,y+25)
	turtle.goto(x,y+25)
	turtle.goto(x,y)

draw_square(0,0)

def draw_triangle(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()	
	turtle.goto(x+25,y+50)
	turtle.goto(x+50,y)
	turtle.goto(x,y)

draw_triangle(20,20)


turtle.onscreenclick(draw_square, btn=1, add=True)
turtle.onscreenclick(draw_triangle, btn=3, add=True)
 
 

turtle.onscreenclick(turtle.goto,btn=1,add=True)
turtle.shape("turtle")
turtle.color("#00008B")
turtle.onscreenclick(turtle.goto,btn=2,add=True)
turtle.shape("turtle")
turtle.color("#FFFF00")	
turtle.onscreenclick(turtle.goto,btn=3,add=True)
turtle.shape("turtle")
turtle.color("#FFB6C1")


def mykey():turtle.color("pink")     
turtle.getscreen().onkeypress(mykey,"Up")
turtle.getscreen().listen()

def mykey():turtle.color("blue")     
turtle.getscreen().onkeypress(mykey,"Down")
turtle.getscreen().listen()

def mykey():turtle.color("red")     
turtle.getscreen().onkeypress(mykey,"Right")
turtle.getscreen().listen()

def mykey():turtle.color("yellow")     
turtle.getscreen().onkeypress(mykey,"Left")
turtle.getscreen().listen()



turtle.mainloop()

