def part1():
    blocker_list = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
    max_height = 0

    command_len = len(commands_R)
    current_command = 0
    for i in range(2022):
        #print(" ")
        if i%100==0:
            print("step:"+str(i)+" = Height:"+str(max_height))
        match i%5:
            case 0:
                
                current_rock = line()
                current_rock.update_pos([2,max_height+4])
            case 1:
                current_rock = cross()
                current_rock.update_pos([2,max_height+5])
            case 2:
                current_rock = corner()
                current_rock.update_pos([2,max_height+4])
            case 3:
                current_rock = rod()
                current_rock.update_pos([2,max_height+4])
            case 4:
                current_rock = cube()
                current_rock.update_pos([2,max_height+4])
        
        while True:
            
            if commands_R[current_command%command_len]:
                if current_rock.can_right(blocker_list):
                    current_rock.update_pos([current_rock.position[0]+1,current_rock.position[1]])
            else:
                if current_rock.can_left(blocker_list):
                    current_rock.update_pos([current_rock.position[0]-1,current_rock.position[1]])
            current_command+=1
            if not current_rock.can_fall(blocker_list):
                for b in current_rock.square_list:
                    blocker_list.append(b)
                break
            current_rock.update_pos([current_rock.position[0],current_rock.position[1]-1])
        max_height = max(max_height,current_rock.top_height())
        
        
        
    # for i in range(18):
    #     test_n = 3129-i
    #     test_str = str(test_n)
    #     for i in range(7):
    #         if [i,test_n] in blocker_list:
    #             test_str+="#"
    #         else:
    #             test_str+="."
    #     print(test_str)
    
    print("Result: "+str(max_height))

def part2():
    blocker_list = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]
    max_height = 0
    command_len = len(commands_R)
    current_command = 0
    prev_height = 0
    max_diff =0
    loop_h_start = 0
    loop_l_start = 0
    loop_steps = []
    target_change = -1
    last_height = 0
    for i in range(10000):
        #print(" ")
        # if i%100==0:
        #     print("step:"+str(i)+" = Height:"+str(max_height))
        #     print("Change:"+str(loop_change))
        #     loop_change = 0
        #this arbitrary search point was created from brute force finding the highest value and when it first appeared, with some buffer to hopefully allow for similar inputs.
        if i > 1500 and target_change < 0:
            target_change = max_diff
            print("Setting target dif to "+str(max_diff))
        match i%5:
            case 0:
                # if max_height-prev_height >13:
                #     print("height change:"+str(max_height-prev_height))
                #     print(i)
                #loop_change+=max_height-prev_height
                max_diff = max(max_diff,max_height-prev_height)
                if target_change > -1 and target_change == max_height-prev_height:
                    if loop_h_start ==0:
                        loop_h_start = max_height
                        loop_l_start = i
                    else:
                        print("DONE HEIGHT: "+str(max_height-loop_h_start)+" LENGTH: "+str(i-loop_l_start))
                        to_travel = 1000000000000-i
                        loop_count = to_travel//(i-loop_l_start)
                        remainder = to_travel%(i-loop_l_start)
                        additional_height = (loop_count)*(max_height-loop_h_start)
                        print(len(loop_steps))
                        print(remainder)
                        for x in range(remainder):
                            additional_height+=loop_steps[x]
                            print(max_height+additional_height)
                        max_height+=additional_height
                        break
                prev_height = max_height
                current_rock = line()
                current_rock.update_pos([2,max_height+4])
            case 1:
                current_rock = cross()
                current_rock.update_pos([2,max_height+5])
            case 2:
                current_rock = corner()
                current_rock.update_pos([2,max_height+4])
            case 3:
                current_rock = rod()
                current_rock.update_pos([2,max_height+4])
            case 4:
                current_rock = cube()
                current_rock.update_pos([2,max_height+4])
        if loop_h_start>0:
            loop_steps.append(max_height-last_height)
        while True:
            
            if commands_R[current_command%command_len]:
                if current_rock.can_right(blocker_list):
                    current_rock.update_pos([current_rock.position[0]+1,current_rock.position[1]])
            else:
                if current_rock.can_left(blocker_list):
                    current_rock.update_pos([current_rock.position[0]-1,current_rock.position[1]])
            current_command+=1
            if not current_rock.can_fall(blocker_list):
                for b in current_rock.square_list:
                    blocker_list.append(b)
                break
            current_rock.update_pos([current_rock.position[0],current_rock.position[1]-1])
        last_height = max_height
        max_height = max(max_height,current_rock.top_height())
        
    
    print("Result: "+str(max_height))

class line:
    #pos = leftmost
    position = [0,0]
    square_list = []
    def can_left(self,blockers:list) -> bool:
        test_block = [self.position[0]-1,self.position[1]]
        return self.position[0]>0 and (test_block not in blockers)
    def can_right(self,blockers:list) -> bool:
        test_block = [self.position[0]+4,self.position[1]]
        return self.position[0]<3 and (test_block not in blockers)
    def update_pos(self,pos:list):
        self.position = pos
        s_list = []
        for i in range(4):
            s_list.append([self.position[0]+i,self.position[1]])
        self.square_list = s_list
    def can_fall(self,blockers:list) -> bool:
        for b in self.square_list:
            test_block = [b[0],b[1]-1]
            if test_block in blockers:
                return False
        return True
    def top_height(self) -> int:
        return self.position[1]
    def bottom_height(self) -> int:
        return self.position[1]

    

class cross:
    #pos = leftmost
    position = [0,0]
    square_list =[]
    def can_left(self,blockers:list) -> bool:
        test = True
        test_blocks = [[self.square_list[0][0]-1,self.square_list[0][1]],[self.square_list[2][0]-1,self.square_list[2][1]],[self.square_list[3][0]-1,self.square_list[3][1]]]
        for t in test_blocks:
            if t in blockers:
                test = False
                break
        return self.position[0]>0 and test
    def can_right(self,blockers:list) -> bool:
        test = True
        test_blocks = [[self.square_list[1][0]+1,self.square_list[1][1]],[self.square_list[2][0]+1,self.square_list[2][1]],[self.square_list[3][0]+1,self.square_list[3][1]]]
        for t in test_blocks:
            if t in blockers:
                test = False
                break
        return self.position[0]<4 and test
    def update_pos(self,pos:list):
        self.position = pos
        s_list = []
        x = self.position[0]
        y = self.position[1]
        s_list.append(self.position.copy())
        s_list.append([x+2,y])
        s_list.append([x+1,y-1])
        s_list.append([x+1,y+1])
        self.square_list = s_list
        
    def can_fall(self,blockers:list) -> bool:
        test_list = self.square_list
        for i in range(3):
            test_block = [test_list[i][0],test_list[i][1]-1]
            if test_block in blockers:
                return False
        return True
    
    def top_height(self) -> int:
        return self.position[1]+1
    def bottom_height(self) -> int:
        return self.position[1]-1
     

class corner:
    #leftmost
    position = [0,0]
    square_list =[]
    def can_left(self,blockers:list) -> bool:
        test = True
        test_blocks = [[self.square_list[0][0]-1,self.square_list[0][1]],[self.square_list[4][0]-1,self.square_list[4][1]],[self.square_list[3][0]-1,self.square_list[3][1]]]
        for t in test_blocks:
            if t in blockers:
                test = False
                break
        return self.position[0]>0 and test
    def can_right(self,blockers:list) -> bool:
        test = True
        test_blocks = [[self.square_list[2][0]+1,self.square_list[2][1]],[self.square_list[3][0]+1,self.square_list[3][1]],[self.square_list[4][0]+1,self.square_list[4][1]]]
        for t in test_blocks:
            if t in blockers:
                test = False
                break
        return self.position[0]<4 and test
    def update_pos(self,pos):
        self.position = pos
        s_list = []
        s_list.append(self.position.copy())
        s_list.append([self.position[0]+1,self.position[1]])
        s_list.append([self.position[0]+2,self.position[1]])
        s_list.append([self.position[0]+2,self.position[1]+1])
        s_list.append([self.position[0]+2,self.position[1]+2])
        self.square_list = s_list

    def can_fall(self,blockers:list) -> bool:
        test_list = self.square_list
        for i in range(3):
            test_block = [test_list[i][0],test_list[i][1]-1]
            if test_block in blockers:
                return False
        return True
    def top_height(self) -> int:
        return self.position[1]+2
    def bottom_height(self) -> int:
        return self.position[1]
    

class rod:
    #bottom
    position = [0,0]
    square_list = []
    def can_left(self,blockers) -> bool:
        test = True
        for s in self.square_list:
            test_block=[s[0]-1,s[1]]
            if test_block in blockers:
                test = False
                break
        return self.position[0]>0 and test
    def can_right(self,blockers) -> bool:
        test = True
        for s in self.square_list:
            test_block = [s[0]+1,s[1]]
            if test_block in blockers:
                test = False
                break
        return self.position[0]<6 and test
    def update_pos(self,pos):
        self.position = pos
        s_list = []
        for i in range(4):
            s_list.append([self.position[0],self.position[1]+i])
        self.square_list = s_list

    def can_fall(self,blockers:list) -> bool:
        return [self.position[0],self.position[1]-1] not in blockers
    def top_height(self) -> int:
        return self.position[1]+3
    def bottom_height(self) -> int:
        return self.position[1]
    

class cube:
    #bottom left
    position = [0,0]
    square_list = []
    def can_left(self,blockers)->bool:
        case1 = [self.square_list[0][0]-1,self.square_list[0][1]] not in blockers
        case2 = [self.square_list[2][0]-1,self.square_list[2][1]] not in blockers
        return self.position[0]>0 and case1 and case2
    def can_right(self,blockers)->bool:
        case1 = [self.square_list[1][0]+1,self.square_list[1][1]] not in blockers
        case2 = [self.square_list[3][0]+1,self.square_list[3][1]] not in blockers
        return self.position[0]<5 and case1 and case2
    def update_pos(self,pos):
        self.position = pos
        s_list = []
        s_list.append(self.position.copy())
        s_list.append([self.position[0]+1,self.position[1]])
        s_list.append([self.position[0],self.position[1]+1])
        s_list.append([self.position[0]+1,self.position[1]+1])
        self.square_list = s_list
    def can_fall(self,blockers:list)->bool:
        case1= [self.square_list[0][0],self.square_list[0][1]-1] not in blockers
        case2 = [self.square_list[1][0],self.square_list[1][1]-1] not in blockers
        
        return case1 and case2
    def top_height(self) ->int:
        return self.position[1]+1
    def bottom_height(self)->int:
        return self.position[1]
    

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day17.txt","r")
    list = [number.strip() for number in input.readlines()]
    commands_R =[]
    for i in list[0]:
        commands_R.append(i==">")
    
    width = 6
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break