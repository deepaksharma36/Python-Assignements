__author__ = 'MAYANK JAIN mj2997'
__author__ = 'DEEPAK SHARMA ds5930'

import turtle as t
import random
import math

global totalLeaf
totalLeaf=0


def init():
    """
    Initialize for drawing.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,-280), heading (north), down
    :return: None
    """
    t.up()
    t.title('enhanced tree')
    t.setpos(0, -280)
    t.down()
    t.left(90)
    t.speed(0)


def leaf():
    """
    Draws a leaf of quadrilateral shape and fills it with green color
    :pre: pos relative(0,0), heading (north), down
    :post: pos relative(0,0), heading (north), down
    :param: None
    :return: None
    """

    t.color("green")
    t.begin_fill()
    t.down()
    t.left(30)
    t.forward(5)
    t.right(60)
    t.forward(5)
    t.right(120)
    t.forward(5)
    t.right(60)
    t.forward(5)
    t.right(150)
    t.end_fill()
    t.color("black")


def get_tree_angle(bushiness):
    """
    This function determines the get_tree_angle based on the value of the parameter.
    :param: bushiness- (a floating point number between 0 and 1) represents the number
                       of sub branches at the end of a branch
    :return: angle value between first and last branch at the same level
    """
    if bushiness <= 0.2:
        return 50
    if bushiness <= .4:
        return 120
    elif bushiness <= .7:
        return 150
    elif bushiness < 1:
        return 160


def isleaf(leafiness):
    """
    Creates a list of variable reference 'probabilitylist' and stores characters 'L' and 'NL' in it,
    which represents drawing a Leaf and no Leaf respectively. Then using random function an element
    is selected from the list and based on that a boolean value is returned.
    :param: leafiness- (a float point value between 0 and 1) represents the probability of a
                       leaf appearing at the end of a branch that has no sub branches.
    :return: Boolean value
    """
    probabilitylist=[]
    leafiness = leafiness*10
    leafiness = int(leafiness)
    for _ in range(leafiness):
        probabilitylist.append("L")
    for _ in range(10-leafiness):
        probabilitylist.append("NL")
    if probabilitylist[random.randint(0, 9)] == "L":
        return True
    else:
        return False


def leaf_counter():
    """
    Declares a global variable 'totalleaf' and gets incremented by 1 every time this function is called.
    :param: None
    :return: None
    """
    global totalLeaf
    totalLeaf = totalLeaf + 1


def tree(bushiness, n, size, leafiness):
    """
    This function draws a tree recursively where the parameters, bushiness and size
    of the branches, are selected randomly and the parameter n gets reduced by 1
    every time the recursion happens while the leafiness parameter remains the same.
    :pre: pos relative(0,-280), heading (north), down
    :post: pos relative(0,-280), heading (north), down
    :param: bushiness- (a floating point number between 0 and 1) represents the number
                       of sub branches at the end of a branch
            n- (an integer value) represents the b=number of layers for a tree.
            size- (an integer value) represents the size of a brc=nch at that particular level
            leafiness- (a floating point value between 0 and 1) represents the probability of a
                       leaf appearing at the end of a branch that has no sub branches.
    :return: None
    """

    if n == 1:           # base condition for recursion: if n==1, a single branch is drawn.
            t.forward(size)
            if isleaf(leafiness):
                leaf()
                leaf_counter()
            t.back(size)

    elif size <= 1 or n <= 0:       # break condition: if size of branch <=1 or n <=0 recursion breaks
            return
    else:
        tree_angle = get_tree_angle(bushiness)          # tree_angle:angle value between first and last subbranch.
        t.forward(size)
        branch = math.ceil(bushiness*10)            # branch: number of branches at a particular level.
        if branch-1 > 0:
                branch_angle = 1.0*(tree_angle/(branch-1))      # branch_angle: angle between 2 consecutive branches.
        else:
                branch_angle = 0
        if branch % 2 > 0:
                # initial_angle: angle to rotate the turtle head in a position from where branches are being drawn.
                initial_angle = branch_angle*(branch-1)/2.0
        else:
                initial_angle = branch_angle*((branch)/2.0-1)+branch_angle/2.0
        t.left(initial_angle)
        for i in range(int(branch)):            # calling tree method recursively for each branch at level n.
                tree(random.uniform(0, 1), n-1, random.uniform(size/3, 2*size/3), leafiness)
                t.right(branch_angle)
        t.left(branch_angle)
        t.left(initial_angle)       # brings the turtle to initial orientation
        t.back(size)            # brings the turtle to initial position


def main():
    """
    The main function asks for the input parameters from users and if they are invalid
    it again asks the for the valid input. These parameters are used in drawing a tree
    recursively for the method tree(bushiness,n,size,leafiness).
    :pre: pos (0,-280), heading (north), down
    :post: pos (0,-280), heading (north), down
    :param: None
    :return: None
    """
    numberoflevels = int(input("how many number of layers?"))
    while numberoflevels < 0:
        print("invalid input")
        numberoflevels = int(input("how many number of layers of tree?"))

    totalheight = int(input("what is the total height of tree?"))
    while totalheight < 0:
        print("invalid height")
        totalheight = int(input("what is the total height of tree?"))

    bushiness = float(input("what is the bushiness(enter floating point number between 0 and 1)?"))
    while bushiness <= 0 or bushiness >= 1:
        print("Invalid input")
        bushiness = float(input("what is the bushiness(enter floating point number between 0 and 1)?"))

    leafiness = float(input("what is the probability of leafiness?"))
    while leafiness <= 0 or leafiness >= 1:
        print("Invalid input")
        leafiness = float(input("what is the probability of leafiness?"))

    init()
    tree(bushiness, numberoflevels, totalheight/2, leafiness)

if __name__ == "__main__":
    main()
    print("number of leaves are  " + str(totalLeaf))
    z=raw_input("press enter for exit")

