import csv


alldict = []
allcity = set()
class CityNotFoundError(Exception):
    def __init__(self, city):
        self.message=("%s does not exist" % city)


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            alldict.append(row)
            allcity.add(row["city1"])
            allcity.add(row["city2"])

            
            
def find_nc(city1,city2):
    for dic in alldict:
        if dic["city1"] == city1 and dic["city2"] == city2 or dic["city1"] == city2 and dic["city2"] == city1:
            return int(dic["distance"])
        
def find_neibor(city):
    neibors = []
    for dic in alldict:
        if dic["city1"] == city:
            neibors.append(dic["city2"])
        elif dic["city2"] == city:
            neibors.append(dic["city1"])
    return neibors


# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
  
    frontier = [[start,0,[start]]]
    visited = []
    
    i=-1
    while i < len(frontier)-1:
        changed=False
        i=i+1
        frontier.sort(key=lambda row:(row[1]))
        new_frontier = frontier.copy()
        new_frontier.pop(i)
        tup = frontier[i]#
        if tup[0]==end or  tup[0] in visited:
            continue
        neibors = find_neibor(tup[0])
        for neibor in neibors:
            route = tup[2].copy()
            if neibor not in visited:
                changed = True
                route.append(neibor)
                new_frontier.append([neibor,find_nc(tup[0], neibor) + tup[1] , route])
        if changed:
            i=-1
            visited.append(tup[0])
            frontier=new_frontier
    
        
    for tup in frontier:
        if tup[0] == end:
            print(f"Reached goal with: {tup[1]} cost")
            print(f"with using route: {tup[2]}")
            break


# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    
    valid = False 
    while not valid:
        try:
            path = input("Path of csv file:")
            build_graph(path)
            valid = True
        except Exception as e:
            print(e)
    
    valid = False 
    while not valid:
        try:
            start = input("Start city:")
            if start not in allcity:
                raise CityNotFoundError(start)
            valid = True
        except Exception as e:
            print(e.message)
            
    valid = False 
    while not valid:
        try:
            end = input("End city:")
            if end not in allcity:
                raise CityNotFoundError(end)
            valid = True
        except Exception as e:
            print(e.message)
            
    uniform_cost_search(alldict, start, end)