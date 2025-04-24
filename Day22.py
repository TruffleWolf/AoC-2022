

def part1():
    global current_rotation
    global current_loc
    rotation = [1,0]
    current_index = 0
    current_line = "R0"
    dir = 1
    
    for com in commands:
        if com =="L":
            current_rotation=(current_rotation-1)%4
            rotation=rotations[current_rotation]
            if rotation[0]==0:
                current_line="C"+str(current_loc[0])
                dir = -rotation[1]
            else:
                current_line="R"+str(current_loc[1])
                dir = rotation[0]
            current_index = grid[current_line].index(current_loc)
            continue
        elif com=="R":
            current_rotation=(current_rotation+1)%4
            rotation=rotations[current_rotation]
            if rotation[0]==0:
                current_line="C"+str(current_loc[0])
                dir = -rotation[1]
            else:
                current_line="R"+str(current_loc[1])
                dir = rotation[0]
            current_index = grid[current_line].index(current_loc)
            continue
        
        for step in range(int(com)):
            new_index = (current_index+dir)%len(grid[current_line])
            next_pos = grid[current_line][new_index]
            if next_pos[2]=="#":
                break
            current_index=new_index
            current_loc=next_pos
        
    current_loc[0]+=1
    current_loc[1]+=1
    final = (1000*current_loc[1])+(4*current_loc[0])+current_rotation
    print("Result: "+str(final))

def part2():
    pass

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day22.txt","r")
    list = [number.replace("\n","") for number in input.readlines()]

    rotations = [[1,0],[0,-1],[-1,0],[0,1]]
    current_rotation = 0
    current_loc = []
    commands=[]
    #use a dictionary with keys representing each row or column
    grid = {}
    command_mode = False
    command_line = ""
    current_row = 0
    
    for i in list:
        if not "R"+str(current_row)in grid:
            grid["R"+str(current_row)]=[]
        
        if i=="":
            command_mode=True
            continue
        if command_mode:
            command_line = i
            continue
        current_col=0
        for c in i:
            if not "C"+str(current_col) in grid:
                grid["C"+str(current_col)]=[]
            if not c == " ":
                grid["C"+str(current_col)].append([current_col,current_row,c])
                grid["R"+str(current_row)].append([current_col,current_row,c])
                if len(current_loc)==0:
                    current_loc = [current_col,current_row,"."]

            current_col+=1
            
        current_row+=1
    

    command = ""
    for t in command_line:
        if t == "R" or t=="L":
            commands.append(command)
            commands.append(t)
            command = ""
            continue
        command +=t
    if command != "":
        commands.append(int(command))

    
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break