import math
import random
import networkx as nx
import matplotlib.pyplot as plt


class HCP:
    def __init__(self,path):
        self.graph = self.build_graph(path)

    def build_graph(self,path):
        Graph = {}

        with open(path) as f:
            for line in f:
                tmp_str = line.split(" ")
                tmp = (int(tmp_str[0]), float(tmp_str[1]), float(tmp_str[2]))
                Graph[tmp[0]] = (tmp[1], tmp[2])

        return Graph

    def nearest_neighbor(self,G):
        graph = G.copy()
        total_dist = 0
        route = []
        start = random.randint(1, len(graph))
        route.append(start)

        while len(graph) != 1:
            v = graph[start]
            v_x = v[0]
            v_y = v[1]
            min_dist = float("inf")
            graph.pop(start)

            for key, value in graph.items():
                x = value[0]
                y = value[1]
                cur_dist = math.sqrt(math.pow(v_x - x, 2) + math.pow(v_y - y, 2))
                # print(cur_dist)
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    start = key

            total_dist += min_dist
            route.append(start)

        route.append(route[0])
        last_two = G[route[-2]]
        last_one = G[route[-1]]
        # print(total_dist)
        total_dist += math.sqrt(
            math.pow(last_two[0] - last_one[0], 2)
            + math.pow(last_two[1] - last_one[1], 2)
        )
        # print(route)
        # print(total_dist)

        return route, total_dist


    def cheapest_insertion(self,G):
        '''{1:(x,y) , 2:(x,y)}'''
        graph = G.copy()
        V = []
        for value in graph.values():
            V.append([value[0],value[1]])

        v0 = V[0]
        H = [v0, v0]
        W = V[1:len(V)]
        route = []

        while len(H) < len(V):
            cost = 0
            for w in W: 
                distance = []
                for i in range(len(H)-1):
                    # distance of the left node
                    d1 = math.sqrt(pow((w[0]-H[i][0]),2) + pow((w[1]-H[i][1]),2))
                    # distance of the right node
                    d2 = math.sqrt(pow((w[0]-H[i+1][0]),2) + pow((w[1]-H[i+1][1]),2))
                    d3 = math.sqrt(pow((H[i+1][0]-H[i][0]),2) + pow((H[i][1]-H[i+1][1]),2))
                    # total distance
                    d = d1 + d2 - d3
                    distance.append(d)

                # find the minimal distance
                min_distance_index = distance.index(min(distance))
                cost += min(distance)
                # add node w in H
                H.insert(min_distance_index+1, w)
                
        for h in range(len(H)):
            route.append(V.index(H[h])+1)
            # H[h] = H.index(h)


        return route, cost 



    def draw_graph(self,route):
        '''visualise the graph'''
        G = nx.DiGraph()
        pos = {}
        options = {
            "font_size": 13,
            "node_size": 500,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 0.5,
            "width": 3,
            "arrowsize": 5,
        }

        for i in range(len(route) - 1):
            cur_node = int(route[i])
            next_node = int(route[i + 1])
            G.add_edge(cur_node, next_node)

        for key in self.graph:
            pos[key] = (self.graph[key][0], self.graph[key][1])

        G.add_edge(int(route[-2]), int(route[-1]))  # get back to start
        
        nx.draw_networkx(G, pos, **options)
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()
        return


chp_1 = HCP("./Daten/eins.txt") # read the data from eins.txt and create graph
graph_1 = chp_1.graph

route, dist = chp_1.nearest_neighbor(graph_1)
# chp_1.draw_graph(route) # visulise the graph
# route, dist = chp_1.cheapest_insertion(graph_1)
# chp_1.draw_graph(route)
# print(route,dist)






