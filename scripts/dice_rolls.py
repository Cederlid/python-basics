import random

path = "dice_rolls.txt"

with open(path, "w") as f:
    f.write("===================================\n")
    f.write("This is to simulate a dice roll\n")
    f.write("===================================\n")
    f.write("a) \n")
    dice_rolls = [random.randint(1,6) for r in range(20)]
    f.write(str(dice_rolls))
    f.write("\nb) \n")
    sorted_rolls = sorted(dice_rolls)
    f.write(str(sorted_rolls))
    f.write("\nc) \n")
    count_four = str(sorted_rolls.count(4))
    f.write(f"Number four is accuring {count_four} times")
