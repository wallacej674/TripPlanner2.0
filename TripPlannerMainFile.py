#This is the part that has the template of what to do. So I will type this out into a format that works for python.
#Also, I will add a pytesting platform so that you get used to knowing how testing works in python. People usually do it two of the following ways: a. through using unit testing or b. Using pytest which allows for an easy way of testing as well. Testing is a very important part of documentation and helps in finding errors. Every function you write must be tested No excuses.

#the libraries that will be used:
from typing import NamedTuple, Tuple, Any

from abc import ABC, abstractmethod


"""
# Final project: Trip Planner

import cons

### Basic Types ###

#  - Latitudes and longitudes are numbers:
let Lat?  = num?
let Lon?  = num?

#  - Point-of-interest categories and names are strings:
let Cat?  = str?
let Name? = str?

### Raw Item Types ###

#  - Raw positions are 2-element vectors with a latitude and a longitude
let RawPos? = TupC[Lat?, Lon?]

#  - Raw road segments are 4-element vectors with the latitude and
#    longitude of their first endpoint, then the latitude and longitude
#    of their second endpoint
let RawSeg? = TupC[Lat?, Lon?, Lat?, Lon?]

#  - Raw points-of-interest are 4-element vectors with a latitude, a
#    longitude, a point-of-interest category, and a name
let RawPOI? = TupC[Lat?, Lon?, Cat?, Name?]

### Contract Helpers ###

# ListC[T] is a list of `T`s (linear time):
let ListC = Cons.ListC
# List of unspecified element type (constant time):
let List? = Cons.list?


interface TRIP_PLANNER:

    # Returns the positions of all the points-of-interest that belong to
    # the given category.
    def locate_all(
            self,
            dst_cat:  Cat?           # point-of-interest category
        )   ->        ListC[RawPos?] # positions of the POIs

    # Returns the shortest route, if any, from the given source position
    # to the point-of-interest with the given name.
    def plan_route(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_name: Name?          # name of goal
        )   ->        ListC[RawPos?] # path to goal

    # Finds no more than `n` points-of-interest of the given category
    # nearest to the source position.
    def find_nearby(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_cat:  Cat?,          # point-of-interest category
            n:        nat?           # maximum number of results
        )   ->        ListC[RawPOI?] # list of nearby POIs


class TripPlanner (TRIP_PLANNER):
    pass
#   ^ YOUR WORK GOES HERE


def my_first_example():
    return TripPlanner([[0,0, 0,1], [0,0, 1,0]],
                       [[0,0, "bar", "The Empty Bottle"],
                        [0,1, "food", "Pierogi"]])

test 'My first locate_all test':
    assert my_first_example().locate_all("food") == \
        cons([0,1], None)

test 'My first plan_route test':
   assert my_first_example().plan_route(0, 0, "Pierogi") == \
       cons([0,0], cons([0,1], None))

test 'My first find_nearby test':
    assert my_first_example().find_nearby(0, 0, "food", 1) == \
        cons([0,1, "food", "Pierogi"], None)

"""
### Basic Types ###

#  - Latitudes and longitudes are numbers:
Lat  = float
Lon  = float

#  - Point-of-interest categories and names are strings:
Cat  = str
Name = str

### Raw Item Types ###

#  - Raw positions are 2-element vectors with a latitude and a longitude
RawPos = Tuple[Lat, Lon]

#  - Raw road segments are 4-element vectors with the latitude and
#    longitude of their first endpoint, then the latitude and longitude
#    of their second endpoint
RawSeg = Tuple[Lat, Lon, Lat, Lon]

#  - Raw points-of-interest are 4-element vectors with a latitude, a
#    longitude, a point-of-interest category, and a name
RawPOI = Tuple[Lat, Lon, Cat, Name]

### Contract Helpers ###
ListC = [] #this is a list of 'T's (linear time): a regular list.

# List of unspecified element type (constant time):
List = lambda x: isInstance(List)


# The actual interface for creating a triplanner class
class TripPlanner(ABC):

    #self, dst_cat all that belong to the category -> listC
    def locate_all(self, dst_cat):
        #to located all of the categories
        #locate-all Takes a point-of-interest category; returns the positions of all pointsof-interest in the given category. The positions can returned be in any order you want, but the result should not include duplicates.
        pass
    
    #self, staring lat, starting lon, name of goal -> ListC
    def plan_route(self, src_lat, src_lon, dst_name):
        # Returns the shortest route, if any, from the given source position
        # to the point-of-interest with the given name.
        #if you need more information refer to the project file.
        pass
    
    #self, starting lat, starting lon, destination category, natural number(for the amount of destinations you want) -> ListC  
    def find_nearby(self, src_lat, src_lon, dst_cat, num):
        # Finds no more than `n` points-of-interest of the given category
        # nearest to the source position.
        # if you need more information refer to the project file.
        pass


# type of ADT we will be using for this project is Weighted graph. It would probably be the easiest to implement. In the future we could do other types of ADTs, but for now this is the ADT we will be working with.
#the next step would be to make a solid impletmentation of a weighted undirected graph in this project. I do not think it will be that much of a challenge for us. Also, I do have some pseudo code for us to reference and the functions that would need to be created for the graph.

#let Vertex? = nat?
#let VertexList? = Cons.ListC[Vertex?]
#let Weight? = AndC(num?, NotC(OrC(inf, -inf, nan)))
#let OptWeight? = OrC(Weight?, NoneC)
#struct WEdge:
#let u: Vertex?
#let v: Vertex?
#let w: Weight?
#let WEdgeList? = Cons.ListC[WEdge?]
#interface WUGRAPH:
#def len(self) -> nat?
#def set_edge(self, u: Vertex?, v: Vertex?, w: OptWeight?) -> NoneC
#def get_edge(self, u: Vertex?, v: Vertex?) -> OptWeight?
#def get_adjacent(self, v: Vertex?) -> VertexList?
#def get_all_edges(self) -> WEdgeList?
#class WUGraph (WUGRAPH):
#def __init__(self, size: nat?)
#def sort_vertices(lst: Cons.list?) -> Cons.list?:
#def sort_edges(lst: Cons.list?) -> Cons.list?:
#def dfs(graph: WUGRAPH!, start: Vertex?, f: FunC[Vertex?, AnyC]) -> NoneC
#def dfs_to_list(graph: WUGRAPH!, start: Vertex?) -> VertexList?

#the code above is in the form of DSSL2. Try and convert the code to Python is the next step.

isVertex = lambda x :  True if x >= 0 else False
isVertexList = lambda x: True if isinstance(x, List) else False
isWeight = lambda x: True if isinstance(x, int) and not None else False
isOptWeight = lambda x: True if isWeight(x) or None else False

#there is a lot that cannot be done in python. For example, Structs do not exist in Python. I wish that I could make a struct in python.

#contains 4 sets of data u : vertex, v : vertex, w : weight, WEdgeList : Weighted Edge List that contains a list of all the edges that are connected by this weighted edge.

#the structure of a weighted edge
class WEdge():
    def __init__(self, u, v, w, WEdgeList):
        self.u = u
        self.v = v
        self.w = w
        WEdgeList = self.WedgeList

#the interface for a weighted edge
class WUGRAPH(ABC):
    #self -> Natural Number
    #check the length of the WUGraph
    def len(self):
        pass

    #self, vertex, vertex, weight -> None
    #mutate the value of an edge into existence
    def set_edge(self, u, v, w):
        pass

    #self, u, v -> optweight
    #returns the weight associated with this vertex
    def get_edge(self, u, v):
        pass

    #self v -> VertexList
    #returns all adjacent vertexes based on the given vertex.
    def get_adjacent(self, v):
        pass

    #self -> WEdgeList
    #returns all of the weighted edges found in the graph
    def get_all_edges(self):
        pass
#the class for a weighted graph
class WUGraph(WUGRAPH):

    def __init__(self, size):
        pass

    def sort_vertices(lst):
        pass
    
    #def dfs(graph: WUGRAPH!, start: Vertex?, f: FunC[Vertex?, AnyC]) -> NoneC
    #WUGRAPH, start: vertex?, (FunC[Vertex?, AnyC]) -> None
    def dfs(graph, start, function):
        pass

    #sorts all the edges in a graph
    def sort_edges(lst):
        pass
    
    #makes a dfs list of the vertexes.
    def dfs_to_list(graph, start):
        pass











