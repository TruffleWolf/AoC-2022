def part1():
    step =3
    for i in range(len(input)):
        char1=input[step-3]
        char2=input[step-2]
        char3=input[step-1]
        char4=input[step]
        duplicate = (char1==char2 or char1==char3 or char1==char4 or char2==char3 or char2==char4 or char3==char4)

        if (not duplicate):
            step+=1
            break
        
        step +=1
    
    print("Result: "+str(step))

def part2():
    step=0
    length=14

    for i in range(len(input)):
        char_list = {}
        for x in range(length):
            char_list[input[step+x]]=char_list.get(input[step+x],0)+1
        duplicate = False
        for key, value in char_list.items():
            if value>1:
                duplicate = True
        
        if (not duplicate):
            break

        step +=1

    print("Result: "+str(step+length))


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day6.txt","r").readline().strip()

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break