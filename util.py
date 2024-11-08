import networkx as nx
import customtkinter as ctk


def create_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_edge("Medellin", "Puerto Berrio", weight=186)
    G.add_edge("Medellin", "Puerto Triunfo", weight=190)
    G.add_edge("Medellin", "Manizales", weight=200)
    G.add_edge("Puerto Triunfo", "Puerto Berrio", weight=129)
    G.add_edge("Honda", "Manizales", weight=141)
    G.add_edge("Honda", "Puerto Triunfo", weight=102)
    G.add_edge("Honda", "Ibague", weight=141)
    G.add_edge("Honda", "Bogota", weight=169)
    G.add_edge("Honda", "Girardot", weight=138)
    G.add_edge("Ibague", "Manizales", weight=174)
    G.add_edge("Girardot", "Ibague", weight=66)
    G.add_edge("Girardot", "Bogota", weight=133)
    return G


def on_click(G: nx.Graph, origen: str, destino: str) -> None:
    print(nx.bidirectional_shortest_path(G, origen, destino))


def create_tab_nodes(G, frm: ctk.CTkFrame, nodes: list[str]):
    tabview = ctk.CTkTabview(frm, corner_radius=25)
    tabview.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    tabs: dict[str] = {}
    for node in nodes:
        tabview.add(node)
        tabs[node] = ctk.CTkTextbox(
            tabview.tab(node),
            width=650,
            height=200,
        )
        tabs[node].grid(row=0, column=0)
    return tabview, tabs


def fill_tabs(G: nx.Graph, tabs: dict):
    nodes = list(G.nodes)

    for node in nodes:
        i = 0
        current_textbox = tabs[node]
        for edge in G.edges(node):
            current_textbox.insert(f"{i}.0", edge[1] + "\n")
            i += 1

    # current_tab = tabview.get()


# current_textbox.delete("0.0", "end")

# edges = list(G.edges(current_tab))
# for edge in edges:
#     current_textbox.insert(edge)


# def showNodes(G: nx.Graph, frm: tk.Frame) -> None:
#     node_list: tk.Listbox = tk.Listbox(frm)
#     node_list.grid(row=0, column=0)
#     nodes = list(G.nodes)
#     for node in nodes:
#         node_list.insert(tk.END, node)


# print(nx.bidirectional_shortest_path(G, "Medellin", "Bogota"))
# nx.draw_spring(G, with_labels=True)
# plt.show()
