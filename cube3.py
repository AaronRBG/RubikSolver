import turtle, json


class Cube:

    def __init__(self, id, faces):  # constructor
        self.id = id
        self.faces = faces
        self.dict_colours = {0: 'white', 1: 'yellow', 2: 'red', 3: 'orange', 4: 'blue', 5: 'green'}
        self.dict_faces = {0: 'UP', 1: 'DOWN', 2: 'FRONT', 3: 'BACK', 4: 'LEFT', 5: 'RIGHT'}

    def generateMoves(self):  # this method computes the valid moves for the cube

        n = len(self.faces["UP"])  # here we get the dimension of the cube NxNxN

        aux = ""

        for i in range(n):
            aux += "L" + str(i) + ",";
            aux += "l" + str(i) + ",";
            aux += "D" + str(i) + ",";
            aux += "d" + str(i) + ",";
            aux += "B" + str(i) + ",";
            aux += "b" + str(i) + ",";

        return aux;

    def moveL(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(4)
        if (layer == length - 1):
            self.turnRight(5)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[3]][i][layer]  # store the layer

            self.faces[self.dict_faces[3]][i][layer] = self.faces[self.dict_faces[1]][i][layer]
            self.faces[self.dict_faces[1]][i][layer] = self.faces[self.dict_faces[2]][i][layer]
            self.faces[self.dict_faces[2]][i][layer] = self.faces[self.dict_faces[0]][length - 1 - i][inv]

        for i in range(length):
            self.faces[self.dict_faces[0]][length - 1 - i][inv] = aux[i]

    def moveD(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(1)
        if (layer == length - 1):
            self.turnRight(0)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[3]][layer][length - 1 - i]

            self.faces[self.dict_faces[3]][inv][length - 1 - i] = self.faces[self.dict_faces[4]][i][inv]
            self.faces[self.dict_faces[4]][i][inv] = self.faces[self.dict_faces[2]][layer][i]
            self.faces[self.dict_faces[2]][layer][i] = self.faces[self.dict_faces[5]][length - 1 - i][layer]
            self.faces[self.dict_faces[5]][length - 1 - i][layer] = aux[i]

    def moveB(self, layer, inv, aux, length):

        if (layer == 0):
            self.turnRight(3)
        if (layer == length - 1):
            self.turnRight(2)

        for i in range(length):
            aux[i] = self.faces[self.dict_faces[5]][layer][i]

            self.faces[self.dict_faces[5]][layer][i] = self.faces[self.dict_faces[1]][layer][i]
            self.faces[self.dict_faces[1]][layer][i] = self.faces[self.dict_faces[4]][layer][i]
            self.faces[self.dict_faces[4]][layer][i] = self.faces[self.dict_faces[0]][layer][i]
            self.faces[self.dict_faces[0]][layer][i] = aux[i]

    def move(self, movement):  # this method performs the selected move on the cube

        length = len(self.faces["UP"])  # here we get the dimension of the cube NxNxN
        layer = int(movement[1])  # here we get the layer where the move is performed
        mov = movement[0]  # here we get the type of movement. Example L0 layer is 0, mov = L
        inv = length - 1 - layer  # here we get the inverse layer of the selected layer (useful for some movements)
        aux = [0 for a in range(length)]  # we create an auxiliaty array to store a row/column of a face

        if (mov == "L"):
            self.moveL(layer, inv, aux, length)
        if (mov == 'l'):
            for i in range(length):
                self.moveL(layer, inv, aux, length)
        if (mov == "D"):
            self.moveD(layer, inv, aux, length)
        if (mov == 'd'):
            for i in range(length):
                self.moveD(layer, inv, aux, length)
        if (mov == "B"):
            self.moveB(layer, inv, aux, length)
        if (mov == 'b'):
            for i in range(length):
                self.moveB(layer, inv, aux, length)

    def printState(self):

        turtle.hideturtle()
        turtle.tracer(False)
        turtle.speed(0)

        t = None
        t = turtle.Turtle()

        x = 0
        y = 0

        n = 3

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

                for j in range(n):  # make a row of 3 squares

                    t.penup()
                    t.goto(x, y)
                    t.pendown()
                    face = self.faces[self.dict_faces[l]]
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
        # turtle.getscreen()._root.mainloop()
        input()

    def turnRight(self, index):

        matrix = self.faces[self.dict_faces[index]]

        res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        aux = [0, 0, 0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                aux[j] = matrix[i][j]

            for j in range(len(matrix)):
                res[j][len(matrix) - 1 - i] = aux[j]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.faces[self.dict_faces[index]][i][j] = res[i][j]

    def turnLeft(self, index):

        for i in range(3):
            self.turnRight(index)


def json2cube(filename):
    input_file = open(filename)
    json_array = json.load(input_file)

    for item in json_array:
        store_details = {"UP": None, "DOWN": None, "FRONT": None, "BACK": None, "LEFT": None, "RIGHT": None}
        store_details['UP'] = item['UP']
        store_details['DOWN'] = item['DOWN']
        store_details['FRONT'] = item['FRONT']
        store_details['BACK'] = item['BACK']
        store_details['LEFT'] = item['LEFT']
        store_details['RIGHT'] = item['RIGHT']

    cubo = Cube("id", store_details)

    return cubo


def cube2Json(c, filename):
    with open(filename, 'w') as outfile:
        json.dump([c.faces], outfile)


cubo = [
    {
        "UP": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "DOWN": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        "FRONT": [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        "BACK": [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        "LEFT": [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
        "RIGHT": [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    }
]

c = json2cube('cube.txt')
print('ok')
print(c)
cube2Json(c, 'data1.txt')
print('ok')
print(c)
c = json2cube('data1.txt')
print('ok')
print(c)
