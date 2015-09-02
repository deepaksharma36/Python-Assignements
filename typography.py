__author__ = 'Deepak Sharma'
"""
CSCI-603: Intro Lecture (week 1)
Author: Deepak Sharma (sps@cs.rit.edu)

This program  draws few English language Character for forming a word "COLDPAYS"
"""
import turtle
import math
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """
    :pre: pos (0,0), heading (east), up
    :post: pos (-180,0), heading (east), up
    :return: None
    """
    turtle.up()
    x_cor=-180
    y_cor=0
    turtle.setx(x_cor)
    turtle.sety(y_cor)
    print("Starting Position ("+str(x_cor)+","+str(y_cor)+")" )
    turtle.setheading(0)

    turtle.title('Typography')
    #turtle.speed(-2)
def drawO(length):
    """
    Draw English character 'O'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.up()
def drawSpace(space_length_x,space_length_y):
    """
    Draw Space between characters
    :pre: (relative) pos (X,X), heading (east), up
    :post: (relative) pos (X+space_length_x,X+space_length_y), heading (east), up
    :return: None
    """
    turtle.up()
    if space_length_x>0:
       turtle.forward(space_length_x)
    elif space_length_x<0:
        turtle.back(space_length_x)
        turtle.right(180)
    if space_length_y>0:
        turtle.left(90)
        turtle.forward(space_length_y)
        turtle.right(90)
    elif space_length_y<0:
        turtle.right(90)
        turtle.forward(space_length_y)
        turtle.left(90)
    turtle.up()
def drawL(length):
    """
    Draw English character 'L'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.forward(length)
    turtle.left(180)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.up()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.up()
def drawD(length):
    """
    Draw English character 'D'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.up()
def drawP(length):
    """
    Draw English character 'P'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.up()
    turtle.forward(length)
    turtle.up()
def drawA(length):
    """
    Draw English character 'A'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.left(180)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.up()
def drawY(length):
    """
    Draw English character 'Y'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.down()
    turtle.right(45)
    turtle.forward(math.sqrt((2*math.pow((length/2),2))))
    #moving at 45 degree angle for length sqrt(((math.pow((length/2)+(math.pow((length/2)),2)))
    # calculated using pythagorean theorem.
    turtle.right(45)
    turtle.forward(length/2)
    turtle.right(180)
    turtle.forward(length/2)
    turtle.right(45)
    turtle.forward(math.sqrt((2*math.pow((length/2),2))))
    turtle.right(45)
    turtle.up()
    turtle.right(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.up()
def drawC(length):
     """
     Draw English character 'C'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
     :return: None
     """

     turtle.down()
     turtle.right(180)
     turtle.forward(length)
     turtle.right(90)
     turtle.forward(length)
     turtle.right(90)
     turtle.forward(length)
     turtle.up()
     turtle.right(90)
     turtle.forward(length)
     turtle.left(90)
     turtle.down()

     #print("C: " + str(0)+"," + str(-length))
def drawS(length):
    """
    Draw English character 'S'
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+length,Y), heading (east), up
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.down()
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length)
    turtle.up()

def main():
    """
    Call various function for drawing various English character and space between them.
    :pre: (relative) pos (X,Y), heading (east), up
    :post: (relative) pos (X+26/5*length+,Y), heading (east), up
    :return: None

    """
    length = int(input('Enter the font size(for best fit on screen give 50): '))
    init()
    drawC(length)
    drawSpace(length/5,0)
    drawO(length)
    drawSpace(length/5,0)
    drawL(length)
    drawSpace(length/5,0)
    drawD(length)
    drawSpace(length/5,0)
    drawP(length)
    drawSpace(length/5,0)
    drawL(length)
    drawSpace(length/5,0)
    drawA(length)
    drawSpace(length/5,0)
    drawY(length)
    drawSpace(length/5,0)
    drawS(length)
    turtle.hideturtle()
    #drawO(length)
    input('press enter to close...')

if __name__ == '__main__':
    main()