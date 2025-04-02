# I've written enough search algos from scratch in 2023/4. Time to learn someone else's
import networkx as netx

def part1():
    
    graph = netx.MultiDiGraph()
    s_pos = (start[0],start[1])
    e_pos = (end[0],end[1])
    y_pos = 0
    for y in grid:
        x_pos = 0
        for x in y:
            graph.add_node((x_pos,y_pos))
            x_pos+=1
        y_pos+=1
    positions = {}
    for node in graph.nodes.items():
        positions[node[0]]=(node[0][0],-node[0][1])
        pos = node[0]
        up = (pos[0],pos[1]-1)
        down = (pos[0],pos[1]+1)
        left = (pos[0]-1,pos[1])
        right = (pos[0]+1,pos[1])
        directions = [up,down,left,right]
        candidates = []
        for d in directions:
            
            if in_bounds(d) and grid[d[1]][d[0]] < grid[pos[1]][pos[0]]+2:
                candidates.append(d)
            
        
        for c in candidates:
            graph.add_edge(node[0],c)
    
    
    best = netx.shortest_path_length(graph,source = s_pos,target = e_pos)
    print("Result: "+str(best))



def part2():
    graph = netx.MultiDiGraph()
    start_list = [(start[0],start[1])]
    e_pos = (end[0],end[1])
    y_pos = 0
    for y in grid:
        x_pos = 0
        for x in y:
            if x ==0:
                start_list.append((x_pos,y_pos))
            graph.add_node((x_pos,y_pos))
            x_pos+=1
        y_pos+=1
    positions = {}
    for node in graph.nodes.items():
        positions[node[0]]=(node[0][0],-node[0][1])
        pos = node[0]
        up = (pos[0],pos[1]-1)
        down = (pos[0],pos[1]+1)
        left = (pos[0]-1,pos[1])
        right = (pos[0]+1,pos[1])
        directions = [up,down,left,right]
        candidates = []
        for d in directions:
            
            if in_bounds(d) and grid[d[1]][d[0]] < grid[pos[1]][pos[0]]+2:
                candidates.append(d)
            
        
        for c in candidates:
            graph.add_edge(node[0],c)
    
    best = 999999999
    #print(start_list)
    for s in start_list:
        if netx.has_path(graph,source = s,target=e_pos):
            best = min(best,netx.shortest_path_length(graph,source = s,target = e_pos))
    print("Result: "+str(best))


def in_bounds(pos):
    return (pos[0]>-1 and pos[0]<len(grid[0]))and (pos[1]>-1 and pos[1]<len(grid))

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day12.txt","r")
    list = [number.strip() for number in input.readlines()]
    grid = []
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    start = []
    end = []

    x = 0
    y =0
    for i in list:
        row = []
        x=0
        for char in i:
            if char == "S":
                start = [x,y]
                row.append(0)
            elif char =="E":
                end = [x,y]
                row.append(25)
            else:
                row.append(letters.index(char))

            x+=1
        grid.append(row.copy())
        y+=1




    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break