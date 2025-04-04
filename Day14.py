def part1():
    sand_count = 0
    current_pos = [500,0]
    
    while current_pos[1]<lowest_point:
        if [current_pos[0],current_pos[1]+1] not in rock_list:
            current_pos = [current_pos[0],current_pos[1]+1]
            continue
        if [current_pos[0]-1,current_pos[1]+1] not in rock_list:
            current_pos = [current_pos[0]-1,current_pos[1]+1]
            continue
        if [current_pos[0]+1,current_pos[1]+1] not in rock_list:
            current_pos = [current_pos[0]+1,current_pos[1]+1]
            continue
        sand_count+=1
        rock_list.append(current_pos.copy())
        current_pos = [500,0]

    print("Result: "+str(sand_count))

def part2():
    sand_count = 0
    current_pos = [500,0]
    floor = lowest_point+1
    print(floor+1)
    while True:
        if current_pos[1]!=floor:
            if [current_pos[0],current_pos[1]+1] not in rock_list:
                current_pos = [current_pos[0],current_pos[1]+1]
                continue
            if [current_pos[0]-1,current_pos[1]+1] not in rock_list:
                current_pos = [current_pos[0]-1,current_pos[1]+1]
                continue
            if [current_pos[0]+1,current_pos[1]+1] not in rock_list:
                current_pos = [current_pos[0]+1,current_pos[1]+1]
                continue
        sand_count+=1
        if sand_count%100 == 0:
            print(sand_count)
        if current_pos == [500,0]:
            break
        rock_list.append(current_pos.copy())
        current_pos = [500,0]

    print("Result: "+str(sand_count))


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day14.txt","r")
    list = [number.strip() for number in input.readlines()]

    lowest_point = 0
    rock_list = []
    for i in list:
        split1 = i.split(" -> ")
        step = 0
        rock1 = []
        rock2 = []
        for s in split1:
            split2 = s.split(",")
            if step == 0:
                rock1 = [int(split2[0]),int(split2[1])]
                rock_list.append(rock1.copy())
                lowest_point = max(lowest_point,rock1[1])
                step+=1
                continue

            rock2 = [int(split2[0]),int(split2[1])]

            if rock1==rock2:
                step+=1
                continue
            elif rock1[0]==rock2[0]:
                for x in range(min(rock1[1],rock2[1])+1,max(rock1[1]+1,rock2[1])):
                    rock_list.append([rock1[0],x])
            elif rock1[1]==rock2[1]:
                for x in range(min(rock1[0],rock2[0])+1,max(rock1[0]+1,rock2[0])):
                    rock_list.append([x,rock1[1]])
            else:
                print("NON LINEAR ROCKS DETECTED: "+str(rock1)+" "+str(rock2))
            rock1 = rock2
            lowest_point = max(lowest_point,rock1[1])
            rock_list.append(rock2.copy())
            step+=1
            

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break