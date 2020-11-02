# space invader

import turtle
import os
import math
import random

#Set up the Screen :
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")

# Draw Border :
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
for side in range (4) :
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0 :
score = 0
# Draw the Score :
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "score : %s" %score
score_pen.write(scorestring, False,align="left", font = ("Arial",10,"normal"))
score_pen.hideturtle()

	

# Create the Player Turtle :
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-300)
player.setheading(90)
playerspeed = 20

# Create the Enemy :
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemy.hideturtle()
enemyspeed = 2



# Create the Player's bullet :
bullet = turtle.Turtle()	
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20 #It is Global Declaration

# Create, Destroy the Enemies :
# Here their are 5 Enemies :

number_of_enemies = 5
# Create the empty list :
enemies = []



#dont know position :
for enemy in enemies :
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)
	
enemyspeed = 2

# Now only one enemy is moving so,collision also works with moving one
# go in main game loop : "above #move the Enemy"



# Add Enemies to the list :
for i in range (number_of_enemies) :
	# Create Enemy :
	enemies.append(turtle.Turtle())
	
for enemy in enemies :
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)
	
enemyspeed = 2

	
enemyspeed = 2
# Now since player does't move & are in same position we need to impot random



	


# Define Bullet State :
# ready --> Ready to fire.
# fire --> Bullet has fired.

bulletstate = "ready"
# We are binding ''space'' button to fire the bullet in keyboard binding section :

	

# Move the player left & right :
def move_left() :
	x = player.xcor()
	x -= playerspeed
	if x < -280 :
		x = -280
	player.setx(x)

def move_right() :
	x = player.xcor()
	x += playerspeed
	if x > 280 :
		x = 280
	player.setx(x)
	
	
def fire_bullet() :
	# Declare bulletstate as if it needs changed
	global bulletstate
	if bulletstate == "ready" :
		bulletstate = "fire"
		# Move the bullet to just above the player :
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()	

def isCollision(t1,t2)  :
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15 :
		return True
	else :
		return False
		
	

# Create Keyboard Bindings :
	
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet,"space")

# Main Game Loop :

while True :
	for enemy in enemies :
		# Move the Enemy :
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		
		# Move the Enemy Back and Down :
		if enemy.xcor() > 280 :
			# Move all the Enemies down :
				for e in enemies :
					y = e.ycor()
					y -=40
					e.sety(y)
			    # Change enemy Direction :
				enemyspeed *= -1
				
			
		if enemy.xcor() < -280 :
			# Move all enemy down :
				for e in enemies :
					y = enemy.ycor()
					y -=40
					enemy.sety(y)
				#Change enemy direction :
				enemyspeed *= -1	
			 
			
					
		# Check Collision between Bullet and Enemy :
		if isCollision(bullet,enemy) :
			# Reset the Bullet :
			bullet.hideturtle()			
			bulletstate = "ready"
			bullet.setposition(0,-400)
			# Reset the Enemy :
			x = random.randint(-200,200)
			y = random.randint(100,250)
			enemy.setposition(x,y)
			# Update score
			score += 10
			scorestring = "score : %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align = "left", font=("arial",10,"normal"))
		# Check Collision between the Player and Enemy :
		if isCollision(player,enemy) :
			player.hideturtle()
			enemy.hideturtle()
			
			break # It will bring out of the While loop...
				
	# Move the Bullet :
	if bulletstate == "fire" :
		y = bullet.ycor()
		y +=bulletspeed
		bullet.sety(y)
		
	# Check to see bullet has reach the Top :
	if bullet.ycor() > 275 :
		bullet.hideturtle()
		bulletstate = "ready"
		
	
		






turtle.done()
