import turtle,json

class Cube:

	def __init__(self,id,faces): 
		self.id = id
		self.faces = faces

	def generateMoves(self):
		
		n = len(self.faces["UP"])

		aux=""

		for i in range(n):
			aux+="L" + str(i) + "," ;
			aux+="l" + str(i) + "," ;
			aux+="D" + str(i) + "," ;
			aux+="d" + str(i) + "," ;
			aux+="B" + str(i) + "," ;
			aux+="b" + str(i) + "," ;

		return aux;	

	def move(self,movement):

		length = len(self.faces["UP"])
		layer = int(movement[1])
		inv = length -1 -layer

		dict_faces = {0: 'UP', 1: 'DOWN', 2: 'FRONT', 3: 'BACK', 4: 'LEFT', 5: 'RIGHT'}

		if(movement[0]=="L"):
			aux = [ 0 for a in range(length) ]

			for i in range(length):
				aux[i] = self.faces[dict_faces[3]][i][layer]

				self.faces[dict_faces[3]][i][layer] = self.faces[dict_faces[1]][i][layer]
				self.faces[dict_faces[1]][i][layer] = self.faces[dict_faces[2]][i][layer]
				self.faces[dict_faces[2]][i][layer] = self.faces[dict_faces[0]][length-1-i][inv]

			for i in range(length):

				self.faces[dict_faces[0]][length-1-i][inv] = aux[i]


		if(movement[0]=="l"):
			aux = [ 0 for a in range(length)]

			for i in range(length):
				aux[i] = self.faces[dict_faces[2]][i][layer]

				self.faces[dict_faces[2]][i][layer] = self.faces[dict_faces[1]][i][layer]
				self.faces[dict_faces[1]][i][layer] = self.faces[dict_faces[3]][i][layer]
				self.faces[dict_faces[3]][i][layer] = self.faces[dict_faces[0]][length-1-i][inv]

			for i in range(length):

				self.faces[dict_faces[0]][length-1-i][inv] = aux[i]

		if(movement[0]=="D"):
			aux = [ 0 for a in range(length)]

			for i in range(length):
				aux[i] = self.faces[dict_faces[3]][layer][length-1-i]

				self.faces[dict_faces[3]][inv][length-1-i] = self.faces[dict_faces[4]][i][inv]
				self.faces[dict_faces[4]][i][inv] = self.faces[dict_faces[2]][layer][i]
				self.faces[dict_faces[2]][layer][i] = self.faces[dict_faces[5]][length-1-i][layer]
				self.faces[dict_faces[5]][length-1-i][layer] = aux[i]

		if(movement[0]=="d"):
			aux = [ 0 for a in range(length)]

			for i in range(length):
				aux[i] = self.faces[dict_faces[3]][layer][length-1-i]

				self.faces[dict_faces[3]][inv][length-1-i] = self.faces[dict_faces[5]][length-1-i][layer]
				self.faces[dict_faces[5]][length-1-i][layer] = self.faces[dict_faces[2]][layer][i]
				self.faces[dict_faces[2]][layer][i] = self.faces[dict_faces[4]][i][inv]
				self.faces[dict_faces[4]][i][inv] = aux[i]

		if(movement[0]=="B"):
			aux = [ 0 for a in range(length)]

			for i in range(length):
				aux[i] = self.faces[dict_faces[5]][layer][i]

				self.faces[dict_faces[5]][layer][i] = self.faces[dict_faces[1]][layer][i]
				self.faces[dict_faces[1]][layer][i] = self.faces[dict_faces[4]][layer][i]
				self.faces[dict_faces[4]][layer][i] = self.faces[dict_faces[0]][layer][i]
				self.faces[dict_faces[0]][layer][i] = aux[i]

		if(movement[0]=="b"):
			aux = [ 0 for a in range(length)]

			for i in range(length):
				aux[i] = self.faces[dict_faces[4]][layer][i]

				self.faces[dict_faces[4]][layer][i] = self.faces[dict_faces[1]][layer][i]
				self.faces[dict_faces[1]][layer][i] = self.faces[dict_faces[5]][layer][i]
				self.faces[dict_faces[5]][layer][i] = self.faces[dict_faces[0]][layer][i]
				self.faces[dict_faces[0]][layer][i] = aux[i]

	def printState(self):

		turtle.hideturtle()
		turtle.tracer(False)
		turtle.speed(0)

		t= None
		t = turtle.Turtle()

		dict_colours = {0: 'white', 1: 'yellow', 2: 'red', 3: 'orange', 4: 'blue', 5: 'green'}
		dict_faces = {0: 'UP', 1: 'DOWN', 2: 'FRONT', 3: 'BACK', 4: 'LEFT', 5: 'RIGHT'}

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
					face = self.faces[dict_faces[l]]
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
		#turtle.getscreen()._root.mainloop()
		input()

pass

def json2cube():

	input_file = open('cube.txt')
	json_array = json.load(input_file)

	for item in json_array:
		store_details = {"UP":None,"DOWN":None,"FRONT":None,"BACK":None,"LEFT":None,"RIGHT":None}
		store_details['UP'] = item['UP']
		store_details['DOWN'] = item['DOWN']
		store_details['FRONT'] = item['FRONT']
		store_details['BACK'] = item['BACK']
		store_details['LEFT'] = item['LEFT']
		store_details['RIGHT'] = item['RIGHT']

	cubo=Cube("id",store_details)

	return cubo

cubo = [ [ [0,0,0],[0,0,0],[0,0,0] ],
[ [1,1,1],[1,1,1],[1,1,1] ],
[ [2,2,2],[2,2,2],[2,2,2] ],
[ [3,3,3],[3,3,3],[3,3,3] ],
[ [4,4,4],[4,4,4],[4,4,4] ],
[ [5,5,5],[5,5,5],[5,5,5] ] ]

c = json2cube()
print(c.generateMoves())
c.printState()
c.move("B0")
c.printState()