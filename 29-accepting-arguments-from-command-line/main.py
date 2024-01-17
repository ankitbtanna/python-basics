import sys
import argparse

print(sys.argv) #  python3 item.py beau 25
name = sys.argv[1]
print(name)

print("Hello World!")

parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)
parser.add_argument('-c', '--color', metavar='color', type=str, required=True, help='The color of the dog')
args = parser.parse_args()

print(args.color)
