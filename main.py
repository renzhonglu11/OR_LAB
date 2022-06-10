from Aufgabe_1 import HCP
from Aufgabe_2 import MST

def main():
    chp_1 = HCP("./Daten/eins.txt")  # read the data from eins.txt
    graph_1 = chp_1.graph           # create graph

#############################################
##  uncomment each block for each question ##
#############################################

    # Aufgabe 1 (b)
    # Algorithmus 1
    # route, dist = chp_1.nearest_neighbor(graph_1)
    # print(route,dist)
    # time_nearest_neighbor = chp_1.cal_time(chp_1.nearest_neighbor,graph_1) # caculate the run time
    # print("Elapsed time of 1st Algorithms: ",time_nearest_neighbor)
    # chp_1.draw_graph(route) # visulise the graph


    # Algorithmus 2
    # route, dist = chp_1.cheapest_insertion(graph_1)
    # print(route,dist)
    # time_cheapest_insertion = chp_1.cal_time(chp_1.cheapest_insertion,graph_1) # caculate the run time
    # print("Elapsed time of 2nd Algorithms: ",time_cheapest_insertion)
    # chp_1.draw_graph(route) # visulise the graph


    # Aufgabe 1 (c) 
    # route, dist = chp_1.nearest_neighbor(graph_1) # get the Hamiltonian cycle of nearest_neighbor algorithms
    # route, dist = chp_1.cheapest_insertion(graph_1) # get the Hamiltonian cycle of cheapest_insertion algorithms
    # res_route, res_dist = chp_1.OPT2(route,100)
    # print(res_route,res_dist)
    # time_2opt = chp_1.cal_time(chp_1.cheapest_insertion,graph_1)
    # print("Elapsed time of 2opt Algorithms: ",time_2opt)
    # chp_1.draw_graph(res_route)

    # Aufgabe 2
    # mst = MST()
    # length,route = mst.find_mst(graph_1)
    # print(length)
    # time_prim = chp_1.cal_time(mst.find_mst,graph_1)
    # print("Elapsed time of prim Algorithms: ",time_prim)
    # mst.draw_graph(route,graph_1)

    
main()