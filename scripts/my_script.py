import argparse

parser = argparse.ArgumentParser(description="Tells you if your computer is bad")

parser.add_argument("--name", type=str, required=True)
parser.add_argument("--age", type=float, required=True)
parser.add_argument("--computer", type=str, default="windows", help="What type of computer?")
parser.add_argument("--problem", type=bool, default=True, help="Do you have computer problem often")

args = parser.parse_args()

def evaluate_computer(name, age, computer, problem):
    if age > 18:
        if problem:
            if computer == "windows":
                print(f"Hi {name}! You are using {computer} so it's very common with problems")
            elif computer == "mac":
                print(f"Hi {name}! Are you sure you know how to use {computer}")
            else:
                print(f"Hi {name}! Get a Mac instead")
        else:
            print("Good for you!")
    else:
        print("You should play outside instead of sitting infront of your computer")

evaluate_computer(name=args.name, age=args.age, computer=args.computer, problem=args.problem)