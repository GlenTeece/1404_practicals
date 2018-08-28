COLOURS = {"FIREBRICK": "#b22222",
           "FORESTGREEN": "#228b22",
           "GOLDENROD": "#daa520",
           "HOTPINK": "#ff69b4",
           "MEDIUMPURPLE": "#9370db",
           "PALETURQUOISE": "#afeeee",
           "SKYBLUE": "#87ceeb",
           "STEELBLUE": "#4682b4",
           "VIOLET": "#ee82ee",
           "YELLOWGREEN": "#9acd32"}

print(COLOURS.keys())
user_colour = input("please enter a colour: ").upper()
while user_colour != "":
    if user_colour in COLOURS:
        print(user_colour, "is", COLOURS[user_colour])
    else:
        print("Invalid Colour")
    user_colour = input("please enter a colour: ").upper()
