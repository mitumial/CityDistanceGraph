import tkinter as tk
from tkinter import ttk
from util import *

G = create_graph()

root = tk.Tk()
root.title("Grafo de ciudades")

frm_info = ttk.Frame(root)
frm_info.grid(row=0, column=0)

showNodes(G, frm_info)

frm_calc = ttk.Frame(root)
frm_calc.grid(row=1, column=0, padx=5, pady=5)


lbl_origen = ttk.Label(frm_calc, text="Origen")
lbl_destino = ttk.Label(frm_calc, text="Destino")
lbl_origen.grid(row=1, column=0)
lbl_destino.grid(row=2, column=0)

btn = ttk.Button(
    frm_calc,
    text="Calcular distancia minima",
    command=on_click(G, "Medellin", "Bogota"),
)
btn.grid(row=3, column=0)


root.mainloop()
