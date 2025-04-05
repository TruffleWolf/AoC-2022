def part1():
    target_row = 2000000
    results = 0
    min_x = 999999
    max_x = -999999
    count = 0
    for s in sensors:
        if calc_dist(s,[s[0],target_row])<=distances[count]:
            max_x = max(max_x,s[0]+distances[count])
            min_x = min(min_x,s[0]-distances[count])
        count+=1
    
    for x in range(min_x,max_x+1):
        test_loc = [x,target_row]
        if test_loc in beacons:
            continue
        count = 0
        for s in sensors:
            if calc_dist(test_loc,s)<=distances[count]:
                results+=1
                break
            count+=1
            

    print("Result: "+str(results))


def part2():
    max_range = 4000000
    target_loc = [1,1]
    complete = False
    for y in range(max_range+1):
        if y%100000==0:
            print(y)
        relevants = []
        count = 0
        for s in sensors:
            if y in range((s[1]-distances[count]),(s[1]+distances[count]+1)):
                dist = abs(distances[count]-abs((s[1]-y)))
                relevants.append([s[0]-(dist+1),y])
                relevants.append([s[0]+(dist+1),y])
            count+=1

        
        for r in relevants:
            if r[0]<0 or r[0]>max_range:
                continue
            #print(r)
            found = True
            count = 0
            for s in sensors:
                if calc_dist(r,s)<=distances[count]:
                    found = False
                    break
                count+=1
            if found:
                target_loc = r.copy()
                print("Found: "+str(target_loc))
                complete= True
                break
        if complete:
            break




    print("Result: "+str((4000000*target_loc[0])+target_loc[1]))

def calc_dist(a,b):

    return abs(a[0]-b[0])+abs(a[1]-b[1])

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day15.txt","r")
    list = [number.strip() for number in input.readlines()]

    sensors = []
    beacons = []
    distances = []
    for i in list:
        split1 = i.split(": ")
        splitS = split1[0].split(", ")
        splitB = split1[1].split(", ")
        new_sensor = [int(splitS[0][12:]),int(splitS[1][2:])]
        new_beacon = [int(splitB[0][23:]),int(splitB[1][2:])]
        sensors.append(new_sensor.copy())
        beacons.append(new_beacon.copy())
        distances.append(calc_dist(new_sensor,new_beacon))


    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break