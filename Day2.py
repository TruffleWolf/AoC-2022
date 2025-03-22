
def part1():
    
    total = 0
    pity_dict = {"X":1,"Y":2,"Z":3}

    victory_dict = {"A X":3,"B X":0,"C X":6,
                    "A Y":6,"B Y":3,"C Y":0,
                    "A Z":0,"B Z":6,"C Z":3}

    for i in list:
        compare = i.split()
        total += victory_dict[i]+pity_dict[compare[1]]


    print("Result: "+ str(total))

def part2():
    total = 0
    victory_dict = {"X":0,"Y":3,"Z":6}

    pity_dict = {"A X":3,"B X":1,"C X":2,
                "A Y":1,"B Y":2,"C Y":3,
                "A Z":2,"B Z":3,"C Z":1}

    for i in list:
        compare = i.split()
        total += victory_dict[compare[1]]+pity_dict[i]
    
    print("Result: "+ str(total))

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day2.txt","r")
    list = [number.strip() for number in input.readlines()]
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break