__author__ = 'MAYANK'

import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def init():
    """
    Initialize for drawing.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('Typography')
    turtle.speed(0)

def space(n):
    """
    provides space between alphabets
    """

    turtle.forward(n)

def drawM(length):
    """
    Draw M.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(135)
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.left(90)
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.right(135)
    turtle.forward(length)
    turtle.left(90)
    turtle.up()

def drawA(length):
    """
    Draw A.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.up()
    turtle.back(length/2)
    turtle.right(90)
    turtle.down()
    turtle.forward(length)
    turtle.up()
    turtle.back(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(90)

def drawY(length):
    """
    Draw Y.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.forward(length/2)
    turtle.down()
    turtle.left(90)
    turtle.forward(length/2)
    turtle.right(45)
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.up()
    turtle.back(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.left(90)
    turtle.down()
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.up()
    turtle.back(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.right(45)
    turtle.back(length/2)
    turtle.right(90)
    turtle.forward(length/2)

def drawN(length):
    """
    Draw N.
    :pre: (relative) pos (0, 0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.left(90)
    turtle.down()
    turtle.forward(length)
    turtle.right(135)
    turtle.forward(math.sqrt(pow(length,2) + pow(length,2)))
    turtle.left(135)
    turtle.forward(length)
    turtle.up()
    turtle.back(length)
    turtle.right(90)

def drawK(length):
    """
    Draw K.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.down()
    turtle.left(90)
    turtle.forward(length)
    turtle.up()
    turtle.back(length/2)
    turtle.down()
    turtle.right(45)
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.up()
    turtle.back(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.right(90)
    turtle.down()
    turtle.forward(math.sqrt(pow(length/2,2) + pow(length/2,2)))
    turtle.left(45)
    turtle.up()

def drawJ(length):
    """
    Draw J.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(length/2)
    turtle.up()
    turtle.back(length/2)
    turtle.right(90)
    turtle.down()
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.back(2*length/2)
    turtle.up()
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def drawI(length):
    """
    Draw I.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.down()
    turtle.forward(length)
    turtle.back(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.back(length)
    turtle.up()
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)

def drawS(length):
    """
    Draw S.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (length,0), heading (east), up
    :return: None
    """

    turtle.down()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.up()
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)

def drawname(length):
    """
    Draw name.
    :pre: (relative) pos (200,0), heading (east), up
    :post: (relative) pos (200 + 11*length + 9*length/5 + length/2 ,0), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.setpos(-320,0)
    turtle.down()
    drawM(length)
    space(length/5)
    drawA(length)
    space(length/5)
    drawY(length)
    space(length/5)
    drawA(length)
    space(length/5)
    drawN(length)
    space(length/5)
    drawK(length)
    space(length/2)
    drawJ(length)
    space(length/5)
    drawA(length)
    space(length/5)
    drawI(length)
    space(length/5)
    drawN(length)
    space(length/5)
    drawS(length)

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: (relative) pos (200 + 11*length + 9*length/5 + length/2 ,0), heading (east), up
    :return: None
    """
    length = int(input('Enter your font size: '))
    drawname(length)

    input('hit enter to close')

if __name__ == '__main__':
    main()