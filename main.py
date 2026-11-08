import tkinter as tk
from Idea import *

root = tk.Tk()
root.title("Game idea generator")
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

def randomise():
    game_genre.config(text=f"Game genre: {genre()}")
    game_theme.config(text=f"Game theme: {theme()}")
    game_style.config(text=f"Game style: {game_styles()}")

title = tk.Label(root, text="Game Idea Generator!")
title.pack( pady=20)
game_genre = tk.Label(root, text=f"Game genre: {genre()}")
game_theme = tk.Label(root, text=f"Game theme: {theme()}")
game_style = tk.Label(root, text=f"Game style: {game_styles()}")

game_theme.pack(pady=5)
game_genre.pack(pady=5)
game_style.pack(pady=5)

button = tk.Button(root, text="Randomise", width=25, command=randomise)
button.pack(pady=15, padx=10)

root.mainloop()