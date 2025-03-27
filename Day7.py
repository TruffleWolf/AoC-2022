from functools import cache

def part1():
    
    result = 0
    for key in file_sys:
        # print(key)
        size = get_size(key)
        if size <=100000:
            result +=size
    
    print("Result: "+str(result))

def part2():
    result = 70000000

    target_size = 30000000-(70000000-get_size("//"))
    for key in file_sys:
        size = get_size(key)
        if size>=target_size:
            result = min(result,size)
    print("Result: "+str(result))

@cache
def get_size(dir):
    total_size = 0
    total_list = file_sys[dir]
    # print(total_list)
    for item in total_list:
        # print(type(item))
        if isinstance(item,int):
            total_size+= item
        else:
            total_size+=get_size(item)

    return total_size

def map_filesys():
    # print("Filesys")
    file_sys = {}
    for i in list:
        if i[0]=="$":
            if i[2:4]=="cd":
                # print("CD Command")
                if i[5:]=="..":
                    current_directory.pop()
                else:
                    current_directory.append(i[5:])
            # else:
            #     print("LS Command")
            continue
        elif i[:4]=="dir ":
            # print("Directory")
            new_dir = get_curren_dir_key()+i[4:]+"/"
            dir_list = file_sys.get(get_curren_dir_key(),[])
            dir_list.append(new_dir)
            file_sys[get_curren_dir_key()]=dir_list

        else:
            # print("File")
            file = i.split(" ")
            dir_list = file_sys.get(get_curren_dir_key(),[])
            dir_list.append(int(file[0]))
            file_sys[get_curren_dir_key()]=dir_list


    
    return file_sys

def get_curren_dir_key():
    output = ""
    for c in current_directory:
        output=output+c+"/"
    return output

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day7.txt","r")
    list = [number.strip() for number in input.readlines()]
    current_directory = []
    file_sys = map_filesys()
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break