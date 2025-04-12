from typing import List
from collections import deque
import math

def part1():
    results = []
    
    time = 24
    count = 0
    for r in robots:
        max_geo=0
        init_mine = MineState()
        current_queue:deque[List[MineState,int]] = deque([[init_mine,0]])
        max_ore = max(max(max(r[0].ore,r[1].ore),r[2].ore),r[3].ore)
        #branch based on target bot instead of each step?
        while current_queue:

            state = current_queue.popleft()
            current_mine = state[0]
            step = state[1]
            current_time = time-step
            check=((current_mine.geo_bots + current_time)*current_time)+current_mine.geo_stock
            if check<max_geo:
                continue
            
            for i in range(current_time):
                
                #geo possiblity
                if current_mine.obsidian_stock>=r[3].obsidian and current_mine.ore_stock>=r[3].ore:
                    geo_mine = current_mine.copy()
                    geo_mine.progress()
                    geo_mine.geo_bots+=1
                    geo_mine.ore_stock-=r[3].ore
                    geo_mine.obsidian_stock-=r[3].obsidian
                    geo_mine.can_ore = True
                    geo_mine.can_clay = True
                    geo_mine.can_obsidian =True
                    current_queue.append([geo_mine,i+step+1])
                
                #obsidian possiblity
                if current_mine.clay_stock>=r[2].clay and current_mine.ore_stock>=r[2].ore and current_mine.can_obsidian:
                    obsid_mine = current_mine.copy()
                    obsid_mine.progress()
                    obsid_mine.obsidian_bots+=1
                    obsid_mine.clay_stock-=r[2].clay
                    obsid_mine.ore_stock-=r[2].ore
                    obsid_mine.can_ore = True
                    obsid_mine.can_clay = True
                    obsid_mine.can_obsidian =True
                    current_queue.append([obsid_mine,i+step+1])
                    current_mine.can_obsidian =False
                
                #clay possiblity
                if current_mine.ore_stock>=r[1].ore and r[1].ore<current_time-i and current_mine.can_clay and current_mine.clay_bots<r[2].clay:
                    clay_mine = current_mine.copy()
                    clay_mine.progress()
                    clay_mine.clay_bots+=1
                    clay_mine.ore_stock-=r[1].ore
                    clay_mine.can_ore = True
                    clay_mine.can_clay = True
                    clay_mine.can_obsidian =True
                    #print("CLAY"+str(clay_mine.clay_bots))
                    current_queue.append([clay_mine,i+step+1])
                    current_mine.can_clay = False
                
                #ore possibility
                if current_mine.ore_stock>=r[0].ore and current_mine.ore_bots<max_ore and current_mine.can_ore:
                    ore_mine = current_mine.copy()
                    ore_mine.progress()
                    ore_mine.ore_bots+=1
                    ore_mine.ore_stock-=r[0].ore
                    ore_mine.can_ore = True
                    ore_mine.can_clay = True
                    ore_mine.can_obsidian =True
                    current_queue.append([ore_mine,i+step+1])
                    current_mine.can_ore = False
                current_mine.progress()

            max_geo = max(max_geo,current_mine.geo_stock)
            if len(current_queue)%5 ==0:
                print("r"+str(count)+":"+str(len(current_queue)))
        

        results.append(max_geo)
        count+=1
        print("r"+str(count))

    print(results)

    total_score = 0
    count = 1
    for i in results:
        total_score+=(count*i)
        count+=1
    
    print("Result: "+str(total_score))

def part2():
    results = []
    
    time = 32
    count = 0
    for r in robots:
        if count ==3:
            break
        max_geo=0
        init_mine = MineState()
        current_queue:deque[List[MineState,int]] = deque([[init_mine,0]])
        max_ore = max(max(max(r[0].ore,r[1].ore),r[2].ore),r[3].ore)
        #branch based on target bot instead of each step?
        while current_queue:

            state = current_queue.popleft()
            current_mine = state[0]
            step = state[1]
            current_time = time-step
            check=((current_mine.geo_bots + current_time)*current_time)+current_mine.geo_stock
            if check<max_geo:
                continue
            
            for i in range(current_time):
                
                #geo possiblity
                if current_mine.obsidian_stock>=r[3].obsidian and current_mine.ore_stock>=r[3].ore and current_mine.can_geo:
                    geo_mine = current_mine.copy()
                    geo_mine.progress()
                    geo_mine.geo_bots+=1
                    geo_mine.ore_stock-=r[3].ore
                    geo_mine.obsidian_stock-=r[3].obsidian
                    geo_mine.can_ore = True
                    geo_mine.can_clay = True
                    geo_mine.can_obsidian =True
                    geo_mine.can_geo = True
                    current_queue.append([geo_mine,i+step+1])
                    current_mine.can_geo = False
                
                #obsidian possiblity
                if current_mine.clay_stock>=r[2].clay and current_mine.ore_stock>=r[2].ore and current_mine.can_obsidian and current_mine.obsidian_bots<r[3].obsidian:
                    obsid_mine = current_mine.copy()
                    obsid_mine.progress()
                    obsid_mine.obsidian_bots+=1
                    obsid_mine.clay_stock-=r[2].clay
                    obsid_mine.ore_stock-=r[2].ore
                    obsid_mine.can_ore = True
                    obsid_mine.can_clay = True
                    obsid_mine.can_obsidian =True
                    obsid_mine.can_geo = True
                    current_queue.append([obsid_mine,i+step+1])
                    current_mine.can_obsidian =False
                
                #clay possiblity
                if current_mine.ore_stock>=r[1].ore and r[1].ore<current_time-i and current_mine.can_clay and current_mine.clay_bots<r[2].clay:
                    clay_mine = current_mine.copy()
                    clay_mine.progress()
                    clay_mine.clay_bots+=1
                    clay_mine.ore_stock-=r[1].ore
                    clay_mine.can_ore = True
                    clay_mine.can_clay = True
                    clay_mine.can_obsidian =True
                    clay_mine.can_geo = True
                    #print("CLAY"+str(clay_mine.clay_bots))
                    current_queue.append([clay_mine,i+step+1])
                    current_mine.can_clay = False
                
                #ore possibility
                if current_mine.ore_stock>=r[0].ore and current_mine.ore_bots<max_ore and current_mine.can_ore:
                    ore_mine = current_mine.copy()
                    ore_mine.progress()
                    ore_mine.ore_bots+=1
                    ore_mine.ore_stock-=r[0].ore
                    ore_mine.can_ore = True
                    ore_mine.can_clay = True
                    ore_mine.can_obsidian =True
                    ore_mine.can_geo = True
                    current_queue.append([ore_mine,i+step+1])
                    current_mine.can_ore = False
                current_mine.progress()

            max_geo = max(max_geo,current_mine.geo_stock)
            if len(current_queue)%1000 ==0:
                print("r"+str(count)+":"+str(len(current_queue)))
        

        results.append(max_geo)
        count+=1
        print("r"+str(count))

    print(results)

    total_score = 1
    for i in results:
        total_score=(total_score*i)
    
    print("Result: "+str(total_score))

class MineState:
    can_ore = True
    can_clay = True
    can_obsidian = True
    can_geo = True
    ore_stock = 0
    clay_stock = 0
    obsidian_stock=0
    geo_stock=0
    ore_bots =1
    clay_bots=0
    obsidian_bots=0
    geo_bots=0
    history = ""
    def progress(self):
        self.ore_stock+=self.ore_bots
        self.clay_stock+=self.clay_bots
        self.obsidian_stock+=self.obsidian_bots
        self.geo_stock+=self.geo_bots
    def __str__(self):
        return("Ore:"+str(self.ore_bots)+":"+str(self.ore_stock)+
               " Clay:"+str(self.clay_bots)+":"+str(self.clay_stock)+
               " Obsid:"+str(self.obsidian_bots)+":"+str(self.obsidian_stock)+
               " Geo:"+str(self.geo_bots)+":"+str(self.geo_stock))
    def copy(self):
        clone_mine = MineState()
        clone_mine.ore_stock = self.ore_stock
        clone_mine.clay_stock = self.clay_stock
        clone_mine.obsidian_stock = self.obsidian_stock
        clone_mine.geo_stock = self.geo_stock
        clone_mine.ore_bots = self.ore_bots
        clone_mine.clay_bots = self.clay_bots
        clone_mine.obsidian_bots = self.obsidian_bots
        clone_mine.geo_bots = self.geo_bots
        clone_mine.history = self.history
        return clone_mine

class Robot:
    def __init__(self,o,cl=0,ob=0):
        self.ore=o
        self.clay=cl
        self.obsidian=ob
    def __repr__(self):
        return "Ore:"+str(self.ore)+" Clay:"+str(self.clay)+" Obsidian:"+str(self.obsidian)
    def __str__(self):
        return "Ore:"+str(self.ore)+" Clay:"+str(self.clay)+" Obsidian:"+str(self.obsidian)
    
    ore = 0
    clay = 0
    obsidian = 0


while True:
    part = int(input("Please select 1 or 2: "))
    input = open("input/Day19.txt","r")
    list = [number.strip() for number in input.readlines()]

    robots:List[List[Robot]] = []
    for i in list:
        split = i.split(". ")
        split1 = split[0].split(" ")
        split2 = split[1].split(" ")
        split3 = split[2].split(" ")
        split4 = split[3].split(" ")
        
        robots.append([Robot(int(split1[6])),
                       Robot(int(split2[4])),
                       Robot(int(split3[4]),int(split3[7])),
                       Robot(int(split4[4]),0,int(split4[7]))
                       ])

    
    if part == 1:
        part1()
        break
    elif part == 2:
        part2()
        break