nv,ne=map(int,input().split(','))
edges=[]
for x in range(ne):
    a,b,c=map(int,input().split(','))
    edges.append((a,b,c))
neighbors={x:[] for x in range(nv)}
for w,a,b in edges:
    neighbors[a].append((w,b))
    neighbors[b].append((w,a))
start=0
visited = []
arr = []
arr.append((0,start))
ng={}
vised=[]
k=nv
mst=[]
while arr:
    w,d = arr.pop(0)
    if d not in visited:
        visited.append(d)
        mst.append((w,d))
        for wt,v in neighbors[d]:
            arr.append((wt,v))
            arr.sort()
min_cost=0
for w,d in mst:
    min_cost+=w
print(min_cost)
