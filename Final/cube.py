import hashlib
import turtle, json

class Cube:

    def __init__(self, id="", faces=None):  # constructor
        self.id = id
        self.faces = faces
        self.dict_colours = {0: 'red', 1: 'blue', 2: 'yellow', 3: 'green', 4: 'orange', 5: 'white'}
        self.dict_faces = {0: 'BACK', 1: 'DOWN', 2: 'FRONT', 3: 'LEFT', 4: 'RIGHT', 5: 'UP'}

    def setID(self,id):
        self.id=id

    def setFaces(self,faces):
        self.faces=faces

    def generateMoves(self):  # this method computes the valid moves for the cube

        n = len(self.faces["UP"])  # here we get the dimension of the cube NxNxN

        ret = ()
        aux = ""

        for i in range(n):
            aux = "L" + str(i)
            ret += (aux,)
            aux = "l" + str(i)
            ret += (aux,)
            aux = "D" + str(i)
            ret += (aux,)
            aux = "d" + str(i)
            ret += (aux,)
            aux = "B" + str(i)
            ret += (aux,)
            aux = "b" + str(i)
            ret += (aux,)

        return ret;

    def moveL(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(3) # 3:LEFT
        if (layer == length - 1):
            self.turnRight(4) # 4:RIGHT
            self.turnRight(4)
            self.turnRight(4)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[0]][i][layer]  # store the layer 0:BACK

            self.faces[self.dict_faces[0]][i][layer] = self.faces[self.dict_faces[1]][i][layer]	#0:BACK 1:DOWN 2:FRONT 5:UP
            self.faces[self.dict_faces[1]][i][layer] = self.faces[self.dict_faces[2]][i][layer]
            self.faces[self.dict_faces[2]][i][layer] = self.faces[self.dict_faces[5]][length - 1 - i][inv]

        for i in range(length):
            self.faces[self.dict_faces[5]][length - 1 - i][inv] = aux[i]	# 5:UP

    def moveD(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(1)	# 1:DOWN
        if (layer == length - 1):
            self.turnRight(5)	# 5:UP
            self.turnRight(5)
            self.turnRight(5)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[0]][inv][length - 1 - i]	# 0:BACK

            self.faces[self.dict_faces[0]][inv][length - 1 - i] = self.faces[self.dict_faces[3]][i][inv]	# 0:BACK 3:LEFT 2:FRONT 4:RIGHT
            self.faces[self.dict_faces[3]][i][inv] = self.faces[self.dict_faces[2]][layer][i]
            self.faces[self.dict_faces[2]][layer][i] = self.faces[self.dict_faces[4]][length - 1 - i][layer]
        for i in range(length):
            self.faces[self.dict_faces[4]][i][layer] = aux[length - 1 - i]	# 4:RIGHT

    def moveB(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(0)	# 0:BACK
        if (layer == length - 1):
            self.turnRight(2)	# 2:FRONT
            self.turnRight(2)
            self.turnRight(2)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[4]][layer][i]	# 4:RIGHT

            self.faces[self.dict_faces[4]][layer][i] = self.faces[self.dict_faces[1]][layer][i]	# 4:RIGHT 1:DOWN 3:LEFT 5:UP
            self.faces[self.dict_faces[1]][layer][i] = self.faces[self.dict_faces[3]][layer][i]
            self.faces[self.dict_faces[3]][layer][i] = self.faces[self.dict_faces[5]][layer][i]
            self.faces[self.dict_faces[5]][layer][i] = aux[i]

    def move(self, movement):  # this method performs the selected move on the cube

        length = len(self.faces["UP"])  # here we get the dimension of the cube NxNxN
        layer = int(movement[1])  # here we get the layer where the move is performed
        mov = movement[0]  # here we get the type of movement. Example L0 layer is 0, mov = L
        inv = length - 1 - layer  # here we get the inverse layer of the selected layer (useful for some movements)
        aux = [0 for a in range(length)]  # we create an auxiliaty array to store a row/column of a face

        if (mov == "L"):
            self.moveL(layer, inv, aux, length)
        if (mov == 'l'):
            for i in range(3):
                self.moveL(layer, inv, aux, length)
        if (mov == "D"):
            self.moveD(layer, inv, aux, length)
        if (mov == 'd'):
            for i in range(3):
                self.moveD(layer, inv, aux, length)
        if (mov == "B"):
            self.moveB(layer, inv, aux, length)
        if (mov == 'b'):
            for i in range(3):
                self.moveB(layer, inv, aux, length)
        self.cubeMD5()

    def printState(self):   #This method prints a specific state of the cube

        turtle.hideturtle()
        turtle.tracer(False)
        turtle.speed(0)

        t = turtle.Turtle()

        x = 0
        y = 0
        n = len(self.faces["UP"])

        for l in range(6):  # make the 6 faces

            if (l < 2 or l > 3):
                y = 0
                if (l == 0):
                    x = 0
                elif (l == 1):
                    x = (-30 - 30 * n) * 2
                elif (l == 4):
                    x = (-30 - 30 * n) * 3
                else:
                    x = -30 - 30 * n
            else:
                x = (-30 - 30 * n) * 2
                if (l == 2):
                    y = -30 - 30 * n
                else:
                    y = 30 + 30 * n

            for k in range(n):  # make a cube face

                for j in range(n):  # make a row of N squares

                    t.penup()
                    t.goto(x, y)
                    t.pendown()
                    if(l==1 or l==2):
                    	a=l
                    if(l==4 or l==5):
                    	a=l-1
                    if(l==0):
                    	a=5
                    if(l==3):
                    	a=0
                    face = self.faces[self.dict_faces[a]]
                    t.begin_fill()
                    t.fillcolor(self.dict_colours[face[k][j]])  # here we would have to take the color from the matrix

                    for i in range(4):  # make a square
                        t.forward(30)
                        t.right(90)

                    t.end_fill()

                    x += 30

                x -= 30 * n
                y -= 30

        t.penup()
        t.goto(1000, 1000)
        print("Press ENTER to continue.")
        input()

    def turnRight(self, index): #This is an internal method that allows us to rotate a face of the cube 90 degrees to the right

        matrix = self.faces[self.dict_faces[index]]

        res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        aux = [0 for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                aux[j] = matrix[i][j]

            for j in range(len(matrix)):
                res[j][len(matrix) - 1 - i] = aux[j]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.faces[self.dict_faces[index]][i][j] = res[i][j]

    def cubeString(self):   #This method creates a String from the cube state
        message = ""
        length = len(self.faces["UP"])
        for i in range(6):
            for j in range(length):
                for k in range(length):
                    message+=str(self.faces[self.dict_faces[i]][j][k])
        return message

    def cubeMD5(self,md=""):  #This  method creates an specific MD5 identifier from the string of the previous method
        if md == "":
        	md=self.cubeString()
        result =  hashlib.md5(md.encode())
        self.setID(result.hexdigest())

    def cube2Json(self, filename): #This method creates a json file from a cube object
        with open(filename, 'w') as outfile:
            json.dump([self.faces], outfile)

    def json2cube(self,filename):    #This method creates a cube object from a json file
        input_file = open(filename)
        json_array = json.load(input_file)

        for item in json_array:
            store_details = {"BACK": None, "DOWN": None, "FRONT": None, "LEFT": None, "RIGHT": None, "UP": None}
            store_details['BACK'] = item['BACK']
            store_details['DOWN'] = item['DOWN']
            store_details['FRONT'] = item['FRONT']
            store_details['LEFT'] = item['LEFT']
            store_details['RIGHT'] = item['RIGHT']
            store_details['UP'] = item['UP']

        self.setFaces(store_details)
        self.cubeMD5()