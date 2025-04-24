
def part1():
    def get_directions(pos:list)->list:
        #N,NE,E,SE,S,SW,W,NW
        output = [
            [pos[0],pos[1]-1],
            [pos[0]+1,pos[1]-1],
            [pos[0]+1,pos[1]],
            [pos[0]+1,pos[1]+1],
            [pos[0],pos[1]+1],
            [pos[0]-1,pos[1]+1],
            [pos[0]-1,pos[1]],
            [pos[0]-1,pos[1]-1]
        ]
        return output
    
    def check_n(pos:list)->list:
        moves = get_directions(pos)
        if moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        else:
            return pos
        
    def check_s(pos:list)->list:
        moves = get_directions(pos)
        if moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        else:
            return pos
    
    def check_w(pos:list)->list:
        moves = get_directions(pos)
        if moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        else:
            return pos
        
    def check_e(pos:list)->list:
        moves = get_directions(pos)
        if moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        else:
            return pos

    for i in range(10):
        proposed_moves = []
        for e in elf_list:
            dir_def = get_directions(e)
            nonadjacent = True
            for d in dir_def:
                if d in elf_list:
                    nonadjacent = False
                    break
            
            if nonadjacent:
                proposed_moves.append(e)
            elif i%4==0:
                proposed_moves.append(check_n(e))
            elif i%4==1:
                proposed_moves.append(check_s(e))
            elif i%4==2:
                proposed_moves.append(check_w(e))
            elif i%4==3:
                proposed_moves.append(check_e(e))
        
        index = 0
        for e in elf_list:
            move_list = proposed_moves.copy()
            next_move = move_list.pop(index)
            if next_move not in move_list:
                elf_list[index]=next_move
            index+=1

    #print(elf_list)
    x_range = [elf_list[0][0],elf_list[0][0]]
    y_range = [elf_list[0][1],elf_list[0][1]]
    for e in elf_list:
        x_range=[
            min(x_range[0],e[0]),
            max(x_range[1],e[0])
        ]
        y_range=[
            min(y_range[0],e[1]),
            max(y_range[1],e[1])
        ]
    print(x_range)
    print(y_range)
    result = ((x_range[1]-x_range[0]+1)*(y_range[1]-y_range[0]+1))-len(elf_list)
    print("Result: "+str(result))

def part2():
    def get_directions(pos:list)->list:
        #N,NE,E,SE,S,SW,W,NW
        output = [
            [pos[0],pos[1]-1],
            [pos[0]+1,pos[1]-1],
            [pos[0]+1,pos[1]],
            [pos[0]+1,pos[1]+1],
            [pos[0],pos[1]+1],
            [pos[0]-1,pos[1]+1],
            [pos[0]-1,pos[1]],
            [pos[0]-1,pos[1]-1]
        ]
        return output
    
    def check_n(pos:list)->list:
        moves = get_directions(pos)
        if moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        else:
            return pos
        
    def check_s(pos:list)->list:
        moves = get_directions(pos)
        if moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        else:
            return pos
    
    def check_w(pos:list)->list:
        moves = get_directions(pos)
        if moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        elif moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        else:
            return pos
        
    def check_e(pos:list)->list:
        moves = get_directions(pos)
        if moves[1] not in elf_list and moves[2] not in elf_list and moves[3] not in elf_list:
            return [pos[0]+1,pos[1]]
        elif moves[0] not in elf_list and moves[1] not in elf_list and moves[7] not in elf_list:
            return [pos[0],pos[1]-1]
        elif moves[3] not in elf_list and moves[4] not in elf_list and moves[5] not in elf_list:
            return [pos[0],pos[1]+1]
        elif moves[5] not in elf_list and moves[6] not in elf_list and moves[7] not in elf_list:
            return [pos[0]-1,pos[1]]
        else:
            return pos
    
    count = 0
    while True:
        proposed_moves = []
        nonadjacent_count = 0
        for e in elf_list:
            dir_def = get_directions(e)
            nonadjacent = True
            for d in dir_def:
                if d in elf_list:
                    nonadjacent = False
                    break
            
            if nonadjacent:
                proposed_moves.append(e)
                nonadjacent_count +=1
            elif count%4==0:
                proposed_moves.append(check_n(e))
            elif count%4==1:
                proposed_moves.append(check_s(e))
            elif count%4==2:
                proposed_moves.append(check_w(e))
            elif count%4==3:
                proposed_moves.append(check_e(e))
        
        if nonadjacent_count==len(elf_list):
            break
        
        index = 0
        for e in elf_list:
            move_list = proposed_moves.copy()
            next_move = move_list.pop(index)
            if next_move not in move_list:
                elf_list[index]=next_move
            index+=1
        if count%10==0:
            print(count)
        count+=1

    print("Result: "+str(count+1))


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day23.txt","r")
    lines = [number.strip() for number in input.readlines()]

    elf_list = []
    y_pos = 0
    for i in lines:
        x_pos = 0
        for c in i:
            if c == "#":
                elf_list.append([x_pos,y_pos])
            x_pos+=1
        y_pos +=1

    #print(elf_list)
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break