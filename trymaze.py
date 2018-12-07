import turtle
import math
 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)

#registershapes
turtle.registershape("wizard_right.gif")
turtle.registershape("wizard_left.gif")
turtle.registershape("treasure.gif")
turtle.registershape("wall.gif")
 
 
#create pen
class Pen(turtle.Turtle):
   
    def __init__(self):
       
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
 
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizard_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
	self.gold = 0
 
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_left(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
 
	self.shape("wizard_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_right(self):
        move_to_x = player.xcor() +24
        move_to_y = player.ycor() 

	self.shape("wizard_right.gif")

 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
   def is_collision(self, other):
	a=self.xcor()-other.xcor()
	b=self.ycor()-other.ycor()
	distance=math.sqrt((a**2)+(b**2))
	
	if distance<5:
		return True
	else:
		return False


class Treasure(turtle.Turtle):
   def _inti_(self,x,y):
	turtle.Turtle._inti_(self)
	self.shape("treasure.gif")
	self.color("gold")
	self.penup()
	self.speed(0)
	self.gold=100
	self.goto(x,y)

   def destroy(self):
	self.goto(2000.2000)
	self.hideturtle()	




#create level list
levels = [""]
 
#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX        XXXXX",
"X           XXXXXX  XXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X                       X",
"XXXXXXX  XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX                  X",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                       X",
"XXXXX    XXXXXXXXXX T XXX",
"X        XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                       X",
"XXXXXXXXXXXXX   XXXXXXXXX",
"XXXXXX   XXXX   XXXXXXXXX",
"XXXXX    XXXX           X",
"X                      XX",
"XXXXXXX   YXXXXXXXXXXXXXX",
"XXXXXX     XXXXX     XXXX",
"XXXXXX                XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
 
treasures= []
   
levels.append(level_1)
 
#Create Level Setup Fuction
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
           
            #Get the caracter at each x,y cordinate            
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
 
            #Check if it is an X
            if character == "X":
                pen.goto(screen_x, screen_y)
		pen.shape("wall.gif")
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x,screen_y))
           
           
            #Check if it is a P (Player)
            if character == "P":
                pen.goto(screen_x, screen_y)

            #Check if it is a T (treasure)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y)


               
 
#class instances
pen = Pen()
player = Player()
 
#Create wall cordinate List
walls = []
 
 
setup_maze(levels[1])
 
#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
 
#Turn off screen updates
wn.tracer(0)
 
#main game loop
while True:
    #Update screen
    wn.update()