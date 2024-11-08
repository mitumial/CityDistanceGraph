import customtkinter as ctk
from CTkTable import *
import networkx as nx
from util import *

ctk.set_appearance_mode("dark")

G: nx.Graph = create_graph()
nodes: list[str] = list(G.nodes)

app: ctk.CTk = ctk.CTk()
app.title("Distancia entre ciudades de Colombia")
app.minsize(700, 400)
app.columnconfigure(0, weight=1)


frm_info: ctk.CTkFrame = ctk.CTkFrame(app)
frm_info.grid(row=0, column=0, padx=4, pady=4, sticky="ew")
frm_info.columnconfigure(0, weight=1)

tabview, tabs = create_tab_nodes(G, frm_info, nodes)
fill_tabs(G, tabs)

frm_calc: ctk.CTkFrame = ctk.CTkFrame(app)
frm_calc.grid(row=1, column=0, padx=4, pady=4, sticky="ew")
frm_calc.columnconfigure(0, weight=1)
frm_calc.columnconfigure(1, weight=2)

lbl_origen: ctk.CTkLabel = ctk.CTkLabel(frm_calc, text="Origen")
lbl_origen.grid(row=0, column=0, padx=(40, 8), pady=2, sticky="w")
lbl_destino: ctk.CTkLabel = ctk.CTkLabel(frm_calc, text="Destino")
lbl_destino.grid(row=1, column=0, padx=(40, 8), pady=2, sticky="w")

optmenu_origen: ctk.CTkOptionMenu = ctk.CTkOptionMenu(
    frm_calc,
    values=nodes,
    anchor="center",
)
optmenu_origen.grid(row=0, column=1, padx=(8, 40), pady=(10, 15), sticky="e")
optmenu_destino = ctk.CTkOptionMenu(frm_calc, values=nodes, anchor="center")
optmenu_destino.grid(row=1, column=1, padx=(8, 40), pady=(0, 10), sticky="e")

btn_distance: ctk.CTkButton = ctk.CTkButton(
    frm_calc,
    text="Calcular distancia minima",
    command=lambda: on_click(G, optmenu_origen.get(), optmenu_destino.get()),
    width=200,
)
btn_distance.grid(row=3, column=0, padx=(40, 8), pady=(12, 10), sticky="w")


app.mainloop()
