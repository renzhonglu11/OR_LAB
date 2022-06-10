from unittest import result
from Aufgabe_1 import HCP
from Aufgabe_2 import MST

def main():
    chp_1 = HCP("./Daten/eins.txt")  # read the data from eins.txt and create graph
    graph_1 = chp_1.graph
    # route, dist = chp_1.nearest_neighbor(graph_1)
    # chp_1.draw_graph(route) # visulise the graph
    route, dist = chp_1.cheapest_insertion(graph_1)
    # # chp_1.draw_graph(route)
    # # print(route,dist)
    # time_nearest_neighbor = chp_1.cal_time(chp_1.nearest_neighbor,graph_1)
    # time_cheapest_insertion = chp_1.cal_time(chp_1.cheapest_insertion,graph_1)
    # print("Elapsed time of 1st Algorithms: ",time_nearest_neighbor)
    # print("Elapsed time of 2nd Algorithms: ",time_cheapest_insertion)


    # chp_1 = HCP("./Daten/eins.txt")
    g = chp_1.graph
    # mst = MST()
    # length,route = mst.find_mst(g)
    # print(length)
    # mst.draw_graph(route,g)
    result = chp_1.cheapest_insertion_2OPT(g,route)
    # print(result)

main()