def part1():
    seen_grid = []
    for i in list:
        seen_grid.append([])
    for y in list:
        count = 0
        for x in y:
            seen_grid[count].append(False)
            count+=1
    
    x_pos = 0
    y_pos = 0
    #north
    for x in grid:
        
        current_height = -1
        for y in x:
            if y > current_height:
                current_height= y
                seen_grid[x_pos][y_pos]=True
            y_pos+=1
        x_pos+=1
        y_pos = 0

    #south
    x_pos = 0
    y_pos = -1
    for x in grid:
        current_height = -1
        for y in x:
            if grid[x_pos][y_pos]>current_height:
                current_height = grid[x_pos][y_pos]
                seen_grid[x_pos][y_pos]=True
            y_pos -=1
        x_pos+=1
        y_pos = -1
    #east
    x_pos = 0
    y_pos = 0
    for y in grid[0]:
        current_height =-1
        for x in grid:
            if grid[x_pos][y_pos]>current_height:
                current_height = grid[x_pos][y_pos]
                seen_grid[x_pos][y_pos]=True
            x_pos+=1
        y_pos +=1
        x_pos = 0

    #west
    x_pos = -1
    y_pos = 0
    x_pos = 0
    y_pos = 0
    for y in grid[0]:
        current_height =-1
        for x in grid:
            if grid[x_pos][y_pos]>current_height:
                current_height = grid[x_pos][y_pos]
                seen_grid[x_pos][y_pos]=True
            x_pos-=1
        y_pos +=1
        x_pos = -1

    result = 0
    for x in seen_grid:
        for y in x:
            if y:
                result+=1
    print("Result: "+str(result))


def part2():
    seen_grid = []
    for i in list:
        seen_grid.append([])
    for y in list:
        count = 0
        for x in y:
            seen_grid[count].append(0)
            count+=1
    
    x_pos = 0
    y_pos = 0
    for x in grid:
        
        for y in x:

            current_count = 0
            target_height = y
            total_height = []
            cur_x = x_pos
            cur_y = y_pos
            #north
            cur_y -=1
            while cur_y > -1:
                current_count +=1
                if grid[cur_x][cur_y]>=target_height:
                    total_height.append(current_count)
                    break
                cur_y -=1
            if len(total_height) == 0:
                total_height.append(current_count)
            #south
            current_count = 0
            cur_y = y_pos
            cur_y +=1
            while cur_y < len(grid[0]):
                current_count+=1
                if grid[cur_x][cur_y]>= target_height:
                    total_height.append(current_count)
                    break
                cur_y +=1
            if len(total_height) == 1:
                total_height.append(current_count)
            #east
            current_count = 0
            cur_y = y_pos
            cur_x -=1
            while cur_x>=0:
                current_count+=1
                if grid[cur_x][cur_y]>= target_height:
                    total_height.append(current_count)
                    break
                cur_x-=1
            if len(total_height) == 2:
                total_height.append(current_count)
            #west
            current_count = 0
            cur_x = x_pos
            cur_x+=1
            while cur_x<len(grid):
                current_count+=1
                if grid[cur_x][cur_y]>= target_height:
                    total_height.append(current_count)
                    break
                cur_x+=1
            if len(total_height) == 3:
                total_height.append(current_count)
            #get score for the square
            total = 1
            for i in total_height:
                total *= i
            seen_grid[x_pos][y_pos]=total

            y_pos +=1
        y_pos = 0
        x_pos+=1

    result = 0
    
    for x in seen_grid:
        
        
        for y in x:
            if y>result:
                result = y
    print("Result: "+str(result))


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day8.txt","r")
    list = [number.strip() for number in input.readlines()]
    grid = []
    for i in list[0]:
        grid.append([])
    for y in list:
        count = 0
        for x in y:
            grid[count].append(int(x))
            count +=1


    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break