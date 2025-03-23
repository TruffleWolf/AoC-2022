
def part1():
    
    total = 0

    for i in list:
        front = i[:int(len(i)/2)]
        back = i[int(len(i)/2):]
        
        for char in front:
            loc = back.find(char)
            if loc != -1:
                total +=char_scores.index(char)
                break
    
    print("Result: "+str(total))

def part2():
    total = 0
    count = 0
    group_list = []
    for i in list:
        if count >2:

            for char in group_list[0]:
                if group_list[1].find(char)!=-1:
                    if group_list[2].find(char)!=-1:
                        print(char)
                        total +=char_scores.index(char)
                        break
            count = 0
            group_list = []
        group_list.append(i)
        count +=1
    
    for char in group_list[0]:
                if group_list[1].find(char)!=-1:
                    if group_list[2].find(char)!=-1:
                        print(char)
                        total +=char_scores.index(char)
                        break  


    print("Result: "+str(total))

while True:
    char_scores = ["_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                   "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day3.txt","r")
    list = [number.strip() for number in input.readlines()]
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break