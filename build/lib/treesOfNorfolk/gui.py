"""
Resources:

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/
https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-spatial-data/customize-raster-plots/interactive-maps/
https://realpython.com/python-folium-web-maps-from-data/

"""

from tkinter import ttk
from tkinter import *


def foo():
    root = Tk()
    root.title("Norfolk's Oldest Trees")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky="N, S, E, W")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Button(mainframe, text="Show Me The Map!", command=command()).grid(column=3, row=3)

    meters = StringVar()
    meter_entry = ttk.Entry(mainframe, width=8, textvariable=meters)

    root.mainloop()
    root.destroy()
