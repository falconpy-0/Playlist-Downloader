import tkinter.font as font
import tkinter as tk

root = tk.Tk()
available_fonts = list(font.families())
available_fonts.sort()

for f in available_fonts:
    print(f)
