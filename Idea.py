import random
themes = [
    "Pirates",
    "Space",
    "Victorian Horror",
    "Cyberpunk",
    "Ancient Egypt",
    "Fairy Tale",
    "Wild West",
    "Underwater",
    "Post-Apocalyptic",
    "Mythology",
    "Paranormal"
]

genres = [
    "Farming Sim",
    "Roguelike",
    "Puzzle",
    "Management Sim",
    "Survival",
    "Deckbuilder",
    "RPG",
    "City Builder",
    "Tycoon",
    "Mystery",
    "Tower Defence"
]

styles = [
    "Pixel Art",
    "Low Poly",
    "Hand Drawn",
    "Watercolour",
    "Cartoon",
    "Voxel",
    "Comic Book",
    "PS1 Style"
]

def theme(): 
    theme_output = random.choice(themes)
    return theme_output

def genre():
    genres_output = random.choice(genres)
    return genres_output

def game_styles():
    styles_output = random.choice(styles)
    return styles_output