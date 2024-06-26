import heapq
graph={}
heuristic_values={}
def heuristic_update(all_info):
    heuristic_values[all_info[0]]=all_info[1]
    # print(heuristic_values)


def create_graph(all_info):
    parent=all_info[0]
    graph[parent]={}
    for i in range (2,len(all_info),2):
       child_node=all_info[i]
       weight=int(all_info[i+1])
       graph[parent][child_node]= weight

with open('input_file.txt') as file:
    n = file.readlines()
    # print(n)
    for i in n:
        all_info = i.split()
        # print(all_info)
        heuristic_update(all_info)
        create_graph(all_info)
    print(graph)