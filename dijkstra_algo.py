v, e= map(int, input().split())
graph={}
for _ in range(e):
    v1, v2, wt= map(str,input().split())
    wt= int(wt)
    if v1 not in graph.keys():
        graph[v1]=[(v2,wt)]
    else:
        graph[v1].append((v2,wt))
    if v2 not in graph.keys():
        graph[v2]=[(v1,wt)]
    else:
        graph[v2].append((v1,wt))

def dijkstra(graph, start):
	burned={}
	for i in graph.keys():
		burned[i]=999999
	burned[start]=0
	queue=[start]
	q_count=0
	while(q_count!=len(burned)-1):
		l=sorted(graph[queue[q_count]], key= lambda x:x[1])
		for i in l:
			if i[0] not in queue:
				queue.append(i[0])
				burned[i[0]]=burned[queue[q_count]]+i[1]
			else:
				burned[i[0]]=min(burned[queue[q_count]]+i[1],burned[i[0]])
		q_count+=1
	return burned

dist=dijkstra(graph,'2')

print(dist)
