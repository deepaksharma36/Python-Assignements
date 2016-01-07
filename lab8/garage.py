__author__ = 'deepak ds5930'
__author__ = 'Mayank jainMJ2997'


class job:
    """
    This class takes a new job from the file and operates on it
    """
    __slots__='job_name', 'hours', 'cost', 'cathy_index', 'howard_index'

    def __init__(self, name, hours, cost, cathy_index, howard_index):
        """
        Constructor takes the values 'name', 'hours', 'cost', 'cathy_index' and 'howard_index'
        :param name: job name
        :param hours: number of hours taken for the given job
        :param cost: cost for that job
        :param cathy_index: location of the job in CathyHeap
        :param howard_index: location of job in HowardHeap
        :return: None
        """
        self.job_name = name
        self.hours = hours
        self.cost = cost
        self.cathy_index = cathy_index
        self.howard_index = howard_index

    def show(self):
        """
        To show the parameters of each job
        :return: string representation of each job
        """
        return str(self.job_name)+" " + str(self.hours) + " " + str(self.cost) + " "+str(self.cathy_index) + " " + str(self.howard_index)


class Heap:
    """
    Heap that orders by a given comparison function, default to less-than.
    """
    __slots__ = ('data','size','compFn','name','settleUp')

    def __init__(self,compFn,name,settleUp):
        """
        Constructortakes in a comparison function 'compfn', jobname 'name'
        :param compFn: comparison function for the heap
        :param name: job name
        :param settleUp: function for updating the indices of each job in a heap.
        :return: None
        """
        self.data = []
        self.size = 0
        self.compFn = compFn
        self.name=name
        self.settleUp=settleUp

    def __parent(self,loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return (loc-1)//2

    def __bubbleUp(self,loc):
        '''
        Starts from the given location and moves the item at that spot
        as far up the heap as necessary
        :param loc: Place to start bubbling from
        '''
        while loc > 0 and self.compFn(self.data[loc],self.data[self.__parent(loc)]):
            self.settleUp(self,loc,self.__parent(loc))
            (self.data[loc], self.data[self.__parent(loc)]) = (self.data[self.__parent(loc)], self.data[loc])
            loc = self.__parent(loc)

    def __bubbleDown(self,loc):
        '''
        Starts from the given location and moves the item at that spot
        as far down the heap as necessary
        :param loc: Place to start bubbling from
        '''
        swapLoc = self.__smallest(loc)
        while swapLoc != loc:
            self.settleUp(self,loc,swapLoc)
            (self.data[loc], self.data[swapLoc]) = (self.data[swapLoc], self.data[loc])
            loc = swapLoc
            swapLoc = self.__smallest(loc)

    def __smallest(self,loc):
        '''
        Finds the "smallest" value of loc and loc's two children.
        Correctly handles end-of-heap issues.
        :param loc: Index
        :return: index of smallest value
        '''
        ch1 = loc*2 + 1
        ch2 = loc*2 + 2
        if ch1 >= self.size:
            return loc
        if ch2 >= self.size:
            if self.compFn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        # now consider all 3
        if self.compFn(self.data[ch1],self.data[ch2]):
            if self.compFn(self.data[loc],self.data[ch1]):
                return loc
            else:
                return ch1
        else:
            if self.compFn(self.data[loc],self.data[ch2]):
                return loc
            else:
                return ch2


    def insert(self,item):
        '''
        Inserts an item into the heap.
        :param item: Item to be inserted
        '''
        self.data.append(item)
        self.size += 1
        self.__bubbleUp(self.size-1)

    def __pop(self, loc):
        '''
        Removes and returns the job at the location 'loc' of the heap
        :param: loc: removes the job at this position
        :return: Item on top of the heap
        '''
        retjob = self.data[loc]

        self.size -= 1
        # if we are popping the only element, assignment will fail,
        # but bubbling is unnecessary, so:
        if self.size >= 0:
            self.settleUp(self,loc,self.size)
            if loc<self.size:
                self.data[loc] = self.data.pop(self.size)
            else:
                self.data.pop(self.size)
            self.__bubbleDown(loc)
        return retjob

    def pop(self):
        '''
        Removes and returns top of the heap
        :return: Item on top of the heap
        '''
        return self.__pop(0)

    def delete(self,loc):
        '''
        Removes the job at the location 'loc' from the heap
        :param loc: position of the job that has to be removed
        :return:
        '''
        self.__pop(loc)

    def __len__(self):
        '''
        Defining the "length" of a data structure also allows it to be
        used as a boolean value!
        :return: size of heap
        '''
        return self.size


    def __str__(self):
        ret = ""
        for item in range(self.size):
            ret += str(self.data[item]) + " "
        return ret


def settleUp(heap,loc1,loc2):
    '''
    function to update the position of all the jobs after removing a job in the heap
    :param heap: heap that has to be updated
    :param loc1: position that needs to be updated
    :param loc2: position that needs to be updated and swapped with
    :return: None
    '''
    if heap.name=='Howard':
        heap.data[loc1].howard_index ,heap.data[loc2].howard_index = heap.data[loc2].howard_index ,heap.data[loc1].howard_index
    elif heap.name=='Cathy':
        heap.data[loc1].cathy_index ,heap.data[loc2].cathy_index = heap.data[loc2].cathy_index ,heap.data[loc1].cathy_index


def minCmp(n1, n2):
    '''
    Simple comparison function on hours. Assumes each name is (first, last) tuple
    :param n1: Name
    :param n2: Other name
    :return: True if n1 comes before n2
    '''
    return float(n1.hours) < float(n2.hours)


def maxCmp(n1, n2):
    '''
    Simple comparison function on cost. Assumes each name is (first, last) tuple
    :param n1: Name
    :param n2: Other name
    :return: True if n1 comes before n2
    '''
    return float(n1.cost) > float(n2.cost)


def main():
    '''
    this function reads in the files, splits it, build the heap and operates on it.
    :return: None
    '''

    HowardHeap=Heap(minCmp,'Howard',settleUp)
    CathyHeap=Heap(maxCmp,'Cathy',settleUp)

    filename = input('Enter filename: ')
    with open(filename) as f:
        for line in f:
            x = line.strip().split()
            if len(x)>0:
                if x[1] == 'ready':
                    if HowardHeap.size > 0 or HowardHeap.size > 0 :
                        if x[0] == "Howard" or x[0] == "howard":
                                current_job=HowardHeap.pop()
                                CathyHeap.delete(current_job.cathy_index)
                        elif x[0] in ["Cathy", "cathy"]:
                                current_job=CathyHeap.pop()
                                HowardHeap.delete(current_job.howard_index)
                        print(str(x[0]) + " starting job "+str(current_job.job_name))
                    else:
                        print("All jobs are done Nothing to do")
                else:
                    print("New job arriving! Job Name: " + str(x[0]) + ", " + str(x[1]) +".0 hours and $" + str(x[2]) +".0")
                    new_job=job(str(x[0]),str(x[1]),str(x[2]),CathyHeap.size,HowardHeap.size)
                    HowardHeap.insert(new_job)
                    CathyHeap.insert(new_job)


def show(heap):
    """
    To show the items in the heap
    :param heap: given heap name that is to be printed
    :return: None
    """
    for item in heap.data:
        print(item.show())


if __name__ == main():
    main()