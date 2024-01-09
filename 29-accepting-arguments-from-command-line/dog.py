import argparse

def str_to_bool(s):
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    else:
        raise argparse.ArgumentTypeError("Invalid value for boolean argument")

parser = argparse.ArgumentParser(
    description="This program takes the input of dog name and breed"
)

parser.add_argument(
    '-n', '--name', required=True, type=str, help="The dog's name"
)
parser.add_argument(
    '-b', '--breed', required=True, type=str, help="The dog's breed"
)
parser.add_argument(
    '-t', '--toy', required=True, type=str, choices={"bone", "ball"}, help="The dog's toy"
)
parser.add_argument(
    '-v', '--vaccinated', required=True, type=str_to_bool, help="Is the dog vaccinated?"
)

args = parser.parse_args()
print(args.name, args.breed, args.vaccinated, args.toy)
