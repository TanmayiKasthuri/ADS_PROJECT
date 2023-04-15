import re as eg # Importing the module re
import sys as system

class min_heap:
    entries = []  # Creating a new list for storing data and assigning it to an attribute called "entries".

    def __init__(self):
        self.entries = []  # Creating an instance attribute "entries", setting it to an empty list in the constructor.

    def insert(self, entry): # for inserting into the heap
        self.entries.append(entry);  # Joining entry at the list end
        self.heapifyUp(len(self.entries) - 1);  # re-establishing the heap property

    def includes(self, entry): # to examine if the newly entered entry is already present in the heap
        if entry in self.entries:
            return True
        else:
            return False

    def minRetrieval(self): # Retrieving the minimum entry from the heap
        if (self.hasNoElements()):  # Verifying if the heap has any elements or not
            return None


        # Retrieving the minimum element and last element from the heap
        minimumElement = self.entries[0]
        lastElement = self.entries.pop()

        if (self.entries):
            self.entries[0] = lastElement
            self.heapifyDown(0)  # Re-establishing the heap property

        return minimumElement;

    def heapifyDown(self, position):
        findLeftChildIndex = position*2 + 1;  # Finding left child's index when index of particular node is given
        findRightChildIndex = position*2 + 2;  # Finding right child's index when index of particular node is given
        smallestIndex = position;

        if (len(self.entries)>findLeftChildIndex):  # Verify if there is a left child.
            getLeftChildRide = self.entries[findLeftChildIndex]  # Retrieve left child
            shortestRide = self.entries[smallestIndex]  # Retrieve the smallest element that is currently available.

            if (self.rankRideCosts(getLeftChildRide, shortestRide) < 0):  # Compare left child and shortest ride
                smallestIndex = findLeftChildIndex # Setting index of the smallest element as index of its left child.

        if (findRightChildIndex < len(self.entries)):  # Verify if there is a left child node.
            getRightChildRide = self.entries[findRightChildIndex]  # Retrieve right child
            shortestRide = self.entries[smallestIndex]  # Retrieve the smallest element that is currently available.

            if (self.rankRideCosts(getRightChildRide, shortestRide) < 0):  # Compare left child and shortest ride
                smallestIndex = findRightChildIndex  # Setting index of smallest element as index of its right child.

        if (smallestIndex != position):  # Swapping the minimum element and input element if they are unequal and
            # perform a recursive heapify down.
            self.swapValues(position, smallestIndex)
            self.heapifyDown(smallestIndex)

    def rankRideCosts(self, rideNumber1, rideNumber2):  # Comparing rides through cost and tripDuration
        if rideNumber1.getRideCost() < rideNumber2.getRideCost(): # If the cost of rideNo1>rideNo2 ,
            # initialize a variable to -1
            comparision = -1
        elif rideNumber1.getRideCost() > rideNumber2.getRideCost(): # If the cost of rideNo1<rideNo2 ,
            # initialize a variable to 1
            comparision = 1
        else:
            comparision = 0 # If the cost of rideNo1=rideNo2 , initialize a variable to 0
        if (comparision != 0): # If the variable to which values -1,0,1 are assigned != 0, then return the variable
            return comparision;
        else:
            if rideNumber1.getTripDuration() < rideNumber2.getTripDuration(): # If the TripDuration of rideNo1>rideNo2 ,
                # initialize a variable to -1
                return -1
            elif rideNumber1.getTripDuration() > rideNumber2.getTripDuration(): # If the TripDuration of rideNo1<rideNo2
                # , initialize a variable to 1
                return 1
            else: # Else, initialize the variable to 0
                return 0

    def hasNoElements(self): # Checking if the tree is empty
        return not bool(self.entries)

    def heapifyUp(self, position): # Re-establishing the heap property
        while (position > 0):
            try:
                parentIndex = ((position - 1) // 2)
                if self.entries[position].rideCost > self.entries[parentIndex].rideCost:
                    c = 1
                elif self.entries[position].rideCost < self.entries[parentIndex].rideCost:
                    c = -1
                else:
                    c = 0
                if (c > 0 or (c == 0 and (
                        self.entries[position].getTripDuration() >= self.entries[parentIndex].getTripDuration()))):
                    break
                self.swapValues(position, parentIndex)
                position = parentIndex
            except IndexError as e:
                print("Error: ", e)
                break

    def swapValues(self, a, b):  #swapping values
        self.entries[a], self.entries[b] = self.entries[b], self.entries[a]

    def compare(self, a, b): # compares two keys and returns -1 if the first key is less than the second,
        # 1 if the first key is greater than the second, and 0 if they are equal
        return (a > b) - (a < b)

    def remove(self, element):  # deleting entry from the heap
        try:
            position = 0
            k = 0
            while k < len(self.entries):
                if self.entries[k].rideNumber == element.rideNumber and self.entries[k].rideCost == element.rideCost and self.entries[k].tripDuration == element.tripDuration:
                    position = k
                    break
                k += 1
            else:
                raise ValueError("Element not found in heap")

            last = self.entries.pop()
            if (position != len(self.entries)):
                self.entries[position] = last
                if (self.compare(last.rideNumber, element.rideNumber) < 0):
                    self.heapifyDown(position)  # Re-establishing the heap property
                else:
                    self.heapifyUp(position)  # Re-establishing the heap property
            return True

        except ValueError as e:
            print(e)
            return False


from collections import deque # Importing deque data structure from the collections module

class RBTree:
    def __init__(self): # Initializing attributes of the objects
        self.RED = True
        self.BLACK = False

    class Node:
        def __init__(self, key, value, color, size): # Initializing attributes of the objects
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = color
            self.size = size

    root = Node(0, 0, 0, 0) # Initializing values of the objects to the root node as zeros

    def makingComparision(self, key1, key2): # Comparing 2 keys
        if key2 > key1: # if true, return -1
            return -1
        elif key2 < key1: # if true, return 1
            return 1
        else: # return 0 if the code does pass through the blocks of the above selection operations
            return 0

    def get(self, key):
        x = self.root
        while (x != None):
            if key < x.key:
                c = -1
            elif key > x.key:
                c = 1
            else:
                c = 0
            if (c < 0):
                x = x.left; # travelling left
            elif (c > 0):
                x = x.right; # travelling right
            else:
                return x.value;

        return None

    def includesKey(self, key): # Checking if a key is present
        return self.get(key) != None

    def puti(self, x, key, value):
        if (x == None):
            return self.Node(key, value, self.RED, 1)

        if x.key < key:
            c = 1
        elif x.key > key:
            c = -1
        else:
            c = 0
        if (c > 0):
            x.right = self.puti(x.right, key, value)
        elif (c < 0):
            x.left = self.puti(x.left, key, value)
        else:
            x.value = value

        if (self.isNodeRed(x.left) and self.isNodeRed(x.left.left)): # when LL rotation
            x = self.rightRotation(x)

        if (self.isNodeRed(x.left) and self.isNodeRed(x.right)): # when LR rotation
            self.colorChange(x)

        if (self.isNodeRed(x.right) and not self.isNodeRed(x.left)): # when RL rotation
            x = self.leftRotation(x)


        x.size = 1 + self.capacity(x.left) + self.capacity(x.right)
        return x

    def put(self, key, value):
        try:
            self.root = self.puti(self.root, key, value)
            self.root.color = self.BLACK  # by RB tree rule, root node is always black
        except Exception as e:
            print(f"Error: {e}")

    def remove(self, key):
        if (not self.includesKey(key)):
            return;

        if (not self.isNodeRed(self.root.right) and not self.isNodeRed(self.root.left)):
            self.root.color = self.RED;

        self.root = self.removee(self.root, key);
        if (not self.hasNoElements()):
            self.root.color = self.BLACK

    def removee(self, x, key):
        if x.key > key:
            if (not self.isNodeRed(x.left.left) and not self.isNodeRed(x.left)):
                x = self.movingRedToLeft(x)

            x.left = self.removee(x.left, key)
        else:
            if (self.isNodeRed(x.left)):
                x = self.rightRotation(x)

            if (x.right == None and key == x.key):
                return None

            if (not self.isNodeRed(x.right.left) and not self.isNodeRed(x.right) ):
                x = self.movingRedToRight(x)

            if key == x.key:
                t = self.minimal(x.right)
                x.key = t.key
                x.value = t.value
                x.right = self.removeMin(x.right)
            else:
                x.right = self.removee(x.right, key)
        return self.stabilize(x)

    def maximal(self): # Searching for the maximal element in the tree
        return self.maximal(self.root)

    def maximal(self, x): # Searching for maximal element in the tree
        if (x == None):
            return None
        if (x.right == None):
            return x
        return self.maximal(x.right)

    def minimal(self):
        return self.minimal(self.root);

    def minimal(self, x):
        if (x.left == None):
            return x;
        else:
            return self.minimal(x.left)


    def capacity(self):
        return self.capacity(self.root)

    def capacity(self, x):  # Counting nodes
        if x is None:
            return 0
        try:
            return x.size
        except AttributeError:
            raise TypeError("The given node does not have a 'size' attribute.")

    def hasNoElements(self): # Checking if the tree is empty
        return self.root == None

    def isNodeRed(self, x): # Checking if the color of the node is red
        if (x == None):
            return False

        return x.color == self.RED;

    def leftRotation(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        y.color = x.color
        x.color = self.RED
        y.size = x.size
        x.size = 1 + self.capacity(x.left) + self.capacity(x.right)
        return y

    def rightRotation(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        y.color = x.color
        x.color = self.RED
        y.size = x.size
        x.size = 1 + self.capacity(x.left) + self.capacity(x.right)
        return y

    def colorChange(self, x):  # Flipping the colors
        try:
            x.left.color = not x.left.color
            x.right.color = not x.right.color
            x.color = not x.color
        except AttributeError as e:
            print(f"An AttributeError occurred: {e}")

    def movingRedToLeft(self, x):
        self.colorChange(x)
        if (self.isNodeRed(x.right.left)):
            x.right = self.rightRotation(x.right)
            x = self.leftRotation(x)
            self.colorChange(x)
        return x

    def movingRedToRight(self, x):
        self.colorChange(x)
        if (self.isNodeRed(x.left.left)):
            x = self.rightRotation(x)
            self.colorChange(x)
        return x

    def removeMin(self, x):
        if (x.left == None):
            return None
        if (not self.isNodeRed(x.left.left) and not self.isNodeRed(x.left)):
            x = self.movingRedToLeft(x)
        x.left = self.removeMin(x.left)
        return self.stabilize(x)

    def stabilize(self, x):  # Balancing RBT with rotations and color changes
        if (self.isNodeRed(x.right)):
            x = self.leftRotation(x)

        if (self.isNodeRed(x.left) and self.isNodeRed(x.left.left)):
            x = self.rightRotation(x)

        if (self.isNodeRed(x.left) and self.isNodeRed(x.right)):
            self.colorChange(x)

        x.size = 1 + self.capacity(x.left) + self.capacity(x.right);
        return x

    def data(self):
        return self.data(self.maximal().key, self.minimal().key)

    def data(self, high, low):
        queue = deque();
        queue = self.data(self.root, high, low, queue);
        return queue;

    def data(self, x,high, low, queue):
        if (x == None):
            return

        cmplow = self.makingComparision(low, x.key)
        cmphigh = self.makingComparision(high, x.key)
        if (cmplow < 0):
            queue = self.data(x.left, high, low, queue)

        if (cmplow <= 0 and cmphigh >= 0):
            queue = queue.add(x.key)

        if (cmphigh > 0):
            queue = self.data(x.right, high, low, queue)
        return queue

    def subMap(self, fromKey, toKey):
        if  (fromKey == toKey) or (fromKey < toKey):
            subMap = {}
            subMap = self.subMapHelpFunction(self.root, subMap, fromKey, toKey);
            return subMap

    def subMapHelpFunction(self, x, subMap, fromKey, toKey):

        try:
            if (x == None):
                return
            compareFrom = self.makingComparision(x.key, fromKey);
            compareTo = self.makingComparision(x.key, toKey);

            if (compareFrom < 0):
                k = self.subMapHelpFunction(x.right, subMap, fromKey, toKey)
                if k != None:
                    subMap.update(k)
            elif (compareTo >= 0):
                k = self.subMapHelpFunction(x.left, subMap, fromKey, toKey)
                if k != None:
                    subMap.update(k)
            else:
                k = self.subMapHelpFunction(x.left, subMap, fromKey, toKey)
                if k != None:
                    subMap.update(k)
                if not subMap:
                    subMap = {x.key: x.value}
                else:
                    subMap.update({x.key: x.value})
                k = self.subMapHelpFunction(x.right, subMap, fromKey, toKey)
                if k != None:
                    subMap.update(k)
            return subMap
        except Exception as e:
            print(f"An exception occurred: {e}")


class GatorTaxi:
    duplicateridenumber = False
    counter_rideNumber = 0  # Assigning a counter in order to monitor of the number of rides.

    # Iniializing min heap and red-black tree
    def __init__(self, sortedRideQueue, rideTree):
        self.sortedRideQueue = sortedRideQueue  # Arranging the rides in ascending order of cost using min heap
        self.rideTree = rideTree  # Sorting rides with ride numbers using RBT

    class Ride:
        # Initializing ride number, ride cost and trip duration
        rideNumber = 0
        rideCost = 0
        tripDuration = 0

        def __init__(self, rideNumber, rideCost, tripDuration):

            self.rideCost = rideCost;
            self.rideNumber = rideNumber;
            self.tripDuration = tripDuration;

        def getRideCost(self):
            return self.rideCost

        def getTripDuration(self):
            return self.tripDuration

    def Print(self, rideNumber1, rideNumber2=None):  # Printing ride detail for which rideNumber1 <= rx <= rideNumber2
        # Note: if ride2 details not given,print the details of only 1st ride mentioned.
        if rideNumber2 == None:
            ride = self.rideTree.get(rideNumber1)
            if (ride != None):
                return "(" + str(ride.rideNumber) + ", " + str(ride.rideCost) + ", " + str(ride.tripDuration) + ")"
            else:
                return "(0, 0, 0)"
        else:
            if (self.rideTree == None or len(self.rideTree.subMap(rideNumber1, rideNumber2 + 1)) == 0):
                return "(0, 0, 0)"
            else:
                is_first = True;
                kmap = self.rideTree.subMap(rideNumber1, rideNumber2 + 1)
                outcome = []
                i = 0
                while i < len(kmap):  # Looping over each entry in the 'kmap' dictionary.
                    entry = list(kmap.keys())[i]
                    k = ''
                    ride = kmap[entry]  # Getting 'ride' object from the 'Kmap' dictionary using current 'entry' key.
                    k = "(" + str(ride.rideNumber) + ", " + str(ride.rideCost) + ", " + str(ride.tripDuration) + ")"
                    is_first = False
                    outcome.append(k)  # Appending the attained ride details to the list "outcome"
                    i += 1
                return outcome

    def Insert(self, rideNumber, rideCost, tripDuration):
        # Code block to insert a new ride

        if (self.sortedRideQueue.includes(self.Ride(rideNumber, 0, 0)) or self.rideTree.includesKey(rideNumber)):
            return ("Duplicate RideNumber")
        if (self.counter_rideNumber == 2000): # when number of rides exceed
            return "No more rides can be added as the maximum number of active rides reached"

        ride = self.Ride(rideNumber, rideCost, tripDuration)
        self.sortedRideQueue.insert(ride)
        self.rideTree.put(rideNumber, ride)
        self.counter_rideNumber = self.counter_rideNumber + 1
        return None

    def GetNextRide(self):  # Retrieve ride with minimum due from min_heap and delete it from RBT

        ride = self.sortedRideQueue.minRetrieval()  # Retrieving min cost ride
        if (ride != None):
            self.rideTree.remove(ride.rideNumber)  # Deleting the ride
            self.counter_rideNumber -= 1  # Updating the number of rides still need to be taken up
            return "(" + str(ride.rideNumber) + ", " + str(ride.rideCost) + ", " + str(ride.tripDuration) + ")"
        else:
            return "No active ride requests"


    def CancelRide(self, rideNumber):  # Removing a particular ride
        ride = self.rideTree.get(rideNumber)  # Retrieving ride
        if (ride != None):
            self.rideTree.remove(rideNumber)  # Deleting ride
            self.counter_rideNumber -= 1  # Updating number of rides yet to be taken up
            self.sortedRideQueue.remove(ride)  # Deleting ride from heap
            newSortedRideQueue = min_heap()

            while True:
                if self.sortedRideQueue.hasNoElements():
                    break
                newSortedRideQueue.insert(self.sortedRideQueue.minRetrieval())
            self.sortedRideQueue = newSortedRideQueue;

    def UpdateTrip(self, rideNumber, new_TripDuration):  # Updating trip duration, given: ride number
        ride = self.rideTree.get(rideNumber)  # get the ride with the given ride number from the red-black tree
        if (new_TripDuration > 0 and ride != None):
            existing_TripDuration = ride.tripDuration  # get the existing duration of the trip for the ride
            # If new duration < current one, updating the trip duration with new one and increasing cost by 10 units
            if (existing_TripDuration >= new_TripDuration):
                ride.tripDuration = new_TripDuration;
                self.sortedRideQueue.remove(ride)
                self.rideTree.remove(rideNumber)
                self.sortedRideQueue.insert(ride)
                self.rideTree.put(rideNumber, ride);
            # If new duration is twice as greater than existing one or more, cancel the trip
            elif (2 * existing_TripDuration >= new_TripDuration):
                newRideCost = ride.rideCost + 10
                self.sortedRideQueue.remove(ride);
                self.rideTree.remove(rideNumber);
                self.Insert(rideNumber, newRideCost, new_TripDuration);
            else:
                self.sortedRideQueue.remove(ride)
                self.rideTree.remove(rideNumber)
        else:
            return ("Invalid new_TripDuration")


sortedRideQueue = min_heap()
rideTree = RBTree()
g = GatorTaxi(sortedRideQueue, rideTree)


def StringToNumber(stri): # Extracting numbers from strings
    arr = eg.findall(r'[0-9]+', stri)
    return arr

fil=system.argv[1]
mainSolution = open(fil)  # Opening the input file
results = []  # Initializing list "results"
stri = mainSolution.readline()  # Read the first line of the file

while stri:
    if eg.search("^Insert(.*)$", stri):  # Identifying insert operations from input file
        arr = StringToNumber(stri)
        if g.Insert(int(arr[0]), int(arr[1]), int(arr[2])) == "Duplicate RideNumber":
            k = "Duplicate RideNumber"
            results.append(k)
            break
    elif eg.search("^GetNextRide(.*)$", stri):  # Identifying getNextRide operations from input file
        k = g.GetNextRide()
        results.append(k)

    elif eg.search("^Print(.*)$", stri):  # Identifying print operations from input file
        arr = StringToNumber(stri)
        if len(arr) == 1:
            k = g.Print(int(arr[0]))
            results.append(k)
        elif len(arr) == 2:
            k = g.Print(int(arr[0]), int(arr[1]))
            results.append(k)
    elif eg.search("^CancelRide(.*)$", stri):  # Identifying cancel operations from input file
        arr = StringToNumber(stri)
        g.CancelRide(int(arr[0]))
    elif eg.search("^UpdateTrip(.*)$", stri):  # Identifying update operations from input file
        arr = StringToNumber(stri)
        updation = g.UpdateTrip(int(arr[0]), int(arr[1]))
        if updation != None:
            results.append(updation)
    else:
        print("Ivalid input")
    stri = mainSolution.readline()  # Read the next line of the file


# Creating and writing output to the output file
with open("output_file.txt", 'w') as the_file:
    count = 0
    while count < len(results):
        r = results[count]
        if isinstance(r, str):
            the_file.write(r + "\n")
        else:
            the_file.write(",".join(r) + "\n")
        count += 1





















    #   class GatorTaxi:
    #                   counter_rideNumber=0  #Assigning a counter in order to monitor of the number of rides.
    #                   duplicateridenumber=False

    #                   def__init__(self,sortedRideQueue,rideTree):
    #                   self.rideTree=rideTree  #min heap data structure to keep rides with min cost at the top
    #                   self.sortedRideQueue=sortedRideQueue  #RBTree data structure to keep rides sorted through
    #                   parameter as ride number

    #                   class Ride:
    #                       def __init__(self,rideNumber,rideCost,tripDuration)

    #                       def getRideCost(self):

    #                       def getTripDuration(self):

    #                   def Print(self,rideNumber1,rideNumber2=None)  #Printing ride detail for which
    #                   rideNumber1 <= rx <= rideNumber2
    #                   Note: if ride2 details not given,print the details of only 1st ride mentioned.

    #                   def Insert(self,rideNumber,rideCost,tripDuration)  #Code block to insert a new ride

    #                   def GetNextRide(self)  #Retrieve ride with minimum due from min_heap and delete it from RBT

    #                   def CancelRide(self,rideNumber)  #Removing a particular ride

    #                   def UpdateTrip(self,rideNumber,new_TripDuration)  #Updating trip duration, given: ride number
