from functools import cache

def part1():
    inspections = []
    m_count = len(inventories)

    for i in range(m_count):
        inspections.append(0)
    
    for i in range(20):
        
        for x in range(m_count):
            
            for y in inventories[x]:
                
                inspections[x]+=1
                p_result = parse_monkey1(y,x)
                inventories[p_result[1]].append(p_result[0])
            inventories[x]=[]
    print(inspections)
    inspections.sort()
    print("Result: "+str(inspections[-1]*inspections[-2]))

def part2():
    inspections = []
    m_count = len(inventories)

    for i in range(m_count):
        inspections.append(0)
    
    for i in range(10000):
        for x in range(m_count):
            
            for y in inventories[x]:
                
                inspections[x]+=1
                p_result = parse_monkey2(y,x)
                inventories[p_result[1]].append(p_result[0])
            inventories[x]=[]
    print(inspections)
    inspections.sort()
    print("Result: "+str(inspections[-1]*inspections[-2]))

@cache
def parse_monkey1(item,monkey):

    item_A = 0
    item_B = 0
    if operations[monkey][0]=="old":
        item_A = item
    else:
        item_A = int(operations[monkey][0])
    if operations[monkey][2]=="old":
        item_B = item
    else:
        item_B = int(operations[monkey][2])
    new_item = item
    if operations[monkey][1] == "+":
        new_item = item_A+item_B
    else:
        new_item = item_A*item_B
    new_item = new_item//3
    new_target = 0
    if new_item%mod_cases[monkey]==0:
        new_target=result_targets[monkey][0]
    else:
        new_target=result_targets[monkey][1]
    
    return [new_item,new_target]

@cache
def parse_monkey2(item,monkey):
    mod_value = 1
    for m in mod_cases:
        mod_value*=m
    item_A = 0
    item_B = 0
    if operations[monkey][0]=="old":
        item_A = item
    else:
        item_A = int(operations[monkey][0])
    if operations[monkey][2]=="old":
        item_B = item
    else:
        item_B = int(operations[monkey][2])
    new_item = item
    if operations[monkey][1] == "+":
        new_item = item_A+item_B
    else:
        new_item = item_A*item_B
    new_item = new_item%mod_value
    new_target = 0
    if new_item%mod_cases[monkey]==0:
        new_target=result_targets[monkey][0]
    else:
        new_target=result_targets[monkey][1]
    
    return [new_item,new_target]

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day11.txt","r")
    list = [number.strip() for number in input.readlines()]

    inventories = []
    operations = []
    mod_cases = []
    result_targets = []

    groups = []
    current_group = []
    for i in list:
        if i == "":
            groups.append(current_group.copy())
            current_group = []
            continue
        current_group.append(i)
    groups.append(current_group)

    for g in groups:
        #inventory format
        inv = g[1][16:]
        inv = inv.split(", ")
        new_inv = []
        for item in inv:
            new_inv.append(int(item))
        inventories.append(new_inv)
        
        #operation format
        op = g[2][17:]
        op = op.split(" ")
        operations.append(op)

        #condition format
        cond = g[3][19:]
        mod_cases.append(int(cond))

        #result format
        result_t = g[4][25:]
        result_f = g[5][26:]
        result_targets.append([int(result_t),int(result_f)])
        
    
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break