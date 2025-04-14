from functools import cache
# import networkx as netx
# import matplotlib.pyplot as plt

def part1():
    result = monkey_dive("root")
    print("Result: "+str(result))

def part2():
    root_m = monkeys["root"]
    left = human_dive(root_m[0])
    right =human_dive(root_m[2])
    print(left)
    print(right)
    target = left[0]
    if left[1]:
        target = right[0]
    human_chain.reverse()
    print(target)
    for h in human_chain:
        #print(h)
        step = h[0]
        print(h)
        if step == "humn":
            print("Target:"+str(target))
            break
        a = h[2][0]
        b = target
        if h[2][1]:
            a = target
            b = h[5][0]
        match h[3]:
            case "+":
                if a == target:
                    target = a-b
                    print(str(a)+"-"+str(b)+"="+str(target))
                else:
                    target = b-a
                    print(str(b)+"-"+str(a)+"="+str(target))
            case "-":
                if a == target:
                    target = a+b
                    print(str(a)+"+"+str(b)+"="+str(target))
                else:
                    target = a-b
                    print(str(a)+"-"+str(b)+"="+str(target))
            case "*":
                if a == target:
                    target = a//b
                    print(str(a)+"/"+str(b)+"="+str(target))
                else:
                    target = b//a
                    print(str(b)+"/"+str(a)+"="+str(target))
            case "/":
                target = a*b
                print(str(a)+"*"+str(b)+"="+str(target))

        


@cache
def monkey_dive(id:str)->int:
    value = 0
    current_m = monkeys[id]
    match current_m[1]:
        case "A":
            value=current_m[0]
        case "+":
            value= monkey_dive(current_m[0])+monkey_dive(current_m[2])
        case "-":
            value= monkey_dive(current_m[0])-monkey_dive(current_m[2])
        case "*":
            value= monkey_dive(current_m[0])*monkey_dive(current_m[2])
        case "/":
            value= monkey_dive(current_m[0])//monkey_dive(current_m[2])
    return value
    
@cache
def human_dive(id):
    value = 0
    current_m = monkeys[id]
    h_case = False
    a = []
    b = []
    if id == "humn":
        print("HUMAN FOUND")
        h_case = True
    match current_m[1]:
        case "A":
            value=current_m[0]
        case "+":
            a = human_dive(current_m[0])
            b = human_dive(current_m[2])
            value= a[0]+b[0]
            h_case = a[1] or b[1]
        case "-":
            a = human_dive(current_m[0])
            b = human_dive(current_m[2])
            value= a[0]-b[0]
            h_case = a[1] or b[1]
        case "*":
            a = human_dive(current_m[0])
            b = human_dive(current_m[2])
            value= a[0]*b[0]
            h_case = a[1] or b[1]
        case "/":
            a = human_dive(current_m[0])
            b = human_dive(current_m[2])
            value= a[0]//b[0]
            h_case = a[1] or b[1]
    if h_case:
        parsed = [id,current_m[0],a,current_m[1],current_m[2],b,value]
        human_chain.append(parsed)
    return [value,h_case]

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day21.txt","r")
    list = [number.strip() for number in input.readlines()]
    monkeys = {}
    human_chain = []
    for i in list:
        split = i.split(": ")
        
        if split[1].isnumeric():
            monkeys[split[0]]=[int(split[1]),"A",0]
        else:
            split2=split[1].split(" ")
            monkeys[split[0]]=[split2[0],split2[1],split2[2]]

    
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break