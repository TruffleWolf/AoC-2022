import networkx as netx
from functools import cache

def part1():
    current_pos = "AA"
    timer = 30

    total_scores = dive(current_pos,relevant_valves.copy(),timer,0)
 
    total_scores.sort()

    print("Result: "+str(total_scores[-1]))



def part2():
    #this code runs for a long time but double dive's print(best) can help you make a good guess under time contraints
    player_pos = "AA"
    ele_pos = "AA"
    timer = 26

    total_scores = double_dive([player_pos,ele_pos],relevant_valves.copy(),timer,[0,0],0)

    total_scores.sort()

    print("Result: "+str(total_scores[-1]))





def dive(position,options,timer,current_score):
    scores = []
    for o in options:
        route = calc_route(position,o)
        time_spent = len(route)
        #print(time_spent)
        if time_spent<timer:
            new_opt = options.copy()
            new_opt.remove(o)
            new_score = current_score+((timer-time_spent)*flow_rates[o])
            scores=scores+ dive(o,new_opt,timer-time_spent,new_score)
    if len(scores)==0:
        return [current_score]

    return scores

def double_dive(positions,options,timer,land_times,current_score):
    scores = []
    global best                
                        
    if land_times[0]==0:
        for o in options:
            route = calc_route(positions[0],o)
            time_spent = len(route)
            if time_spent<timer:
                new_opt = options.copy()
                new_opt.remove(o)
                new_score = current_score+((timer-time_spent)*flow_rates[o])
                next_time = min(time_spent,land_times[1])
                scores=scores+double_dive([o,positions[1]],new_opt,timer-next_time,[time_spent-next_time,land_times[1]-next_time],new_score)
    if land_times[1]==0:
        for o in options:
            route = calc_route(positions[1],o)
            time_spent = len(route)
            if time_spent<timer:
                new_opt = options.copy()
                new_opt.remove(o)
                new_score = current_score+((timer-time_spent)*flow_rates[o])
                next_time = min(time_spent,land_times[0])
                scores= scores+double_dive([positions[0],o],new_opt,timer-next_time,[land_times[0]-next_time,time_spent-next_time],new_score)
    if len(scores)==0:
        if current_score>best:
            best = current_score
            print(best)
        return[current_score]
    return scores

@cache
def calc_route(start,end):
    path = netx.astar_path(graph,start,end)
    return path

while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day16.txt","r")
    list = [number.strip() for number in input.readlines()]
    best = 0
    valve_ids = []
    relevant_valves = []
    flow_rates = {}
    path_dict = {}
    graph = netx.Graph()
    for i in list:
        split1 = i.split("; ")
        valve_id = split1[0][6:8]
        valve_rate = int(split1[0][23:])
        split2 = split1[1].split(", ")
        paths = []
        count = 0
        for s in split2:
            if count ==0:
                paths.append(s[-2:])
                count+=1
                continue
            paths.append(s)
            count+=1
        valve_ids.append(valve_id)
        flow_rates[valve_id]=valve_rate
        if valve_rate >0:
            relevant_valves.append(valve_id)
        path_dict[valve_id]=paths.copy()
        graph.add_node(valve_id,flow = valve_rate)
    for v in valve_ids:
        for v2 in path_dict[v]:
            graph.add_edge(v,v2)




    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break