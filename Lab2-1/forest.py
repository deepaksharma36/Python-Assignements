__author__ = 'Deepak Sharma , Mayank Jain' 
"""
CSCI-603: Lab 2
Author: Deepak Sharma(ds5930) Mayak Jain(mj2997)  
This program  can draw three types of trees of random heights, hut, sun and star also calculate total wood present in tree and hut. 
"""

import turtle as t
import math
import random as r
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

def init(x , y):
    """	
    :input: x and y corrdinate for setting intial/starting corrdinates
    :pre:(relative) pos (0,0), heading (east), up
    :post:(relative) pos (x,y), heading (east), up
    :return: None
    """
    t.up()
    t.title('forest')
    t.setx(x)
    t.sety(y)
    
def trunk(length):
    """
     This method draws the trunk of given length for all types of tree.
    :input: length of the truck of the tree  
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y+length), heading (east), up
    :return: None
    """

    t.down()
    t.left(90)
    t.forward(length)
    t.right(90)
    t.up()

def polygon(n,side_length):
    """
     This method draws polygons with given sides and size.
    :input: number of sides and side length of the polygon  
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (east), up
    :return: None
    """
    t.down()
    angle_sum=(n-2)*180
    rotation=angle_sum/n
    for dummy in range(n):
          t.left(180-rotation)
          t.forward(side_length)
    t.up()

def maple_shape(length):
    """
     This method draws the circle shape for type maple tree.
    :input: radius length of the maple shape
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (west), up
    :return: None
    """
    t.down()
    t.circle(length)
    t.right(180)
    t.up()

def pine_shape(length):
    """
     This method draws the triangle shape for type pine tree.
    :input: Side length of the pine shape
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (west), up
    :return: None
    """
    t.down()
    t.forward(length/2)
    polygon(3,length)
    t.right(180)
    t.forward(length/2)
    t.up()

def bodhi_shape(length):
    """
     This method draws the hexagonal shape for type bodhi tree.
    :input: length of the bodhi shape
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (west), up
    :return: None
    """
    t.down()
    t.right(30)
    polygon(6,length)
    t.left(30)
    t.right(180)
    t.up()

def star2(length):
    """
     This method draws the star using while loop of given dimensions at height = length.
    :input: height of the star
    :pre:(relative) pos  (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (east), up
    :return: None
    """
    t.left(90)
    t.forward(length)
    t.down()
    t.forward(10)
    angle=0
    while angle<360:
         t.forward(10)
         t.back(10)
         angle+=45
         t.right(45)
    t.up()
    t.back(length+10)
    t.right(90)

def house(length):
       """
        This method draws the house of pentagon shape with wall height = length.
       :input: height of the wall of the house
       :pre:(relative) pos (X,Y), heading (east), up
       :post:(relative) pos (X+length,Y), heading (east), up
       :return: None
       """
       t.down()
       trunk(length)
       t.right(45)
       trunk(length/math.sqrt(2))
       t.right(90)
       trunk(length/math.sqrt(2))
       t.right(45)
       trunk(length)
       t.right(180)
       t.up()

def treeAndHouse(type,totalWood):
    """
     This method draws a tree for given type condition and returns the totalwood forest contains .
    :input: type of tree that will be drawn and total wood present in forest before drawing the given tree.
    :pre:(relative) pos (X,Y), heading (east), up
    :post:(relative) pos (X,Y), heading (east), up
    :return: length of the tree and total wood consumed after creating give type of tree 
    """
    t.down()
    if type == "Mapel":
        length = r.randint(50,150)
        trunk(length)
        maple_shape(length/3)
        trunk(length)
        t.right(180)
        #print(length)
        t.up()
        return (5*length/3,totalWood+length)
    elif type == "Pine":
        length = r.randint(50,200)
        trunk(length)
        pine_shape(2*length/3)
        trunk(length)
        t.right(180)
        #print(length)
        t.up()
        return (length*(1+(1/math.sqrt(3))),totalWood+length)

    elif type =="bodhiTree":
       length = r.randint(50,175)
       trunk(length)
       bodhi_shape(length/2)
       trunk(length)
       t.right(180)
       #print(length)
       t.up()
       return (2*length,totalWood+length)

    elif type=="House":
       length = 100
       house(100)
       #print(2*(length+length/math.sqrt(2)))
       t.up()
       return (150,totalWood+2*(length+length/math.sqrt(2)))


def main():
    """
    :pre:(relative) pos (0,0), heading (east), up
    :post:(relative) pos (X,0), heading (east), up
    :return: none 
    """
    
    numberOfTree=int(raw_input("How many trees in your forest ?"))
    treeHome=["Mapel","Pine","bodhiTree"]
    dummy_house=raw_input("Is there a house in the forest (y/n)?")
    highestHeight=50

    treeHomeRandom=[treeHome[r.randint(0,2)] for n in range(numberOfTree) ]
    if dummy_house in ['Y','y']:
        if numberOfTree>2:
           treeHomeRandom.insert(r.randint(1,numberOfTree-2),"House")
        elif numberOfTree<=2:
             treeHomeRandom.insert(1,"House")  
    if numberOfTree <= 11:
        if dummy_house in ['Y','y']:
          init(-(numberOfTree+1)*100/2,-100)
        else: 
          init(-(numberOfTree)*100/2,-100)
    else:
         init(-600,-100)

    #print(treeHomeRandom)
    totalWood=0
    for myTree in treeHomeRandom:
       (length,totalWood)=treeAndHouse(myTree,totalWood)
       if length>highestHeight:
           highestHeight=length
       t.up()
       t.forward(100)
       t.down()
    t.up()
    t.back(100)
    star2(highestHeight+10)
    
    raw_input("Night is done Press Enter for day")
    
    t.reset()
    print("We have " + str(totalWood) +" units of lumber for building." )
    print ("We will build a house with walls " + str((totalWood)/(2+math.sqrt(2)))+ " tall.")
    init(0,-300)
    house((totalWood)/(2+math.sqrt(2)))
    t.left(90)
    t.forward(3*abs((totalWood)/(2+math.sqrt(2)))/2+30)
    t.right(90)
    maple_shape(30)
    t.right(90)
    t.up()
    t.back(3*abs((totalWood)/(2+math.sqrt(2)))/2+30)
    t.right(90)
    raw_input("Day is done, house is build, Press enter to quit")

if __name__ == '__main__':
	main()
