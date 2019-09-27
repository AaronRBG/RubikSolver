#Python program to draw color filled square in turtle programming
import turtle

turtle.hideturtle()
turtle.tracer(False)
turtle.speed(0)

t = turtle.Turtle()
dict_colours = {0: 'red', 1: 'blue', 2: 'yellow', 3: 'green', 4: 'orange', 5: 'white'}
dict_faces = {0: 'UP', 1: 'DOWN', 2: 'FRONT', 3: 'BACK', 4: 'LEFT', 5: 'RIGHT'}
cube = {
	'BACK': [[4,4,4],[3,3,3],[3,3,3]],
	'DOWN': [[1,1,1],[2,4,4],[1,1,1]],
	'FRONT': [[2,2,2],[2,2,2],[5,5,5]],
	'LEFT': [[2,4,4],[0,0,0],[2,4,4]],
	'RIGHT': [[5,5,3],[1,1,1],[5,5,3]],
	'UP': [[0,0,0],[5,5,3],[0,0,0]],
}
x=0
y=0

n = 3

for l in range(6):   	# make the 6 faces

	if(l<2 or l > 3):
		y=0
		if(l==0):
			x=0
		elif(l==1):
			x=(-30-30*n)*2
		elif(l==4):
			x=(-30-30*n)*3
		else:
			x=-30-30*n
	else:
		x=(-30-30*n)*2
		if(l==2):
			y=-30-30*n
		else:
			y=30+30*n

	for k in range(n):	# make a cube face

		for j in range(n):	# make a row of 3 squares

			t.penup()
			t.goto(x,y)
			t.pendown()
			face = cube[dict_faces[l]]
			t.begin_fill()
			t.fillcolor(dict_colours[face[k][j]])	# here we would have to take the color from the matrix

			for i in range(4):	# make a square

				t.forward(30)
				t.right(90)
			
			t.end_fill()

			x+=30

		x-=30*n	
		y-=30
	

t.penup()
t.goto(1000,1000)
turtle.getscreen()._root.mainloop()
