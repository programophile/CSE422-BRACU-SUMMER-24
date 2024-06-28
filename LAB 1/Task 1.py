import heapq
graph={}
heuristic_values={}
def heuristic_update(all_info):
    heuristic_values[all_info[0]]=int(all_info[1])

def create_graph(all_info):
    parent=all_info[0]
    graph[parent]={}
    for i in range (2,len(all_info),2):
           child_node=all_info[i]
           weight=int(all_info[i+1])
           graph[parent][child_node]= weight
def AstarAlgo(start,goal):
    heap_q=[]
    heapq.heappush(heap_q,(int(heuristic_values[start]),0,start,[start]))

    visited=[]
    while heap_q:
        _,weight,city,path=heapq.heappop(heap_q)
        if city in visited:
            continue
        visited.append(city)
        if city==goal:


            return weight,path
        for child,cost in graph[city].items():
            total_weight=weight+cost
            p_value= total_weight+heuristic_values[child]
            heapq.heappush(heap_q, (p_value, total_weight, child,path+[child]))
    return None



with open('input_file.txt') as file:
    n = file.readlines()
    # print(n)
    for i in n:
        all_info = i.split()
        # print(all_info)
        heuristic_update(all_info)
        create_graph(all_info)


start=input("Enter start :")
end=input("Enter End :")
ans=AstarAlgo(start,end)
output=open('output.txt',"w")
if ans:
    print(f"Path: {' -> '.join(ans[1])}")
    print(f"Total distance: {ans[0]} km")
    output.write(f"Path: {' -> '.join(ans[1])}\nTotal distance: {ans[0]} km")
else:
    print("No Path found")