import networkx as nx
import graphviz
import json
import matplotlib.pyplot as plt

dot = graphviz.Digraph(comment='GPT3')
G = nx.Graph()

xs = json.load(
    open('out_1.json','r')
)

with open('some.csv','w') as hand :
    print('x,y',file=hand)
    for x in xs :
        for y in x['keywords'] :
            print(f'{x["name"]},{y}',file=hand)

'''
for x in xs :
    for y in x['keywords'] :
        dot.edge(
            x['name'],
            y
        )
        G.add_edge(x['name'],y)

#dot.render(view=True)
#nx.draw(G, with_labels=True)

pos = nx.circular_layout(G)
nx.draw(G, pos=pos, with_labels=True)

plt.show()
'''