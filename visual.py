#a convenient function which takes in a networkx graph that can be called to make an interactive graph using pyvis.

from pyvis.network import Network

def display(graph, file_name='graph.html'):

        nt = Network(height = "650px", width = "62%", bgcolor = "#222222", font_color = "white")
        nt.from_nx(graph, show_edge_weights=False)
        nt.barnes_hut()
        nt.toggle_physics(True)
        nt.show_buttons(filter_ = ["physics"])
        nt.show(file_name)

#theme and layout is given coded here. Hence the user just needs to call the function with minimal params.
