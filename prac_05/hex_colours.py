colour_to_hex = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                 "ALIZARIN CRIMSON": "#e32636",
                 "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                 "AQUA": "#00ffff", "ARMY GREEN": "#4b5320"}

colour = input("Enter colour name: ").upper()
while colour != "":
    if colour in colour_to_hex:
        print(colour_to_hex[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").upper()