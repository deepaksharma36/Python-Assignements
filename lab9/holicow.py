__author__ = 'deepak sharma ds5930'
__author__ = 'mayank jain mj2997'
import math
import sys
class cow_paintball_vertex:
    """
    This Class represent a vertex in the graph, this nod can be of two tye either cow or paintball
    """
    __slots__='ver_name','neighbours','ver_type'
    def __init__(self,ver_name,ver_type):
        """
        constructor for initalization the below parameters of the vertex
        :param ver_name: name of the node
        :param ver_type: type of the node
        :return:none
        """
        self.ver_name=ver_name
        self.ver_type=ver_type
        self.neighbours=[]
    def __str__(self):
        return self.ver_name

def isInRange(x1,y1,x2,y2,d):
    """
    calculates distance between two input coordinates
    :param x1: x coordinate of the first point
    :param y1: y coordinate of the first point
    :param x2: x coordinate of the second point
    :param y2: y coordinate of the second point
    :param d:  distance between the points
    :return: boolean value True if the distance between two input points less then or equal to input distance else false
    """
    if math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))<=d:
        return True
    else:
        return False

def find_neighbours(node,filename,graph,x1,y1,r):
    """
    find all neighbours for input paintball type vertex in graph and store in graph
    :param node:  vertex for which we are looking neighbours
    :param filename: input text file
    :param graph: graph representation of the graph
    :param x1: x coordinate or input vertex
    :param y1: y coordinate of input vertex
    :param r: radius for the input vertex
    :return: none
    """
    with open(filename) as cow_color_file:
        for line in cow_color_file:
            entry =line.split()
            if entry[1] not in graph:
                   graph[entry[1]]=cow_paintball_vertex(entry[1],entry[0])
            if(node!=entry[1] and   isInRange(x1,y1,float(entry[2]),float(entry[3]),r)):
                    graph[node].neighbours.append(graph[entry[1]])


def simulation(graph,simulation_result,start_vertex,current_vertex,exploring):
    """
    Execute simulation for each paintball type vertex present in graph
    :param graph: input graph
    :param simulation_result: store the result in simulation_result variable, a dictionary of dictionary
                              with key value or starting_vertex and value storing dictionary containing keys
                              as cows and values as colors attached to the cow.
    :param start_vertex: the first vertex with was triggered
    :param current_vertex: vertex triggered by other vertex
    :param exploring: list list of vertex which are triggered for an simulation
    :return: none
    """

    for neighbour in graph[current_vertex].neighbours:
        if neighbour.ver_type=="cow":
            print("     "+str(neighbour.ver_name)+" is painted "+str(current_vertex))
            if neighbour.ver_name not in simulation_result[graph[start_vertex].ver_name]:
                simulation_result[start_vertex][neighbour.ver_name]=[current_vertex] #new list creation
            else:
                simulation_result[graph[start_vertex].ver_name][neighbour.ver_name].append(current_vertex)
        elif neighbour.ver_name not in exploring:
                print("     "+str(neighbour.ver_name)+" paint ball triggered by "+str(current_vertex))
                exploring.append(neighbour.ver_name)
                simulation(graph,simulation_result,start_vertex,neighbour.ver_name,exploring)


def start_simulation(graph,simulation_result):
    """
    This method executed simulation on all paintball type vertex one by one
    :param graph: input graph
    :param simulation_result: store result after executing simulation -- a dictionary of dictionary
                              with key value or starting_vertex and value storing dictionary containing keys
                              as cows and values as colors attached to the cow.
    :return:none
    """
    for start_vertex in graph:
        exploring=[graph[start_vertex].ver_name]
        if graph[start_vertex].ver_type=="paintball":
            if graph[start_vertex].ver_name not in simulation_result:
                simulation_result[graph[start_vertex].ver_name]={}
                #print(simulation_result)
                print("Triggering "+str(start_vertex)+" paint ball")
                simulation(graph,simulation_result,start_vertex,graph[start_vertex].ver_name,exploring)

def show(cow_Graph):
    """
    show graph as per the the instructions given in assignment
    :param cow_Graph: input graph
    :return:none
    """
    for vertex in cow_Graph:
        output=[]
        print(str(vertex)+" connectedTo:" ,end=' ')
        for item in cow_Graph[vertex].neighbours:
            #print(item,end=',')
            output.append(item.ver_name)
        print(str(output))
    print("\n")
def show_result(result):
    """
    show result after triggering various node as instructed in assignment
    :param result: input dictionary store cow as keys and respective color as value
    :return:none
    """
    for cow in result:
        print("     " +str(cow)+"'s colors: ",end="")
        output="{ "
        for color in result[cow]:
            output=output+"'"+str(color)+"' ,"
        output=output[:len(output)-1]+"}"
        print(output)

def result(simulation_result):
    """
    this method figure out after all simulation by triggering with color maximum cows get painted
    :param simulation_result: a dictionary of dictionary
                              with key value of triggered vertex and value storing dictionary containing keys
                              as cows and values as colors attached to the cow.
    :return:  list of the color which color maximum number of cows and dictionary with keys as cows and values as number
             of cows they paint.
    """
    result_table={}
    for color in simulation_result:
        count=0
        for cow in simulation_result[color]:
            count=count+len(simulation_result[color][cow])
        result_table[color]=count
    final_keys=[key for key in result_table if result_table[key]== max(result_table.values())]
    return  final_keys, result_table
def non_colored_cow_insertion(simulation_cow_result,graph):
    """
    :param simulation_cow_result: insert cows with no color in final output
    :param graph: input graph
    :return: updated result with cows with no color
    """
    for item in graph:
        if graph[item].ver_type=="cow":
            if graph[item].ver_name not in simulation_cow_result:
                simulation_cow_result[graph[item].ver_name]=[]
    return simulation_cow_result

def main():
    """
    this method read input file line by line for creating graph from input text file
    execute various method for performing below tasks:
    show graph
    simulate all possible triggering simulations
    calculates results for figure out by triggering which color maximum cows get painted
    :return:none
    """
    cow_Graph={}
    try:
        filename=sys.argv[1]
    except IndexError:
        print("usage: python3 holicow.py {filename}")
        return
    #filename = input('Enter filename: ')
    try:
        with open(filename) as cow_color_file:
            for line in cow_color_file:
                entry =line.split()
                if entry[1] not in cow_Graph:
                        cow_Graph[entry[1]]=cow_paintball_vertex(entry[1],entry[0])
                if entry[0] == 'paintball':
                        find_neighbours(entry[1],filename,cow_Graph,float(entry[2]),float(entry[3]),float(entry[4]))
    except FileNotFoundError:
        print("File not found: "+ filename)
        return
    show(cow_Graph)
    simulation_result={}
    start_simulation(cow_Graph,simulation_result)
    colors,result_calculated=result(simulation_result)
    print("\nResults")
    if len(colors)==0:
        print("No cows were painted by any starting paint ball!")
    else:
        for key in colors:
            if result_calculated[key]>0:
                print("Triggering the "+str(key)+ " paint ball is the best choice with "+str(result_calculated[key]) +" total paint on the cow")
                final_result=non_colored_cow_insertion(simulation_result[key],cow_Graph)
                show_result(final_result)
                break #break can commented for checking all  tie cases
            else:
                print("No cows were painted by any starting paint ball!")
                break
if __name__ == main():
    main()
