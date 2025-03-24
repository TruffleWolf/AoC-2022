def part1():
    total = 0
    for line in list:
        parts = line.split(",")
        front = parts[0].split("-")
        back = parts[1].split("-")
        if int(front[0])<=int(back[0]) and int(front[1])>=int(back[1]):
            total+=1
        elif int(back[0])<= int(front[0]) and int(back[1])>=int(front[1]):
            total+=1
    print("Result: "+str(total))



def part2():
    print("Two")
    total = 0
    for line in list:
        parts = line.split(",")
        front = parts[0].split("-")
        back = parts[1].split("-")
        if int(front[0])>=int(back[0])and int(front[0])<=int(back[1]):
            total+=1
        elif int(front[1])>=int(back[0])and int(front[1])<=int(back[1]):
            total+=1
        elif int(back[0])>=int(front[0])and int(back[0])<=int(front[1]):
            total+=1
        elif int(back[1])>=int(front[1])and int(back[1])<=int(front[1]):
            total+=1

    print("Result: "+str(total))

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day4.txt","r")
    list = [number.strip() for number in input.readlines()]
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break