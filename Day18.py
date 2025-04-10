from collections import deque

def part1():
    face_list = []
    for p in positions:
        for f in p.get_faces():
            if f not in face_list:
                face_list.append(f)
            else:
                face_list.remove(f)

    print("Result: "+str(len(face_list)))

def part2():
    def dive(pos:vec3)->int:
        nonlocal face_list
        nonlocal processed_nodes
        nonlocal max_value
        nonlocal queue
        face_addition = 0
        for f in pos.get_faces():
            if f in face_list:
                face_addition+=1
        up = vec3(pos.x,pos.y,pos.z+1)
        down= vec3(pos.x,pos.y,pos.z-1)
        left= vec3(pos.x-1,pos.y,pos.z)
        right= vec3(pos.x+1,pos.y,pos.z)
        front = vec3(pos.x,pos.y+1,pos.z)
        back = vec3(pos.x,pos.y-1,pos.z)

        
        if up not in processed_nodes and pos.z+1 in range(-1,max_value+1):
            queue.append(up)
            processed_nodes.append(up)
        if down not in processed_nodes and pos.z-1 in range(-1,max_value+1):
            queue.append(down)
            processed_nodes.append(down)
        if left not in processed_nodes and pos.x-1 in range(-1,max_value+1):
            queue.append(left)
            processed_nodes.append(left)
        if right not in processed_nodes and pos.x+1 in range(-1,max_value+1):
            queue.append(right)
            processed_nodes.append(right)
        if front not in processed_nodes and pos.y+1 in range(-1,max_value+1):
            queue.append(front)
            processed_nodes.append(front)
        if back not in processed_nodes and pos.y-1 in range(-1,max_value+1):
            queue.append(back)
            processed_nodes.append(back)

        return face_addition

    
    #find the interior volumes
    #create a 25^3 box and scan for detected edges?
    
    max_value= 0
    face_list = []
    for p in positions:
        for f in p.get_faces():
            max_value = max(max_value,p.x)
            max_value = max(max_value,p.y)
            max_value = max(max_value,p.z)
            if f not in face_list:
                face_list.append(f)
            else:
                face_list.remove(f)
    max_value+=1
    print("Input face calculation complete. Searching gridsize:"+str(max_value))
    # use recursion.
    # it needs to propagate, no loops
    processed_nodes = positions.copy()
    queue = deque([vec3(-1,-1,-1)])
    processed_nodes.append(vec3(-1,-1,-1))
    face_count = 0
    while queue:
        target = queue.popleft()
        face_count+= dive(target)
        if len(processed_nodes)%500==0:
            print(len(processed_nodes))

    
    print("Result: "+str(face_count))

class vec3:
    def __init__(self,start_x = 0,start_y = 0,start_z = 0):
        self.x = start_x
        self.y = start_y
        self.z = start_z
    def __str__(self)->str:
        return str(self.x)+","+str(self.y)+","+str(self.z)
    def __eq__(self,other)->bool:
        return [self.x,self.y,self.z]==[other.x,other.y,other.z]
    def get_faces(self)->list:
        face_list = []
        face_list.append([self.x+.5,self.y,self.z])
        face_list.append([self.x-.5,self.y,self.z])
        face_list.append([self.x,self.y+.5,self.z])
        face_list.append([self.x,self.y-.5,self.z])
        face_list.append([self.x,self.y,self.z+.5])
        face_list.append([self.x,self.y,self.z-.5])
        return face_list

    x = 0
    y = 0
    z = 0
    

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day18.txt","r")
    list = [number.strip() for number in input.readlines()]
    positions = []
    for i in list:
        split = i.split(",")
        new_vec = vec3(int(split[0]),int(split[1]),int(split[2]))
        #print(new_vec)
        positions.append(new_vec)
        

    
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break