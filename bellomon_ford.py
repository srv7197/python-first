v, e= map(int, input().split())
graph={}
for _ in range(e):
    v1, v2, wt= map(str,input().split())
    wt= int(wt)
    if v1 not in graph.keys():
        graph[v1]=[(v2,wt)]
    else:
        graph[v1].append((v2,wt))

def bellman_ford(graph,start):
    shortest_path={}
    for i in graph.keys():
        shortest_path[i]=999999
    shortest_path[start]=0
    for _ in range(len(graph.keys())):
        for i in graph.keys():
            for j in graph[i]:
                shortest_path[j[0]]=min(shortest_path[j[0]],shortest_path[i]+j[1])
    return shortest_path

