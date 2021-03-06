import turtle
import time
import random

delay = .1

a = 0

body_segment = [] #a list to store snake body segments

#set the window first

window = turtle.Screen()
# the window is created,now i want to customize it -.-

window.title("Snake Game :D")
window.bgcolor("grey")
window.setup(width= 800, height= 600)
window.tracer(0) #stops the screen update so we have to manually update the screen

#main code will be written in between window.tracer and window.mainloop

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup() #leaves no line
head.goto(0, 0) #snake will start from 0,0 position
head.direction = "stop"

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,200)

#make a turtle object to show score

score = turtle.Turtle()
score.speed(0) #animation speed 
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(330, 265)
score.write("Score : 0", align = "center")


def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down": 
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)



window.listen()

window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")





#main game loop
while True:
	window.update()

	#check for the collisions
	if head.xcor() >390 or head.xcor() <-390 or head.ycor() >290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"


		#hiding the segments
		for i in body_segment:
			i.goto(2000, 2000) #hehe,, tricky way

		body_segment.clear()

		a = 0
		score.clear()
		score.write("Score : 0", align = "center")




	# if a snake eats a food then the number of segments will increase

	if head.distance(food)<20: #there is a builtin function distance() that measures distance between 2 turtle objects
		x = random.randint(-380, 380)
		y = random.randint(-280, 280)
		food.goto(x, y)

		# create a new segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("skyblue")
		new_segment.penup()
		new_segment.goto(0, 0)
		body_segment.append(new_segment)

		#shorten the delay
		delay = 0.09

		#increase the score
		a = a+1
		score.clear()
		score.write("Score : {}".format(a), align = "center")



	for i in range(len(body_segment)-1, 0, -1):
		x = body_segment[i-1].xcor()
		y = body_segment[i-1].ycor()
		body_segment[i].goto(x, y)

	if len(body_segment)>0:
		x = head.xcor()
		y = head.ycor()

		body_segment[0].goto(x, y)


	move()

	#check for the body collision, we need to check for each body segment
	for i in body_segment:
		if i.distance(head) <20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			for i in body_segment:
				i.goto(2000, 2000)
			body_segment.clear()
			a = 0
			score.clear()
			score.write("Score : 0", align = "center")

	time.sleep(delay)




window.mainloop()# ->this statement will help to pop up the window for infinite time period


