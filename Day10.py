def part1():
    
    result = 0
    relevant= []
    relevant_cycles = [20,60,100,140,180,220]
    register = 1
    cycle = 1

    
    while cycle < 220:
        for command in list:
            #cycles are delayed by each other
            if command == "noop":
                if cycle in relevant_cycles:
                    
                    relevant.append(register*cycle)
                cycle +=1
                continue
            if cycle in relevant_cycles:
                
                relevant.append(register*cycle)
            cycle +=1
            if cycle in relevant_cycles:
                
                relevant.append(register*cycle)
            cycle +=1
            numb = int(command.split(" ")[1])
            register+=numb

    for r in relevant:
        result += r
    print("Result: "+str(result))

def part2():
    width = 40
    register = 1
    image = ""
    cycle = 1
    
    def parse_cycle():
        nonlocal width
        nonlocal image
        nonlocal register
        nonlocal cycle
        if (cycle%width)-1 in range(register-1,register+2):
                image+="#"
        else:
            image+="."
        if cycle%width==0:
            print(image)
            image = ""
        #print("C"+str(cycle)+" R"+str(register))
        cycle +=1

    for command in list:
        if command == "noop":
            parse_cycle()
            continue

        parse_cycle()
        parse_cycle()
        numb = int(command.split(" ")[1])
        register += numb
        



while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day10.txt","r")
    list = [number.strip() for number in input.readlines()]

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break