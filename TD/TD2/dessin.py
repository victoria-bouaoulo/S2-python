import tkinter as tk
import random as rd

def dessine_disque() -> None:
    centre_x = rd.randint(50, CANVAS_WIDTH - 50)
    centre_y =  rd.randint(50, CANVAS_HEIGHT - 50)
    mon_canvas.create_oval(centre_x - 50, centre_y - 50,
                           centre_x + 50, centre_y + 50,
                           fill=couleur)
    
def dessine_carre() -> None:  







CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()
canvas = tk.Canvas(root, bg='black', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.grid()
root.mainloop()

