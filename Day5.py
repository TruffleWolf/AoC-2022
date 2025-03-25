def part1():

    for c in commands:
        for step in range(c[0]):
            moved_block = stacks[c[1]].pop()
            stacks[c[2]].append(moved_block)
    
    result = ""
    for s in stacks:
        result = result+s[-1]
    print("Result: "+result)
            

def part2():
    for c in commands:
        stack_slice = []
        for step in range(c[0]):
            stack_slice.append(stacks[c[1]].pop())
        stack_slice.reverse()
        stacks[c[2]]= stacks[c[2]]+stack_slice

    result = ""
    for s in stacks:
        result = result+s[-1]
    print("Result: "+result)



while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day5.txt","r")
    list = [number for number in input.readlines()]

    #formatting
    stacks = []
    commands = []
    rows = []
    mode = True
    for i in list:
        if mode:
            
            if len(i)==1:
                mode = False
                continue
            if i.strip()[0]=="1":
                count = 0
                for x in i.strip().split(" "):
                    if x !="":
                        new_stack = []
                        for r in rows:
                            if r[(count*4)+1]!=" ":
                                new_stack.insert(0,r[(count*4)+1])
                        stacks.append(new_stack)
                        count +=1
                    
                
                continue
            rows.append(i)
            
        else:
            
            new_command = []
            stripped = i.split(" ")
            new_command.append(int(stripped[1]))
            new_command.append(int(stripped[3])-1)
            new_command.append(int(stripped[5].strip())-1)
            commands.append(new_command)
    #end of command formating

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break