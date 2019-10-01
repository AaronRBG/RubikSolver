import json


def cube2Json(c):
    with open('data.txt', 'w') as outfile:
        json.dump(c, outfile)


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

cube2Json(cubo)
