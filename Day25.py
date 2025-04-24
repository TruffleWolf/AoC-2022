
def part1():
    pass

def part2():
    pass


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day22.txt","r")
    list = [number.replace("\n","") for number in input.readlines()]

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break