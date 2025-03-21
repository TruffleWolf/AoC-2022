import sys

def part1():
    peak = 0
    current = 0
    list = [number.strip() for number in input.readlines()]
    for i in list:
        if i == "":
            peak = max(peak,current)
            print("total:"+str(current))
            current = 0
            
        else:
            current += int(i)
    print("total:"+str(current))
    peak = max(peak,current)
    print("Result: "+str(peak))
        

def part2():
    current = 0
    food_list = []
    list = [number.strip() for number in input.readlines()]
    for i in list:
        if i == "":
            food_list.append(current)
            current = 0
        else:
            current += int(i)
    food_list.append(current)
    food_list.sort()
    peaks = food_list[-1]+food_list[-2]+food_list[-3]
    print("Result: "+str(peaks))

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day1.txt","r")
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break
    

