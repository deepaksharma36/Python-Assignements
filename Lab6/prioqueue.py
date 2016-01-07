"""
Priority queue.py
author: James heliotis
author: Deepak Sharma ds5930
author: Mayank Jain mj2997
description: A priority queue implementation
"""

from node import LinkedNode

class PriorityQueue:
    __slots__ = "front", "after"
    def __init__(self, after):
        """
        Initialize a new empty priority queue.
        :param after: an ordering function, defination will be  provided by the user/taskmaster
        :return: None (constructor)
        """
        self.front = None
        self.after = after
    def __str__(self):
        """
        Return a string representation of the contents of
        this priority queue, front value first.
        """
        result = "Priority Queue["
        n = self.front
        while n != None:
            result += " " + str( n.value )
            n = n.link
            result += " ]"
        return result


    def dequeue(self):
        """
        Removes one of the values v from the queue such that,
        for all values u in the priority queue,
        after (v,u) is False. If more than one value satisfies the requirement,
        the value will be chosen  the one that has been in the queue the longest. :pre: not isEmpty ()
        :return: None
        """
        assert not self.isEmpty()
        "Dequeue from empty Priority queue"
        self.front = self.front.link


    def enqueue(self, newValue):
        """
        Enter a new value into the queue and this method place this value on its position according the defination
        of the function after(v,u) provided by user/taskmaster.
        :param newValue: the value to be entered into the queue
        :return: None
        """
        newNode = LinkedNode( newValue )
        currentNode=self.front
        priviousNode=self.front
        if  self.front == None:
            self.front = newNode
        else:
            while currentNode!=None and self.after(newNode.value,currentNode.value) :
                        priviousNode=currentNode
                        currentNode=currentNode.link
            if currentNode!=None and self.after(currentNode.value,newNode.value) :
                    if priviousNode!=currentNode:
                       #normal insertion
                       priviousNode.link=newNode
                       newNode.link=currentNode
                    else:
                        #change of head
                        self.front = newNode
                        newNode.link=currentNode
            else:
                    #below logical part take care of nodes to be add in the end and addition of equal priority nodes
                    while  currentNode!=None and (not self.after(currentNode.value,newNode.value)):
                            priviousNode=currentNode
                            currentNode=currentNode.link
                    priviousNode.link=newNode
                    if priviousNode!=currentNode:
                        #elementing case of only single node
                        newNode.link=currentNode


    def isEmpty( self ):
        """
        :return: return true if the priority queue is empty
        """
        return self.front == None


    def peek(self):
        """
        Find in the queue the value that would be removed were the dequeue method to be called at this time.
        :pre: not isEmpty () :return: the value described above remove =
         """
        return  self.front.value
    insert = enqueue
    remove = dequeue


def why_not(v,u):
    """
    This method returns the first item it finds from the priority queue
    :return: boolean value
    """
    return False


def test():
    """
    This example causes the priority queue to always return the the item with the highest id.
    :return: None
    """
    s = PriorityQueue(why_not)

    for value in 5,2,1,6,7,5,5:
        s.enqueue( value )
    print( s.peek() )
    my_q=PriorityQueue(lambda v,u:id(v)>id(u))
    for value in 5,3,6,7:
        my_q.enqueue( value )
    print(my_q.peek())

if __name__ == "__main()__":
    test()