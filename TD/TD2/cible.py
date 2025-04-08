import tkinter as tk

CANVAS_SIZE= 600
root = tk.Tk()
canvas = tk.Canvas(root, width= CANVAS_SIZE, height= CANVAS_SIZE, background= "#31cade")
canvas.grid()



root.mainloop()