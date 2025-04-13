from collections import deque

def part1():
    count=0
    for c in coords:
        
        if numbers[c]==0:
            count+=1
            continue
        
        

        move=numbers.pop(c)
        # fall1 = 1
        # if move<0:
        #     fall1=-1
        # wrapped = int(c+move<0 or c+move>=len(coords))
        # if c+move > len(coords)*2 or c+move<-len(coords):
        #     wrapped=wrapped*2 
        # fall1 = fall1*int(wrapped)
        #print(fall1)
        fall = ((c+move)//len(coords))%2
        #print(fall)
        new_loc = (c+move+fall)%len(coords)
        if new_loc==0 and move<0:
            new_loc=len(coords)-1
        numbers.insert(new_loc,move)
        step=0
        
        for pos in coords:
            
            if pos ==c:
                coords[step]=new_loc
                step+=1
                continue
            if coords[step]>c and coords[step]<=new_loc:
                coords[step]-=1
            elif coords[step]<c and coords[step]>=new_loc:
                coords[step]+=1
            step+=1
        count+=1
        
        
    place = 0
    for n in numbers:
        if n ==0:
            break
        place+=1
    a_n=numbers[(1000+place)%len(numbers)]
    b_n=numbers[(2000+place)%len(numbers)]
    c_n=numbers[(3000+place)%len(numbers)]
    print(a_n)
    print(b_n)
    print(c_n)
    print("Result: "+str(a_n+b_n+c_n))


def part2():
    key = 811589153
    
    de_numbers = deque([])
    for n in range(len(numbers)):
        de_numbers.append([n,numbers[n]*key])

    
    #print(de_numbers)
    for i in range(10):
        
        for c in range(len(coords)):
            while de_numbers[0][0] != c:
                de_numbers.rotate(-1)
            
                # if de_numbers[0][1]==0:
                #     continue

            move=de_numbers.popleft()
            
            new_loc = move[1]%len(de_numbers)
            
            de_numbers.rotate(-new_loc)
            de_numbers.append(move)

        #print("inc"+str(i)+":"+str(de_numbers))

    place = 0
    for n in de_numbers:
        if n[1] ==0:
            break
        place+=1
    a_n=de_numbers[(1000+place)%len(numbers)][1]
    b_n=de_numbers[(2000+place)%len(numbers)][1]
    c_n=de_numbers[(3000+place)%len(numbers)][1]
    print(a_n)
    print(b_n)
    print(c_n)
    print("Result: "+str(a_n+b_n+c_n))




while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day20.txt","r")
    list = [number.strip() for number in input.readlines()]
    numbers = []
    for i in list:
        numbers.append(int(i))
    coords = [x for x in range(len(numbers))]
    

    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break