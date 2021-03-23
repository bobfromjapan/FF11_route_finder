import networkx as nx
import codecs
import matplotlib.pyplot as plt
import yaml

walk_only = True

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


# pos = nx.spring_layout(graph, k=1.2)
# nx.draw_networkx_nodes(graph, pos, alpha=0.6, node_size=500)
# nx.draw_networkx_labels(graph, pos, font_size=4, font_family="MS Gothic")
# nx.draw_networkx_edges(graph, pos, alpha=0.4)

print(nx.shortest_path(graph, source='ウィンダス', target='ムバルポロス新市街'))