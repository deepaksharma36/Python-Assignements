"""
description: Linked chained Hash Map with resizing
language: python3
author: ds5930@cs.rit.edu Deepak Sharma
author: mj2997@cs.rit.edu Mayank Jain
"""
from set import SetType
from collections.abc import Iterable, Iterator
class Data:
    """
        A value entry plus a two link to make it a node in a double linked list (chainLink and backChain) and
        two links -- forwardLink and backLink-- for keeping track of the order of elements in which they were inserted.
    """
    __slots__="forwardLink","backLink","chainLink","data","backChain"

    def __init__(self, obj, backLink=None, forwardLink=None, chainLink=None , backChain=None):
        """
        Constructor for creating for input object
        """
        self.data=obj
        self.forwardLink=None
        self.backLink=None
        self.chainLink=None
        self.backChain=None
    def hashCode(self,lookup,size):
        """
        return: hashcode for data object using inbuilt hash method of python
        """
        return hash(self.data) % size



class LinkedHashTable(SetType):
    """
    This Linked hash map table is a list of linked lists. Each node
    in each linked list contains an entry in the map.
    So as the table fills up more and more, this HashMap rehashes to twice its
    size when the number of entries exceeds the length of the table it also reduce
    its size when number of elements are significantly less then capacity.
    In addition it also maintains Double link List between data nodes for
    keeping track of the order in which nodes were inserted in the HashMap
    """

    __slots__= "first","last","size","capacity","loadFactor","lookup","table"

    def __init__(self, initial_num_buckets=100, load_limit=0.75):
        """
        Create a new empty hash table.
        :param initial_num_buckets: starting number_of_buckets
        :param load_limit: See class documentation above.
        :return: none
        """
        self.capacity = 10 if initial_num_buckets < 10 else initial_num_buckets
        self.size=0
        self.first=None
        self.last=None
        self.loadFactor=load_limit
        self.table=[None]*self.capacity
        self.lookup={}
        self.loadLookup()

    def _rehash( self,extend ):
        """
        Rebuild the map in a larger table. The current map is not changed
        in any way that can be seen by its clients, but internally its table is
        grown.
        :return: None
        """
        if extend:
            new_cap = 2 * self.capacity
        else:
            new_cap=self.capacity//2
        self.capacity=new_cap
        self.table=[None]*new_cap
        self.size=0
        for item in self:
            self.add(item)

    def loadLookup(self):
        """
        create dictionary lookup for calculating hash code
        :return:
        """
        value=0
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for item in alphabets:
            self.lookup[item]=value
            value+=1

    def add(self,item):
        """
        Insert a new object into the hash table and remember when it was added
        relative to other calls to this method. However, if the object is
        added multiple times, the hash table is left unchanged, including the
        fact that this object's location in the insertion order does not change.
        Double the size of the table if its load_factor exceeds the load_limit.
        :param obj: the object to add
        :return: None
        """
        if float(self.size)/float(self.capacity)>self.loadFactor:
            self._rehash(True)
        if self.contains(item):
            return
        newNode = Data(item)
        hashcode= newNode.hashCode(self.lookup,self.capacity)
        position=self.table[hashcode]
        if self.size==0:
            self.table[hashcode]=newNode
            self.first=newNode
            self.last=newNode
            newNode.backChain=None
            self.size+=1
        else:
            if(position!=None):
                while(position.chainLink!=None):
                    position=position.chainLink
                position.chainLink=newNode
                newNode.backChain=position
            else:
                 self.table[hashcode]=newNode
                 newNode.backChain=None
            self.size+=1
            self.last.forwardLink=newNode
            newNode.backLink=self.last
            self.last=newNode
            position=None

    def __position(self,item):
        """
        This is a helper method
        Return pointer to the position of the item if its exist in hash Map
        else returns None
        :param item:
        :return: reference to the node which contains the item in the hash map
        """
        item=Data(item)
        hashCode=item.hashCode(self.lookup,self.capacity)
        chain=self.table[hashCode]
        if chain!=None and chain.data==item.data:
                return chain
        while chain!=None:
            if chain.data==item.data:
                return chain
            chain=chain.chainLink
        return chain

    def contains(self,item):
        """
        Is the given item in the hash table?
        :return: True iff obj or its equivalent has been added to this table
        """
        if self.__position(item)!=None:
            return True
        else:
            return False

    def remove(self,item):
        """
        Remove an object from the hash table (and from the insertion order).
        Resize the table if its size has dropped below
        (1-load_factor)*current_size.
        :param item: the value to remove; assumes hashing and equality work
        :return: None
        """
        position=self.__position(item)
        if position!=None:
            if position is self.first:
                self.first=position.forwardLink
                if self.first!=None: #only One Element
                    self.first.backLink=None
            elif position is self.last:
                self.last=position.backLink
                if self.last!=None: #only one Element
                    self.last.forwardLink=None
            else:
                if position.backLink!=None:
                    position.backLink.forwardLink=position.forwardLink
                if position.forwardLink!=None:
                    position.forwardLink.backLink=position.backLink
            item=Data(item)
            hashCode=item.hashCode(self.lookup,self.capacity)
            if position is self.table[hashCode]:
                self.table[hashCode]=position.chainLink
            else:
                if position.backChain!=None:
                    position.backChain.chainLink=position.chainLink
            self.size-=1
            if .25>=float(self.size)/float(self.capacity):
                self._rehash(False)
        else:
            raise Exception("element does not exist")

    def local_iterator(self):
        """
        For Testing
        Created this method for internal testing of the iterator
        :return:None
        """
        for item in self:
            print(item)


    def __iter__( self ):
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
        anIterator=LinkedHashTable.Iter(self.first)
        return anIterator


    class Iter( Iterator ):
        """
        This class implements Iterator abstract class and provide
        implementation to __next__ method
        """
        __slots__ = "iterator"
        def __init__( self, iterator):
            """
            Get executed while creating object ot the Iter
            :param iterator: Initially points to the starting(First) node of Linked Hash map
            :return: None
            """
            self.iterator=iterator
        def __next__( self ):
            """
            Traverse through the Nodes of Linked Hashmap in the order of their insertion in Linked Hash map
            :return: value associated with node
            """
            if self.iterator==None:
                raise StopIteration()
            else:
                value=str(self.iterator.data)
                #print(value)
                self.iterator=self.iterator.forwardLink
                return value

def test():
    """
    For internal Testing of the Linked Hash table
    :return:
    """
    testing=LinkedHashTable(5)
    testing.add("sri")
    testing.add("pearl")
    testing.add("mayank")
    testing.add("anusha")
    testing.add("payal")
    testing.add("brain")
    testing.add("cathy")
    testing.add("emily")
    testing.add("nora")
    testing.add("mayank")
    testing.add("abby")
    testing.add("marbal")
    testing.add("dejoy")

    testing.local_iterator()

    print(testing.contains("sri"))
    print(testing.contains("dejoy"))
    print(testing.contains("cathy"))

    testing.remove("sri")
    print(testing.size)
    testing.local_iterator()
    #print(testing.size)
    testing.remove("dejoy")
    testing.local_iterator()
    print(testing.size)
    testing.remove("cathy")
    testing.local_iterator()
    print(testing.size)




