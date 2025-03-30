

def part1():
    visited = [[0,0]]
    h_pos = [0,0]
    t_pos = [0,0]
    for i in list:
        match i[0]:
            case "U":
                for step in range(int(i[1])):
                    h_pos[1]+=1
                    if abs(h_pos[1]-t_pos[1])>1:
                        t_pos = [h_pos[0],h_pos[1]-1]
                        if t_pos not in visited:
                            visited.append(t_pos.copy())

            case "D":
                for step in range(int(i[1])):
                    h_pos[1]-=1
                    if abs(h_pos[1]-t_pos[1])>1:
                        t_pos = [h_pos[0],h_pos[1]+1]
                        if t_pos not in visited:
                            visited.append(t_pos.copy())
            case "L":
                for step in range(int(i[1])):
                    h_pos[0]-=1
                    if abs(h_pos[0]-t_pos[0])>1:
                        t_pos = [h_pos[0]+1,h_pos[1]]
                        if t_pos not in visited:
                            visited.append(t_pos.copy())
            case "R":
                for step in range(int(i[1])):
                    h_pos[0]+=1
                    if abs(h_pos[0]-t_pos[0])>1:
                        t_pos = [h_pos[0]-1,h_pos[1]]
                        if t_pos not in visited:
                            visited.append(t_pos.copy())
    
    print("Result: "+str(len(visited)))



def part2():

    def update_positions(side):
        for x in range(1,10):
            old_pos = current_positions[x].copy()
            if abs(current_positions[x-1][0]-current_positions[x][0])>1 and abs(current_positions[x-1][1]-current_positions[x][1])>1:
                side = [max(min(current_positions[x-1][0]-current_positions[x][0],1),-1),max(min(current_positions[x-1][1]-current_positions[x][1],1),-1)]
                current_positions[x]=[current_positions[x][0]+side[0],current_positions[x][1]+side[1]]
            elif abs(current_positions[x-1][0]-current_positions[x][0])>1:
                current_positions[x]=[current_positions[x-1][0]-side[0],current_positions[x-1][1]]
                side = [current_positions[x][0]-old_pos[0],current_positions[x][1]-old_pos[1]] 
            elif abs(current_positions[x-1][1]-current_positions[x][1])>1:
                current_positions[x]=[current_positions[x-1][0],current_positions[x-1][1]-side[1]]
                side = [current_positions[x][0]-old_pos[0],current_positions[x][1]-old_pos[1]] 
            else:
                break

        if current_positions[9] not in visited:
            visited.append(current_positions[9].copy())

    visited = [[0,0]]
    current_positions = []
    for i in range(10):
        current_positions.append([0,0])
    
    for command in list:
        
        match command[0]:
            case "U":
                for step in range(int(command[1])):

                    current_positions[0] = [current_positions[0][0],current_positions[0][1]+1]
                    update_positions([0,1])
            case "D":
                for step in range(int(command[1])):

                    current_positions[0] = [current_positions[0][0],current_positions[0][1]-1]
                    update_positions([0,-1])
            case "L":
                for step in range(int(command[1])):

                    current_positions[0] = [current_positions[0][0]-1,current_positions[0][1]]
                    update_positions([-1,0])
            case "R":
                for step in range(int(command[1])):

                    current_positions[0] = [current_positions[0][0]+1,current_positions[0][1]]
                    update_positions([1,0])
    

    print("Result: "+str(len(visited)))



while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day9.txt","r")
    list = [number.strip().split(" ") for number in input.readlines()]


    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break