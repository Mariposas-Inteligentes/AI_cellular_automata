# Luis Solano, Angie Solís y Emilia Víquez


# Global variables
matrix = [800][800]
neighborhood = 2

import argparse

def main(arg1, arg2, arg3):
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")
    print(f"Argument 3: {arg3}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input three arguments")
    parser.add_argument("arg1", type=str, help="Tneighborhoodirst argument")
    parser.add_argument("arg2", type=str, help="The second argument")
    parser.add_argument("arg3", type=str, help="The third argument")

    args = parser.parse_args()
    main(args.arg1, args.arg2, args.arg3)
