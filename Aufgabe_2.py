import math
import networkx as nx
import matplotlib.pyplot as plt

class MST:



    def find_mst(self, graph):
        g = graph.copy()
        v = 1
        Uncon = []
        Con = [v]
        res=[]
        route=[]
        length = 0

        for key in g.keys():
            if key == 1:
                continue
            Uncon.append(key)

        
        while len(Uncon)!=0:
            min_len = float("inf")
            for i in Con:
                for j in Uncon:
                    tmp_len = math.sqrt(
                        math.pow(g[i][0] - g[j][0], 2) + math.pow(g[i][1] - g[j][1], 2)
                    )
                    if tmp_len < min_len:
                        min_len = tmp_len
                        v = j
                        route = [i,j,min_len]              
                        
            length+=min_len
            res.append(route)
            Con.append(v)
            Uncon.remove(v)
           
        
        return length,res

    def draw_graph(self, route, graph):
        """visualise the graph"""
        G = nx.DiGraph()
        g=graph.copy()

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

        for i in route:
            cur_node = i[0]
            next_node = i[1]
            weight = int(i[2])
            G.add_edge(cur_node, next_node,weight=weight)

        for key in g:
            pos[key] = (g[key][0], g[key][1])

        edge_labels = nx.get_edge_attributes(G,"weight")
        nx.draw_networkx(G, pos, **options)
        nx.draw_networkx_edge_labels(G,pos,edge_labels)
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()
        return

