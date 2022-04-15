import networkx as nx
import random
from algorithm import k_shortest, optimal_search

G = nx.Graph()                                     
city_list = ['Craiova', 'Drobeta', 'Pitesti', 'Valcea', 'Arad', 'Zerind', 'Timisoara', 'Oradea', 'Bucuresti', 'Giurgiu', 'Urziceni', 'Fagaras', 'Mehadia', 'Sibiu', 'Lugoj', 'Vaslui', 'Hirsova', 'Iasi', 'Neamt', 'Eforie']
#We add in the graph all the nodes from the Romanian map with their respective conexions and the weight of each road

G.add_edge('Craiova', 'Drobeta', weight=120)
G.add_edge('Craiova', 'Pitesti', weight=138)
G.add_edge('Craiova', 'Valcea', weight=146)
G.add_edge('Arad', 'Zerind', weight=75)
G.add_edge('Arad', 'Timisoara', weight=118)
G.add_edge('Oradea', 'Zerind', weight=71)
G.add_edge('Bucuresti', 'Giurgiu', weight=90)
G.add_edge('Bucuresti', 'Urziceni', weight=85)
G.add_edge('Bucuresti', 'Fagaras', weight=211)
G.add_edge('Drobeta', 'Mehadia', weight=75)
G.add_edge('Pitesti', 'Bucuresti', weight=101)
G.add_edge('Pitesti', 'Valcea', weight=97)
G.add_edge('Sibiu', 'Arad', weight=140)
G.add_edge('Sibiu', 'Oradea', weight=151)
G.add_edge('Sibiu', 'Fagaras', weight=99)
G.add_edge('Valcea', 'Sibiu', weight=80)
G.add_edge('Mehadia', 'Lugoj', weight=70)
G.add_edge('Lugoj', 'Timisoara', weight=111)
G.add_edge('Urziceni', 'Hirsova', weight=98)
G.add_edge('Urziceni', 'Vaslui', weight=142)
G.add_edge('Hirsova', 'Eforie', weight=86)
G.add_edge('Vaslui', 'Iasi', weight=92)
G.add_edge('Iasi', 'Neamt', weight=87)


random_city = random.choice(city_list)
C1 = random_city                                            #We choose randomly the city from where the first person starts
print("The first person starts from:", C1)

random_city = random.choice(city_list)
C2 = random_city                                            #We choose randomly the city from where the second person starts
print("The second person starts from:", C2)

time, distance, route = optimal_search(G, C1, C2)            #We use the search algorithm to determine the shortest route, time and distance
print("The minimum distance travelled is: ", distance)                   #that it will take for the two friends to meet, considering that they always meet 
print("The route taken by the first person is:", route)                  #at the middle of the distance
print("The time necessary for the first person to reach the goal state is: ", time)      