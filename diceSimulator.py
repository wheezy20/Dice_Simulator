# A Text-based user interface
# The software will have the ability to roll up to six dice, each with six faces. 



import random

Dice_Face = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),

    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),

    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),

    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )

}

DieHeight = len(Dice_Face[1])
DieWidth = len(Dice_Face[1][0])
DieFaceSeparator = " "



#"parse input()" takes the user's input as a string, checks it to see if it's a valid integer number.
# It then returns it as a Python int object.

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """

    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)



def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for i in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results



def generate_dice_faces_diagram(dice_values):
    
    dice_faces = []
    for value in dice_values:
        dice_faces.append(Dice_Face[value])

    dice_faces_rows = []
    for row_idx in range(DieHeight):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DieFaceSeparator.join(row_components)
        dice_faces_rows.append(row_string)

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram





                        #MAIN CODE

num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)


# Roll the dice
roll_results = roll_dice(num_dice)

dice_face_diagram = generate_dice_faces_diagram(roll_results)
# Display the diagram
print(f"\n{dice_face_diagram}")



