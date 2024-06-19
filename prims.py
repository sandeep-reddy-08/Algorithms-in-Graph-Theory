nv,ne=map(int,input().split(','))
edges=[]
for x in range(ne):
    a,b,c=map(int,input().split(','))
    edges.append((a,b,c))
'''weighted_dic={}
for x in edges:
    a,b,c=x
    weighted_dic[(b,c)]=a
print(weighted_dic)
weight_list=[]
for x in weighted_dic.values():
    weight_list.append(x)
weight_list.sort()
output=[]
vis=[]
print(weight_list)'''
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
'''    
            
        e=(v1,i)
        g=(i,v1)
        print('$',ng.keys(),vised,e)
        if e not in ng.keys() and g not in ng.keys() and e not in vised and g not in vised:
            for c,d in weighted_dic.items():
                if c==e or c==g:
                    ng[c]=d
                    print('#',c,e,ng)
    for c,d in ng.items():
        a=min(ng.values())
        if a==d:
            vised.append(c)
            v1,v2=c
            if vis[-1]==v2:
                vis.append(v1)
            elif vis[-1]==v1:
                vis.append(v2)
    if len(vis)==nv:
        break
print(vis)
print(vised)
print(nv)
                
'''                