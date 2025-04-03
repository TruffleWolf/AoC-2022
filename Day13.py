from ast import literal_eval

def part1():
    count = 1
    result = 0
    for i in pairs:
        test = is_ordered(i)
        if test == 1:
            result+=count
        if test == 2:
            print("FINAL RESULT WAS A TIE: "+str(i))
        

        count+=1
    
    print("Result: "+str(result))


def part2():
    two_score = 0
    six_score = 0
    for i in pairs:
        test = is_ordered([[[2]],i[0]])
        if test == 2:
            print("FINAL RESULT MATCHED TEST PACKET 2")
        elif test == 0:
            two_score+=1
            six_score+=1
        else:
            test = is_ordered([[[6]],i[0]])
            if test == 2:
                print("FINAL RESULT MATCHED TEST PACKET 6")
            elif test == 0:
                six_score+=1
        
        test = is_ordered([[[2]],i[1]])
        if test == 2:
            print("FINAL RESULT MATCHED TEST PACKET 2")
        elif test == 0:
            two_score+=1
            six_score+=1
        else:
            test = is_ordered([[[6]],i[1]])
            if test == 2:
                print("FINAL RESULT MATCHED TEST PACKET 6")
            elif test == 0:
                six_score+=1

    result = (two_score+1)*(six_score+2)
    print("Result: "+str(result))

def is_ordered(pair):
    left = pair[0]
    right = pair[1]
    step = 0
    for l in left:
        if len(right)<=step:
            return 0
        r = right[step]
        if type(l) is int and type(r) is int:
            if l == r:
                step+=1
                continue
            if l < r:
                return 1
            return 0
        if type(l) is int:
            rec_result = is_ordered([[l],r])
            if rec_result == 2:
                step+=1
                continue
            return rec_result
        if type(r) is int:
            rec_result = is_ordered([l,[r]])
            if rec_result == 2:
                step+=1
                continue
            return rec_result
        
        rec_result = is_ordered([l,r])
        if rec_result==2:
            step+=1
            continue
        return rec_result

    if len(right)> step:
        return 1
    return 2
    
    

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day13.txt","r")
    list = [number.strip() for number in input.readlines()]
    pairs = []
    line_a = []
    line_b = []
    first = True
    for i in list:
        if i =="":
            pairs.append([line_a.copy(),line_b.copy()])
            line_a = []
            line_b = []
            first = True
            continue
        split = i.split()
        for s in split:
            new_line = literal_eval(s)
        if first:
            line_a = new_line
            first = False
            
        else:
            line_b = new_line
            
    pairs.append([line_a.copy(),line_b.copy()])


    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break