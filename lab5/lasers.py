__author__ = 'Mayank Jain mj2997'
__author__ = 'Deepak Sharma ds5930'


def main():
    """
    This function prompts for the file name from the user converts it into the
    list of lists and then performs the logic for given problem.
    :param: None
    :return: None
    """

    list = []
    ScoreLocations = {}
    eligible_orientations=["left", "right", "up", "down"]
    filename = input('Enter filename: ')
    with open(filename) as f:
        for line in f:
            x = line.strip().split()
            list.append(x)
    lasernum = int(input("Enter the number of lasers"))
    # If the user enters a number greater than the potential laser positions
    # the programs displays the message and aks to input the number again unless
    # the value is valid.
    while lasernum > (len(list)**2)-4:
        print("Number of lasers out of bound")
        lasernum = int(input("Enter the number of lasers"))

    # Here we generate all the possible laser positions for a given square grid
    # and check for the orientations with maximum sum as per the problem.
    for i in range(len(list)):
            for j in range(len(list[i])):
                if i-1 < 0:
                    eligible_orientations.remove("up")
                if j-1 < 0:
                    eligible_orientations.remove("left")
                if j+1 >= len(list[i]):
                    eligible_orientations.remove("right")
                if i+1 >= len(list):
                    eligible_orientations.remove("down")
                (left, right, up, down) = neighbour_check(eligible_orientations, i, j, list)

                Score = -float('Inf')
                orientation = None
                (Score, change) = ScoreCalculator(left, right, up, Score)
                if change == True:
                    orientation = "UP"
                (Score, change) = ScoreCalculator(left, right, down, Score)
                if change == True:
                    orientation = "DOWN"
                (Score, change) = ScoreCalculator(down, right,up,Score)
                if change == True:
                    orientation = "RIGHT"
                (Score, change) = ScoreCalculator(up,left,down,Score)
                if change == True:
                    orientation = "LEFT"

                # a dictionary 'ScoreLocations' is made here with keys as 'Score' and
                # values being a tuple as '(i, j, orientation)'
                if Score not in ScoreLocations.keys() and orientation != None:
                    ScoreLocations[Score] = [(i, j, orientation)]
                elif orientation != None:
                    ScoreLocations[Score].append((i, j, orientation))
                eligible_orientations = ["left", "right", "up", "down"]

    SortedListOfScores = [int(keys) for keys in ScoreLocations.keys()]
    bestLocations = []
    for _ in range(lasernum):
        bestLocations += (ScoreLocations[max(SortedListOfScores)])
        SortedListOfScores.remove(max(SortedListOfScores))
        if len(bestLocations) >= lasernum:
            break

    for location in range(lasernum):
        print("(" + str(bestLocations[location][0]) + "," + str(bestLocations[location][1]) + ") " + "facing " + str(bestLocations[location][2]))

        #l=(sorted(ScoreLocations.values()))
        #for i in l[len(l)-lasernum:]:
        #for x in ScoreLocations.keys():
        #if i == ScoreLocations[x]:
        #print(str(x[0])+","+str(x[1])+" facing "+str(x[2]))


def neighbour_check(eligible_orientations, i, j, list):
    """
    This function checks for the valid orientations if present and assigns the variables
    'left', 'right', 'up' and  'down' the values for it from the grid as per the position.
    :param: eligible_orientations - orientations that are valid for the given orientations.
            i,j - coordinates for the given grid position
            list - list that contains a list and represents a square grid.
    :return: left, right, up, down - the variables that has the values for the neighbouring
             positions for each orientation at each position.
    """
    left = -float('Inf')
    right = -float('Inf')
    up = -float('Inf')
    down = -float('Inf')
    for item in eligible_orientations:
        if item == "left":
            left = int(list[i][j-1])
        if item == "right":
            right = int(list[i][j+1])
        if item == "up":
            up = int(list[i-1][j])
        if item == "down":
            down = int(list[i+1][j])
    return left, right, up, down


def ScoreCalculator(dir1, dir2, dir3, Score):
    """
    This function calculates the sum for each orientation at every position and
    assigns the maximum of those to the variable Score for each position.
    :param: dir1, dir2, dir3 - the three neighbouring positions for a particular
            position that forms a particular orientation.
            Score - sum of all the values from these three positions for a particular
            orientation
    :return: Score - maximum sum for the given laser placement among all possible orientations
             change - boolean value variable that returns True when the value of Score gets changed
    """
    change = False
    if dir1 != None and dir2 != None and dir3 != None:
        if Score == None:
            Score = dir1+dir2+dir3
            change = True
        elif Score < dir1+dir2+dir3:
            Score = dir1+dir2+dir3
            change = True
    return Score, change

main()