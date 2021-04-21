import networkx as nx
import codecs
#import matplotlib.pyplot as plt
import yaml

def find_route(source, dest, walk_only=True):

    graph = nx.DiGraph()

    with codecs.open("areas.yaml", "r", 'utf-8') as yml:
        net = yaml.load(yml, Loader=yaml.SafeLoader)

    for i in net['areas']:
        for j in i['distination']:
            if walk_only:
                if j['transportation']=="walk":
                    graph.add_edges_from([(i['name'], j['name'], {"transportation" : j['transportation'], "weight":j['weight']})])
            else:
                graph.add_edges_from([(i['name'], j['name'], {"transportation" : j['transportation'], "weight":j['weight']})])
    try:
        return nx.shortest_path(graph, source=source, target=dest)
    except nx.exception.NodeNotFound:
        return "No route found!"
# pos = nx.spring_layout(graph, k=1.2)
# nx.draw_networkx_nodes(graph, pos, alpha=0.6, node_size=500)
# nx.draw_networkx_labels(graph, pos, font_size=6, font_family="MS Gothic")
# nx.draw_networkx_edges(graph, pos, alpha=0.4)

# plt.show()

if __name__ == "__main__" :
    while True:
        prompt = input("by walk? (if you want to quit, type \"q\")")

        if prompt in ["y", "yes", "Y", "Yes"]:
            walk_only = True
        elif prompt == "q":
            break
        else:
            walk_only = False 
        
        source = input("source:")
        dest = input("dest:")
        
        print(find_route(source=source, dest=dest, walk_only=walk_only))
        